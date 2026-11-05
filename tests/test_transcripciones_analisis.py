"""Synthetic agent-authored fixture; passing tests does not certify semantic fidelity."""
import copy
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from transcripciones_segmentacion import segment_text
from transcripciones_analisis import analyze_parts, check_coverage, cache_key, validate_relation
from transcripciones_modelo import ModelError, sha256_bytes
from transcripciones_taxonomia import seed_taxonomy


def fixture():
    # Six deliberately authored statements across five subjects and one unreadable core.
    lines=["Luz: Propongo evaluar pedidos reales porque contienen excepciones.",
           "Luz: La web debe decir asistencia, sin prometer autonomía.",
           "Mateo: La carpeta requiere revisar permiso; entrenamiento no autorizado.",
           "Luz: Si el piloto tarda más de dos semanas, revisar el alcance.",
           "Mateo: El responsable humano decide los descuentos.",
           "Luz: Corrijo: la evaluación será sólo con pedidos sintéticos.",
           "[pasaje ilegible en la fuente recibida]"]
    data=b"".join(line.encode().ljust(128,b" ") for line in lines)
    segments=segment_text(data,"TR-synthetic","V-1",max_core_bytes=128)
    digest=sha256_bytes(data)
    spans=[dict(tr_id="TR-synthetic",version_id="V-1",text_sha256=digest,start=i*128,end=i*128+len(line.encode()),excerpt_sha256=sha256_bytes(line.encode())) for i,line in enumerate(lines)]
    kinds=["idea","decision","excepcion","excepcion","decision","correccion"]
    subjects=["A","B","C","D","E","A"]
    contents=["Propuesta de evaluar datos reales por sus excepciones", "Promesa limitada a asistencia", "Revisar permiso de carpeta; no autoriza entrenamiento", "Revisar alcance si supera dos semanas", "Descuentos decididos por humano", "Evaluación acotada a datos sintéticos"]
    common=dict(created_at="2026-11-04T00:00:00Z",producer_version="synthetic-agent-1")
    claims=[dict(schema_version="afirmacion.v1",**common,claim_id=f"C{i}",run_id="RUN-fixture",subject_id=subjects[i],kind=kinds[i],content=contents[i],
                 speaker_label=lines[i].split(":")[0],resolved_entity_id=None,attribution_state="etiqueta_sin_resolver",evidence_spans=[spans[i]],scope="synthetic-pilot",
                 asserted_at=None,valid_time=None,editorial_state="propuesta",validity_state="sin_verificar",expression="parafrasis",confidence_basis="Explicit synthetic utterance",limitations=[],supersedes_claim_id=None) for i in range(6)]
    relation=dict(schema_version="relacion.v1",**common,relation_id="R1",predicate="precisa",vocabulary_version="relaciones-banco.v1",source_ref=dict(kind="claim",id="C5",version_id="V-1"),target_ref=dict(kind="claim",id="C0",version_id="V-1"),source_evidence=[spans[5]],target_evidence=[spans[0]],rationale="La corrección tardía limita la propuesta inicial a datos sintéticos",scope="synthetic-pilot",valid_time=None,editorial_state="propuesta",reviewer=None,supersedes_relation_id=None)
    results=[dict(segment_id=s["segment_id"],status="sustantivo" if i<6 else "ilegible",summary=contents[i] if i<6 else "No se puede reconstruir el pasaje",subject_ids=[subjects[i]] if i<6 else [],claim_ids=[f"C{i}"] if i<6 else [],reason=None if i<6 else "Fuente recibida ilegible") for i,s in enumerate(segments)]
    matrix=[dict(subject_id=sid,description=contents[i],evidence_spans=[spans[j] for j,s in enumerate(subjects) if s==sid],claim_ids=[f"C{j}" for j,s in enumerate(subjects) if s==sid],destination=dict(kind="source",id="TR-synthetic",reason="Conservar propuesta sintética para revisión de arquitectura"),reasons=["Datos reales contienen excepciones"] if sid=="A" else [],exceptions=["Sólo sintéticos tras corrección"] if sid=="A" else []) for i,sid in enumerate("ABCDE")]
    reconciliation=dict(status="propuesta",reviewer=None,summary="Cinco asuntos; la corrección final restringe evaluación a sintéticos, mantiene límites de promesa, permiso, plazo y autoridad humana.",subject_ids=list("ABCDE"),corrections=[dict(earlier_claim_id="C0",later_claim_id="C5",relation_id="R1",rationale="Corrección explícita tardía")],open_conflicts=[],limitations=["Un núcleo ilegible", "Fixture sintético; aceptación semántica independiente pendiente"])
    args=dict(data=data,segments=segments,agent_results=results,claims=claims,relations=[relation],subject_matrix=matrix,global_reconciliation=reconciliation,analyzer_version="synthetic-agent-1",taxonomy_version="generic-1",canonical_context_hashes=[],permission_snapshot="1"*64,run_id="RUN-fixture")
    # Explicit semantic assignments authored for this fixture, not keyword inference.
    for subject in matrix:
        subject["classifications"]=[dict(category_id="CAT-criterio",axis="asunto")]
    matrix[0]["classifications"].extend([dict(category_id="CAT-evaluacion",axis="finalidad"),dict(category_id="CAT-propuesta",axis="estado")])
    matrix[2]["classifications"].append(dict(category_id="CAT-recurso",axis="entidad"))
    args["taxonomy"]=seed_taxonomy()
    return args


class AnalysisTests(unittest.TestCase):
    def test_resolved_attribution_requires_scoped_unambiguous_identity(self):
        args=fixture()
        args["claims"][0].update(attribution_state="resuelta",resolved_entity_id="ENTITY-LUZ",resolved_entity_kind="persona")
        with self.assertRaises(ModelError):analyze_parts(**args)
        entity=dict(entity_id="ENTITY-LUZ",name="Luz",kind="persona",scope="synthetic-pilot",aliases=[],identity_evidence=["Identidad acreditada por registro sintético del piloto"])
        args["taxonomy"]["entities"]=[entity]
        self.assertEqual(analyze_parts(**args)["run_id"],"RUN-fixture")
        for change in [lambda a:a["claims"][0].update(resolved_entity_id="ENTITY-MISSING"),
                       lambda a:a["claims"][0].update(resolved_entity_kind="company"),
                       lambda a:a["claims"][0].update(scope="other-company"),
                       lambda a:a["claims"][0].update(speaker_label="Speaker00"),
                       lambda a:a["taxonomy"]["entities"][0].update(identity_evidence=[]),
                       lambda a:a["taxonomy"]["entities"].append(dict(entity,entity_id="ENTITY-HOMONYM"))]:
            changed=copy.deepcopy(args);change(changed)
            with self.assertRaises(ModelError):analyze_parts(**changed)

    def test_classification_foreign_keys_and_version(self):
        args=fixture();run=analyze_parts(**args)
        self.assertEqual(len(run["subject_matrix"][0]["classifications"]),3)
        for change in [lambda a:a.update(taxonomy=None),
                       lambda a:a["taxonomy"].update(taxonomy_version="other"),
                       lambda a:a["subject_matrix"][0]["classifications"][0].update(category_id="unknown"),
                       lambda a:a["subject_matrix"][0]["classifications"][0].update(axis="actividad"),
                       lambda a:a["subject_matrix"][0].update(classifications=[])]:
            args=fixture();change(args)
            with self.assertRaises(ModelError):analyze_parts(**args)
    def test_endpoint_registry_and_wrong_source(self):
        args=fixture();relation=copy.deepcopy(args["relations"][0])
        sources={("TR-synthetic","V-1"):args["data"],("TR-other","V-2"):b"Other source"}
        refs={("claim","C5","V-1"),("claim","C0","V-1")}
        with self.assertRaisesRegex(ModelError,"REFERENCE_REGISTRY_REQUIRED"):
            validate_relation(relation,sources,refs)
        registry={("claim",c["claim_id"],"V-1"):c for c in args["claims"]}
        self.assertTrue(validate_relation(relation,sources,refs,ref_registry=registry))
        relation["source_ref"]=dict(kind="source",id="TR-other",version_id="V-2")
        with self.assertRaisesRegex(ModelError,"RELATION_EVIDENCE_MISMATCH"):
            validate_relation(relation,sources,refs|{("source","TR-other","V-2")},ref_registry=registry)
        relation=copy.deepcopy(args["relations"][0]);relation["source_evidence"]=relation["target_evidence"]
        with self.assertRaisesRegex(ModelError,"RELATION_EVIDENCE_MISMATCH"):
            validate_relation(relation,sources,refs,ref_registry=registry)
        registry[("claim","C5","V-1")]=args["claims"][0]
        with self.assertRaisesRegex(ModelError,"RELATION_REFERENCE_INVALID"):
            validate_relation(args["relations"][0],sources,refs,ref_registry=registry)

    def test_supersession_cycles_and_explicit_history(self):
        args=fixture();args["claims"][0]["supersedes_claim_id"]="C5";args["claims"][5]["supersedes_claim_id"]="C0"
        with self.assertRaisesRegex(ModelError,"CLAIM_CYCLE"):analyze_parts(**args)
        args=fixture();args["claims"][0]["supersedes_claim_id"]="H0"
        with self.assertRaisesRegex(ModelError,"CLAIM_REFERENCE_INVALID"):analyze_parts(**args)
        history=copy.deepcopy(args["claims"][0]);history.update(claim_id="H0",run_id="RUN-previous",supersedes_claim_id=None)
        args["historical_claims"]=[history]
        self.assertEqual(analyze_parts(**args)["run_id"],"RUN-fixture")
        history["supersedes_claim_id"]="C0"
        with self.assertRaisesRegex(ModelError,"CLAIM_CYCLE"):analyze_parts(**args)

    def test_five_subjects_late_correction_and_unreadable(self):
        args=fixture(); run=analyze_parts(**args)
        self.assertEqual(run["coverage"]["material_subjects"],5)
        self.assertEqual(run["coverage"]["examined_core_bytes"],len(args["data"]))
        self.assertEqual(run["coverage"]["state"],"parcial")
        self.assertEqual(run["coverage"]["semantic_acceptance"],"pending_independent_review")
        self.assertEqual(len(run["coverage"]["unreadable_segment_ids"]),1)

    def test_missing_part_subject_bad_span_and_correction(self):
        for mutate in [lambda a:a["agent_results"].pop(), lambda a:a["subject_matrix"].pop(),
                       lambda a:a["claims"][0]["evidence_spans"][0].update(start=1),
                       lambda a:a["global_reconciliation"]["corrections"][0].update(later_claim_id="missing"),
                       lambda a:a["claims"][0].update(resolved_entity_id="invented")]:
            args=fixture(); mutate(args)
            with self.assertRaises(ModelError): analyze_parts(**args)

    def test_cache_context_permission_taxonomy_analyzer(self):
        base=["0"*64,"v1","a1","t1",[],"1"*64]
        for i,value in [(2,"a2"),(3,"t2"),(4,["2"*64]),(5,"3"*64)]:
            variant=copy.deepcopy(base); variant[i]=value
            self.assertNotEqual(cache_key(*base),cache_key(*variant))

    def test_coverage_tampering_and_unknown_fields(self):
        args=fixture(); run=analyze_parts(**args)
        for key,val in [("invented",True),("cache_key","0"*64)]:
            bad=copy.deepcopy(run);bad[key]=val
            with self.assertRaises(ModelError):check_coverage(bad,args["segments"],args["claims"],args["relations"],args["data"],taxonomy=args["taxonomy"])
