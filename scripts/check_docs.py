#!/usr/bin/env python3
"""Check the declared EN/ES inventory and local Markdown links (stdlib only).

This checks files and GitHub-style heading anchors, not translation fidelity,
remote URLs, Mermaid rendering, or agreement between prose and implementation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
ROOT_DOCS = {
    'en': {'README.md', 'AGENTS.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
           'START_HERE.md', 'GET_STARTED_WITH_CODEX.md', 'CONTINUE_WITH_CODEX.md'},
    'es': {'README.es.md', 'EMPIEZA_AQUI.md', 'PROMPT_INICIO_CODEX.md',
           'PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md'},
}


def prose(text: str) -> str:
    return re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text)


def anchors(text: str) -> set[str]:
    result, counts = set(), {}
    for title in re.findall(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', prose(text), re.M):
        title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', title)
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return result


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    try:
        inventory = json.loads((root / 'docs/documentation-map.json').read_text())
        pairs = inventory['pairs']
        if inventory.get('version') != 1 or inventory.get('primary_language') != 'en' or not isinstance(pairs, list) or not pairs:
            raise ValueError('expected version 1, English primary, and nonempty pairs')
    except (OSError, ValueError, KeyError) as exc:
        return [f'inventory: {exc}']
    for item in inventory.get('preserved_documents', []):
        for field in ('path', 'topic_guide'):
            name = item.get(field, '')
            dest = (root / name).resolve()
            if root not in dest.parents or not dest.is_file():
                errors.append(f'missing or unsafe source reference {field}: {name}')
    paths, ids = set(), set()
    for pair in pairs:
        if not isinstance(pair, dict) or not all(isinstance(pair.get(k), str) and pair[k] for k in ('id', 'en', 'es')):
            errors.append(f'invalid pair: {pair!r}')
            continue
        if pair['id'] in ids:
            errors.append(f'duplicate id: {pair["id"]}')
        ids.add(pair['id'])
        for lang in ('en', 'es'):
            name = pair[lang]
            path = (root / name).resolve()
            if name in paths:
                errors.append(f'duplicate path: {name}')
            paths.add(name)
            if root not in path.parents or not path.is_file():
                errors.append(f'missing or unsafe {lang} document: {name}')
            if name not in ROOT_DOCS[lang] and not name.startswith(f'docs/{lang}/'):
                errors.append(f'wrong locale path: {name}')
    actual = {p.relative_to(root).as_posix() for lang in ('en', 'es')
              for p in (root / 'docs' / lang).rglob('*.md')}
    for name in sorted(actual - paths):
        errors.append(f'unpaired document: {name}')
    for name in sorted(paths):
        path = (root / name).resolve()
        if root not in path.parents or not path.is_file():
            continue
        text = prose(path.read_text(encoding='utf8'))
        references = dict(re.findall(r'^\s*\[([^]]+)\]:\s*<?([^\s>]+)>?', text, re.M))
        targets = re.findall(r'!?\[[^]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\'][^\n]*?["\'])?\s*\)', text)
        for label, ref in re.findall(r'\[([^]\n]+)\]\[([^]\n]*)\]', text):
            key = ref or label
            if key not in references:
                errors.append(f'{name}: missing link reference [{key}]')
            else:
                targets.append(references[key])
        targets.extend(references.values())
        for target in targets:
            url = urlsplit(target.strip('<>'))
            if url.scheme or url.netloc:
                continue
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if dest != root and root not in dest.parents:
                errors.append(f'{name}: link escapes repository: {target}')
            elif not dest.exists():
                errors.append(f'{name}: broken link: {target}')
            elif url.fragment and dest.suffix.lower() == '.md' and unquote(url.fragment) not in anchors(dest.read_text(encoding='utf8')):
                errors.append(f'{name}: broken anchor: {target}')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = check(args.root)
    for error in errors:
        print(error)
    print(f'Documentation inventory and local links: {"FAIL" if errors else "PASS"}')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
