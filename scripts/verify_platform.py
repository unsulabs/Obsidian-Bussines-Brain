#!/usr/bin/env python3
"""Headless CI acceptance using synthetic data only; never opens a real vault."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent.parent
MACOS_ONLY = (
    'test_documentos.DocumentosTest.test_actual_darwin_system_aliases_if_present',
    'Requiere ejecución nativa sobre macOS',
)
WINDOWS_ONLY = {
    ('test_windows_fs.WindowsFilesystemTests.' + name, 'native Windows filesystem backend')
    for name in (
        'test_private_acl_is_real_and_existing_broad_acl_is_rejected',
        'test_write_read_immutable_conflict_and_mutable_replace',
        'test_permission_preserving_replace',
        'test_preserve_acl_creates_new_destination',
        'test_publication_inside_writer_lock_keeps_parent_pinned',
        'test_publication_handover_rejects_in_place_junction_mutation',
        'test_directory_preserves_body_exception_types',
        'test_restrictive_but_unprotected_acl_is_rejected',
        'test_windows_aliases_and_streams_rejected',
        'test_pinned_directory_cannot_be_renamed',
        'test_junction_ancestor_rejected',
        'test_native_lock_blocks_and_releases_on_process_death',
    )
}


def write_report(output, name, report):
    report['commit'] = subprocess.check_output(
        ['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()
    text = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    (output / (name + '.json')).write_text(text, encoding='utf-8', newline='\n')
    print(json.dumps(report, ensure_ascii=True, indent=2))


def run_tests(output):
    # Same discovery, fixtures, result and execution semantics as the documented
    # `python -m unittest discover -s tests -v`; only reporting/skip policy differs.
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'))
    with (output / 'tests.log').open('w', encoding='utf-8', newline='\n') as log:
        result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
    skipped = [(test.id(), reason) for test, reason in result.skipped]
    allowed = {MACOS_ONLY} if sys.platform != 'darwin' else set()
    if sys.platform != 'win32':
        allowed |= WINDOWS_ONLY
    unexpected_skips = [entry for entry in skipped if entry not in allowed]
    passed = (result.wasSuccessful() and result.testsRun > 0
              and not unexpected_skips and not result.expectedFailures)
    report = {
        'platform': platform.platform(), 'python': sys.version,
        'result': 'PASS' if passed else 'FAIL',
        'tests_run': result.testsRun,
        'passed': result.testsRun - len(result.failures) - len(result.errors)
                  - len(skipped) - len(result.expectedFailures)
                  - len(result.unexpectedSuccesses),
        'failures': len(result.failures), 'errors': len(result.errors),
        'expected_failures': len(result.expectedFailures),
        'unexpected_successes': len(result.unexpectedSuccesses),
        'skipped': skipped, 'unexpected_skips': unexpected_skips,
        'skip_policy': 'The macOS alias test and twelve named Windows backend tests '
                       'may skip only off their native OS; their matrix job must execute them.',
    }
    write_report(output, 'tests', report)
    if not passed:
        print((output / 'tests.log').read_text(encoding='utf-8'), file=sys.stderr)
    return passed


def run_installation(output):
    from auditar_paquete import audit
    from exportar_producto import MANIFEST, es_ruta_privada

    report = {'platform': platform.platform(), 'python': sys.version,
              'result': 'FAIL', 'steps': [],
              'limits': 'Synthetic headless CLI checks; no Obsidian GUI, real '
                        'vault, account, or semantic business acceptance.'}

    def command(*args, expect=0):
        proc = subprocess.run([sys.executable, *map(str, args)], cwd=ROOT,
                              capture_output=True, text=True)
        report['steps'].append({'command': list(map(str, args)),
                                'exit_code': proc.returncode,
                                'stdout': proc.stdout, 'stderr': proc.stderr})
        if proc.returncode != expect:
            raise RuntimeError(f'{args[0]}: expected exit {expect}, got {proc.returncode}')
        return proc.stdout

    try:
        if sys.prefix == sys.base_prefix:
            raise RuntimeError('Run acceptance with the freshly installed virtual environment')
        command('scripts/cerebro.py', 'doctor')
        command('scripts/cerebro.py', '--help')
        command('scripts/check_docs.py')
        command('scripts/auditar_paquete.py')
        command('scripts/prueba_integral.py')
        with tempfile.TemporaryDirectory(prefix='ce-platform-') as temporary:
            root = Path(temporary)
            vault = root / 'Empresa sintética con espacios ñ'
            command('scripts/cerebro.py', 'crear', '--id', 'CI-SINTETICA',
                    '--nombre', 'Empresa sintética de prueba', '--dest', vault)
            command('scripts/cerebro.py', 'validar', '--vault', vault)
            command('scripts/cerebro.py', 'estado', '--vault', vault)
            command('scripts/cerebro.py', 'validar', '--vault', root / 'missing', expect=1)
            archive_path = root / 'producto sintético.zip'
            command('scripts/exportar_producto.py', '--dest', archive_path)
            with zipfile.ZipFile(archive_path) as archive:
                manifest = json.loads(archive.read(MANIFEST))
                entries = {name for name in archive.namelist() if not name.endswith('/')}
                expected = {item['ruta'] for item in manifest['archivos']}
                if entries != expected | {MANIFEST} or any(es_ruta_privada(p) for p in entries):
                    raise RuntimeError('Export entries do not match manifest or contain private paths')
                for item in manifest['archivos']:
                    data = archive.read(item['ruta'])
                    if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
                        raise RuntimeError('Export manifest hash/size mismatch')
                archive.extractall(root / 'export')
            export_audit = audit(root / 'export')
            if export_audit['problemas']:
                raise RuntimeError(str(export_audit['problemas']))
            report['export'] = {'commit': manifest['commit'], 'files': len(expected),
                                'all_manifest_hashes_verified': True, 'audit': export_audit}
        report['result'] = 'PASS'
    except Exception as exc:
        report['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        write_report(output, 'installation', report)
    return report['result'] == 'PASS'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('phase', choices=['tests', 'installation'])
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents:
        parser.error('Evidence must be outside the product checkout')
    output.mkdir(parents=True, exist_ok=True)
    return 0 if (run_tests(output) if args.phase == 'tests' else run_installation(output)) else 1


if __name__ == '__main__':
    raise SystemExit(main())
