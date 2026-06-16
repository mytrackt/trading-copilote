"""
Phase 3 — Assainissement du cerveau TRADEX-AI
Transforme aggregated_rules (strings) → objets {regle, statut, source_video_id, categorie, confiance, note}
Source statuts : KB_VALIDEE.json (match exact 1265/1265 vérifié)
"""
import json
import os
import tempfile
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_PATH = os.path.join(BASE_DIR, "KNOWLEDGE_BASE_MASTER.json")
VALIDEE_PATH = os.path.join(BASE_DIR, "validation", "KB_VALIDEE.json")
BACKUP_PATH = os.path.join(BASE_DIR, f"KNOWLEDGE_BASE_MASTER.bak_phase3_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

def atomic_write(path, data):
    """Écriture atomique : tempfile → os.replace"""
    tmp_fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise

def main():
    # 1. Charger les fichiers
    print("Chargement des fichiers...")
    with open(MASTER_PATH, 'r', encoding='utf-8') as f:
        kb_master = json.load(f)
    with open(VALIDEE_PATH, 'r', encoding='utf-8') as f:
        kb_validee = json.load(f)

    # 2. Backup atomique
    print(f"Backup → {os.path.basename(BACKUP_PATH)}")
    shutil.copy2(MASTER_PATH, BACKUP_PATH)

    # 3. Construire le lookup texte → métadonnées depuis KB_VALIDEE
    print("Construction du lookup texte→statut...")
    lookup = {}
    for cat, statuts in kb_validee['rules_by_status'].items():
        for statut, rules in statuts.items():
            for r in rules:
                texte = r.get('texte', '').strip()
                if texte:
                    lookup[texte] = {
                        "statut": r.get('statut', statut),
                        "source_video_id": r.get('source_video_id', None),
                        "confiance": r.get('confiance', None),
                        "note": r.get('note', None),
                    }
    print(f"  Lookup : {len(lookup)} entrées")

    # 4. Transformer aggregated_rules
    print("Transformation des règles...")
    agg = kb_master['aggregated_rules']
    new_agg = {}
    total = matched = unmatched = 0

    for cat, rules in agg.items():
        new_agg[cat] = []
        for r_str in rules:
            total += 1
            r_stripped = r_str.strip()
            meta = lookup.get(r_stripped, None)
            if meta:
                matched += 1
                new_agg[cat].append({
                    "regle": r_str,
                    "statut": meta["statut"],
                    "source_video_id": meta["source_video_id"],
                    "categorie": cat,
                    "confiance": meta["confiance"],
                    "note": meta["note"],
                })
            else:
                unmatched += 1
                new_agg[cat].append({
                    "regle": r_str,
                    "statut": "AMBIGU",
                    "source_video_id": None,
                    "categorie": cat,
                    "confiance": None,
                    "note": "⚠️ Statut non résolu lors de la transformation Phase3",
                })

    print(f"  Total : {total} | Matchés : {matched} | Non matchés : {unmatched}")

    if unmatched > 0:
        print(f"  ⚠️  {unmatched} règles sans correspondance — statut forcé à AMBIGU")

    # 5. Mise à jour metadata
    kb_master['aggregated_rules'] = new_agg
    kb_master['metadata']['phase3_transform'] = {
        "date": datetime.now().isoformat(),
        "rules_total": total,
        "rules_matched": matched,
        "rules_unmatched": unmatched,
        "description": "aggregated_rules converti de strings vers objets {regle, statut, source_video_id, categorie, confiance, note}"
    }

    # 6. Écriture atomique
    print(f"Écriture atomique → {os.path.basename(MASTER_PATH)}")
    atomic_write(MASTER_PATH, kb_master)

    # 7. Vérification post-écriture
    print("Vérification post-écriture...")
    with open(MASTER_PATH, 'r', encoding='utf-8') as f:
        kb_check = json.load(f)

    check_total = sum(len(v) for v in kb_check['aggregated_rules'].values())
    check_valide = sum(
        1 for rules in kb_check['aggregated_rules'].values()
        for r in rules if isinstance(r, dict) and r.get('statut') == 'VALIDE'
    )
    check_ambigu = sum(
        1 for rules in kb_check['aggregated_rules'].values()
        for r in rules if isinstance(r, dict) and r.get('statut') == 'AMBIGU'
    )
    check_invalide = sum(
        1 for rules in kb_check['aggregated_rules'].values()
        for r in rules if isinstance(r, dict) and r.get('statut') == 'INVALIDE'
    )

    print(f"\n✅ VÉRIFICATION :")
    print(f"   Total règles : {check_total} (attendu 1265)")
    print(f"   VALIDE  : {check_valide} (attendu 1166)")
    print(f"   AMBIGU  : {check_ambigu} (attendu 45)")
    print(f"   INVALIDE: {check_invalide} (attendu 54)")
    print(f"   Backup  : {os.path.basename(BACKUP_PATH)}")

    assert check_total == 1265, f"ERREUR total {check_total} ≠ 1265"
    assert check_valide == 1166, f"ERREUR VALIDE {check_valide} ≠ 1166"
    assert check_ambigu == 45, f"ERREUR AMBIGU {check_ambigu} ≠ 45"
    assert check_invalide == 54, f"ERREUR INVALIDE {check_invalide} ≠ 54"

    print("\n✅ Phase 3 terminée — KB transformée avec succès.")

if __name__ == "__main__":
    main()
