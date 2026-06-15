"""
Phase B-06 — Integration manuelle des regles Belkhayate Video 10 (Money Management).
Source : Belkhayate Trading Video 10 (officielle) | statut : VALIDE (valide par l'utilisateur).

aggregated_rules ne stockant que des chaines, la provenance (source + statut) est tracee dans :
  - AUDIT_KB_RESULTS.json (statut=VALIDE + motif source)
  - metadata.ajouts_manuels (liste)
Idempotent : une regle deja presente (texte exact) n'est pas re-ajoutee.
Ecriture atomique (tempfile + os.replace).
"""
import os
import sys
import json
import tempfile
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'KNOWLEDGE_BASE_MASTER.json')
RESULTS_PATH = os.path.join(BASE_DIR, '..', '04-cerveau-trading', 'AUDIT_KB_RESULTS.json')

SOURCE = "Belkhayate Trading Vidéo 10 (officielle)"

NOUVELLES_REGLES = {
    "psychologie": [
        "Le money management représente environ 70% du succès du trader (Belkhayate).",
        "L'analyse fondamentale a une importance quasi nulle (environ 0,5%) selon Belkhayate.",
        "Les informations et rumeurs financières sont inutiles pour un trading dont l'entrée/sortie dure moins d'une minute.",
        "Ne jamais perdre, même un seul dirham : la préservation du capital prime sur le gain.",
        "Dès qu'on commence à perdre, il devient exponentiellement plus difficile de revenir à l'équilibre.",
    ],
    "gestion_risque_entree": [
        "Asymétrie des pertes : perdre 50% du capital exige ensuite +100% pour revenir à zéro.",
        "Asymétrie des pertes : perdre 75% du capital exige ensuite +300% pour revenir à zéro.",
        "Toujours calculer le poids de la position avant d'entrer.",
        "L'analyse technique/graphique est le 2e facteur de succès, après le money management.",
    ],
}


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


def main():
    kb = load_json(KB_PATH)
    results = load_json(RESULTS_PATH)
    agg = kb['aggregated_rules']

    total_avant = sum(len(v) for v in agg.values())
    print(f"Total regles AVANT : {total_avant}")

    ajoutes = []
    for cat, regles in NOUVELLES_REGLES.items():
        agg.setdefault(cat, [])
        results.setdefault('categories', {}).setdefault(cat, [])
        for txt in regles:
            if txt in agg[cat]:
                print(f"  SKIP (deja present) [{cat}] {txt[:50]}...")
                continue
            agg[cat].append(txt)
            idx = len(agg[cat]) - 1
            results['categories'][cat].append({
                "index": idx,
                "regle": txt,
                "statut": "VALIDE",
                "motif": f"[Ajout manuel V10] Source : {SOURCE}. Valide utilisateur.",
            })
            ajoutes.append({"categorie": cat, "regle": txt})
            print(f"  + [{cat}] {txt[:55]}...")

    total_apres = sum(len(v) for v in agg.values())
    print(f"Total regles APRES : {total_apres}  (ajoutees : {len(ajoutes)})")

    # Recalcul stats audit
    stats = {}
    for rows in results['categories'].values():
        for r in rows:
            stats[r['statut']] = stats.get(r['statut'], 0) + 1
    results['stats'] = stats
    print(f"Stats audit : {stats}")

    # metadata
    kb['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()
    kb['metadata'].setdefault('ajouts_manuels', []).append({
        "phase": "B-06",
        "source": SOURCE,
        "statut": "VALIDE",
        "nb_regles": len(ajoutes),
        "regles": ajoutes,
        "rules_after": total_apres,
    })

    save_atomic(RESULTS_PATH, results)
    save_atomic(KB_PATH, kb)
    print("Sauvegardes atomiques OK (KB + audit).")

    # Validation JSON finale (json.loads strict)
    with open(KB_PATH, 'r', encoding='utf-8') as f:
        json.loads(f.read())
    with open(RESULTS_PATH, 'r', encoding='utf-8') as f:
        json.loads(f.read())
    print("Validation json.loads : OK (KB + audit valides).")


if __name__ == '__main__':
    main()
