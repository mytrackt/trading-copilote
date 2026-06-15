"""
Phase B-05 — Lever kb_provisoire apres validation echantillon 5% (5 desaccords/63 = 7.9% <= 10%).

Mutations DATA (le flag moteur KB_PROVISOIRE_DEFAUT est gere separement dans claude_brain.py) :
  - KB aggregated_rules[psychologie] : supprime la regle #8 (entrer en sens inverse apres perte).
  - AUDIT_KB_RESULTS.json : #29 et #60 DOUTEUX -> VALIDE (promues a la main),
    #8 -> SUPPRIME_MANUEL ; stats recalculees.
  - KB metadata : kb_provisoire=False + trace b05.
Ecriture atomique (tempfile + os.replace). Assertions : echec si un texte cible est introuvable.
"""
import os
import sys
import json
import tempfile
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'KNOWLEDGE_BASE_MASTER.json')
RESULTS_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'AUDIT_KB_RESULTS.json')

R8 = "S'entraîner à entrer en sens inverse dès une perte permet de déconnecter le cerveau de ses biais et de le former à suivre la réalité du marché."
R29 = "Vendre dans la zone rouge du Gravity Center (extrémité haute du canal)."
R60 = "Le marché oscille de part et d'autre de la ligne bleue (centre de gravité) entre les zones rouges et vertes."


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.JSONDecoder().raw_decode(f.read())[0]


def save_atomic(path, obj):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def set_statut(results, cat, texte, nouveau_statut, note):
    rows = results['categories'][cat]
    for r in rows:
        if r['regle'] == texte:
            ancien = r['statut']
            r['statut'] = nouveau_statut
            r['motif'] = f"[B05 manuel] {note} (ancien: {ancien}). " + r.get('motif', '')
            return ancien
    raise AssertionError(f"Texte introuvable dans audit[{cat}] : {texte[:60]}...")


def main():
    kb = load_json(KB_PATH)
    results = load_json(RESULTS_PATH)

    # 1. Supprimer #8 de la KB
    psy = kb['aggregated_rules']['psychologie']
    avant = len(psy)
    kb['aggregated_rules']['psychologie'] = [r for r in psy if r != R8]
    supprime = avant - len(kb['aggregated_rules']['psychologie'])
    assert supprime == 1, f"Regle #8 : attendu 1 suppression, obtenu {supprime} (texte introuvable ?)"
    print(f"KB psychologie : {avant} -> {len(kb['aggregated_rules']['psychologie'])} (#8 supprimee)")

    # 2. Statuts dans l'audit
    a29 = set_statut(results, 'structure_marche', R29, 'VALIDE', 'promue 5pct')
    a60 = set_statut(results, 'indicateurs_tendance', R60, 'VALIDE', 'promue 5pct')
    a8 = set_statut(results, 'psychologie', R8, 'SUPPRIME_MANUEL', 'supprimee de la KB (dangereuse)')
    print(f"Audit : #29 {a29}->VALIDE | #60 {a60}->VALIDE | #8 {a8}->SUPPRIME_MANUEL")

    # 3. Recalcul stats audit
    stats = {}
    for rows in results['categories'].values():
        for r in rows:
            stats[r['statut']] = stats.get(r['statut'], 0) + 1
    results['stats'] = stats
    print(f"Stats audit recalculees : {stats}")

    # 4. metadata KB : lever provisoire
    total_apres = sum(len(v) for v in kb['aggregated_rules'].values())
    kb['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()
    kb['metadata']['kb_provisoire'] = False
    kb['metadata'].setdefault('purge_b04', {})['kb_provisoire'] = False
    kb['metadata']['b05_lift'] = {
        'validation_5pct': '5 desaccords / 63 = 7.9% <= seuil 10%',
        'regles_supprimees_manuel': ['#8 entrer en sens inverse apres perte'],
        'regles_promues_valide': ['#29 vendre zone rouge COG', '#60 oscillation ligne bleue COG'],
        'rules_after': total_apres,
        'kb_provisoire': False,
        'note': 'Flag moteur KB_PROVISOIRE_DEFAUT=False dans claude_brain.py.',
    }
    print(f"KB metadata.kb_provisoire = False | regles totales : {total_apres}")

    save_atomic(RESULTS_PATH, results)
    save_atomic(KB_PATH, kb)
    print("Sauvegardes atomiques OK (KB + audit).")


if __name__ == '__main__':
    main()
