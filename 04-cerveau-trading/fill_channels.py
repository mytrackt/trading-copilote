"""
Phase 4 — Assainissement du cerveau TRADEX-AI
Remplit le champ `channel` dans videos[] de KNOWLEDGE_BASE_MASTER.json
Sources : MANIFESTE_TRANSCRITS.csv + détection transcript_file + transcripts-bruts/
"""
import json, csv, os, tempfile
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MASTER_PATH = os.path.join(BASE_DIR, "KNOWLEDGE_BASE_MASTER.json")
MANIFESTE_PATH = os.path.join(
    BASE_DIR, "..", "03-transcriptions", "nouvelles-sources",
    "belkhayate-youtube", "MANIFESTE_TRANSCRITS.csv"
)
BRUTS_PATH = os.path.join(BASE_DIR, "..", "03-transcriptions", "transcripts-bruts")
BACKUP_PATH = os.path.join(
    BASE_DIR,
    f"KNOWLEDGE_BASE_MASTER.bak_phase4_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
)

CHANNEL_BELKHAYATE = "belkhayate-youtube (chaine officielle)"
CHANNEL_UNKNOWN    = "belkhayate-youtube (a_verifier)"

def atomic_write(path, data):
    tmp_fd, tmp_path = tempfile.mkstemp(dir=os.path.dirname(path), suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise

def build_lookup():
    """Construit video_id → channel via 3 sources."""
    lookup = {}

    # Source 1 : MANIFESTE_TRANSCRITS.csv
    with open(MANIFESTE_PATH, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            fname = row['fichier']
            vid_id = fname.split('_')[0]
            src = row.get('source', '').strip()
            # Normaliser : toutes les entrées MANIFESTE = chaine officielle
            lookup[vid_id] = CHANNEL_BELKHAYATE
    print(f"  Source 1 (MANIFESTE)       : {len(lookup)} entrées")

    return lookup

def detect_channel(vid_id, transcript_file, lookup):
    """Détecte le canal pour un video_id non dans le lookup."""
    # Source 2 : nom du transcript_file contient "Belkhayate"
    if transcript_file and 'elkhayate' in transcript_file:
        return CHANNEL_BELKHAYATE

    # Source 3 : présence dans transcripts-bruts/
    bruts_file = os.path.join(BRUTS_PATH, f"whisper_{vid_id}.txt")
    if os.path.exists(bruts_file):
        return CHANNEL_BELKHAYATE

    # Fallback
    return CHANNEL_UNKNOWN

def main():
    print("Chargement...")
    with open(MASTER_PATH, 'r', encoding='utf-8') as f:
        kb = json.load(f)

    import shutil
    print(f"Backup → {os.path.basename(BACKUP_PATH)}")
    shutil.copy2(MASTER_PATH, BACKUP_PATH)

    print("Construction du lookup...")
    lookup = build_lookup()

    print("Remplissage du champ channel...")
    stats = {"deja_rempli": 0, "manifeste": 0, "detection": 0, "fallback": 0}
    videos = kb.get("videos", {})

    for vid_id, vid_data in videos.items():
        current = vid_data.get("channel", "")
        if current and current not in ("", "INCONNU"):
            stats["deja_rempli"] += 1
            continue

        if vid_id in lookup:
            vid_data["channel"] = lookup[vid_id]
            stats["manifeste"] += 1
        else:
            tf = vid_data.get("transcript_file", "")
            detected = detect_channel(vid_id, tf, lookup)
            vid_data["channel"] = detected
            if detected == CHANNEL_UNKNOWN:
                stats["fallback"] += 1
            else:
                stats["detection"] += 1

    print(f"\n  Déjà remplis    : {stats['deja_rempli']}")
    print(f"  Via MANIFESTE   : {stats['manifeste']}")
    print(f"  Via détection   : {stats['detection']}")
    print(f"  Fallback (a_verifier): {stats['fallback']}")

    # Mettre à jour metadata
    kb["metadata"]["phase4_channels"] = {
        "date": datetime.now().isoformat(),
        "stats": stats,
        "description": "channel rempli via MANIFESTE + détection transcript_file + transcripts-bruts"
    }

    print(f"\nÉcriture atomique...")
    atomic_write(MASTER_PATH, kb)

    # Vérification
    with open(MASTER_PATH, 'r', encoding='utf-8') as f:
        kb_check = json.load(f)

    vids = kb_check["videos"]
    total = len(vids)
    filled = sum(1 for v in vids.values() if v.get("channel", ""))
    a_verifier = sum(1 for v in vids.values() if v.get("channel") == CHANNEL_UNKNOWN)
    officiel = sum(1 for v in vids.values() if v.get("channel") == CHANNEL_BELKHAYATE)

    print(f"\n✅ VÉRIFICATION :")
    print(f"   Total videos  : {total}")
    print(f"   Channel rempli: {filled}/{total}")
    print(f"   Officiels     : {officiel}")
    print(f"   À vérifier    : {a_verifier}")
    assert filled == total, f"ERREUR : {total - filled} videos sans channel"
    print("\n✅ Phase 4 terminée — champ channel renseigné pour tous les videos.")

if __name__ == "__main__":
    main()
