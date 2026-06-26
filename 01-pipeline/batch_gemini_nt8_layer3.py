"""
Batch Gemini — Layer 3 NinjaTrader / Claude AI Automation (Session S31)
Transcrit 5 videos YouTube sur "Claude AI Trading Automation with NinjaTrader"
via Gemini multimodal (audio + visuel des charts).

Layer 3 = connaissances NinjaTrader + Claude API (distinct de la KB Belkhayate Layer 2)
Sortie  : 03-transcriptions/nouvelles-sources/Claude NinjaTrader/
Idempotent : un transcript .txt deja present => SKIP.

Lancement :
    py C:\\trading-copilote\\01-pipeline\\batch_gemini_nt8_layer3.py
    py C:\\trading-copilote\\01-pipeline\\batch_gemini_nt8_layer3.py --only gPl_X7xkLW0
    py C:\\trading-copilote\\01-pipeline\\batch_gemini_nt8_layer3.py --test

Usage personnel uniquement. Pas de conseil financier.
"""

import os
import sys
import time
import subprocess
import importlib.util
from pathlib import Path

# ============================================================
# CHEMINS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # C:\trading-copilote

TRANSCRIBER_PATH = os.path.join(BASE_DIR, "05-saas", "utils", "gemini_transcriber.py")
TEMP_VIDEO_DIR   = Path(BASE_DIR) / "_temp" / "videos_layer3"
LOG_PATH         = Path(BASE_DIR) / "01-pipeline" / "batch_gemini_nt8_layer3_log.txt"
OUT_DIR          = Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources" / "Claude NinjaTrader"

TEMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# VIDEOS A TRANSCRIRE — Layer 3 NinjaTrader + Claude API
# 3 deja transcrits (SKIP auto) :
#   y_bsjZThP0o (DaviddTech), 1SLbe0k6x4I (Kasper Gold), HfEu7XPUnAU (DaviddTech)
# ============================================================

GROUPE_CLAUDE_NT8 = [
    "gPl_X7xkLW0",   # Claude AI Trading Automation NinjaTrader #1
    "RtHca3NU-D4",   # Claude AI Trading Automation NinjaTrader #2
    "7oJ1ExbuaxQ",   # Claude AI Trading Automation NinjaTrader #3
    "6njREUQAFdg",   # Claude AI Trading Automation NinjaTrader #4
    "lIMu8ysJW68",   # Claude AI Trading Automation NinjaTrader #5
]

# ============================================================
# IMPORT DU TRANSCRIBER (chemin avec tiret + chiffre => importlib)
# ============================================================

def charger_transcriber():
    """Charge gemini_transcriber.py par chemin absolu."""
    spec = importlib.util.spec_from_file_location("gemini_transcriber", TRANSCRIBER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# ============================================================
# LOG
# ============================================================

def log(message):
    """Ecrit dans le log + stdout avec horodatage."""
    ligne = time.strftime('%Y-%m-%d %H:%M:%S') + "  " + message
    print(ligne, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")

# ============================================================
# TELECHARGEMENT yt-dlp (MP4 720p max, retry 2x)
# ============================================================

def telecharger_video(video_id):
    """Telecharge la video en MP4 720p max dans TEMP_VIDEO_DIR.
    Retourne le Path du fichier ou None. Retry reseau 2x."""
    url = "https://www.youtube.com/watch?v=" + video_id
    sortie_modele = str(TEMP_VIDEO_DIR / (video_id + ".%(ext)s"))
    cible = TEMP_VIDEO_DIR / (video_id + ".mp4")

    cmd = [
        "yt-dlp",
        "-f", "bv*[height<=720]+ba/b[height<=720]/b",
        "--merge-output-format", "mp4",
        "--no-playlist",
        "--no-progress",
        "--quiet",
        "-o", sortie_modele,
        url,
    ]

    for tentative in range(1, 3):  # 2 tentatives max
        try:
            subprocess.run(cmd, capture_output=True, timeout=900, check=True)
        except subprocess.CalledProcessError as e:
            err = (e.stderr or b"").decode("utf-8", "ignore")[:160]
            log("    yt-dlp echec tentative " + str(tentative) + " : " + err)
            time.sleep(10)
            continue
        except Exception as e:
            log("    yt-dlp erreur tentative " + str(tentative) + " : " + str(e)[:160])
            time.sleep(10)
            continue

        if cible.exists() and cible.stat().st_size > 1024:
            return cible
        # Extension alternative (mkv, webm)
        candidats = sorted(TEMP_VIDEO_DIR.glob(video_id + ".*"))
        candidats = [c for c in candidats if c.suffix.lower() in (".mp4", ".mkv", ".webm")]
        if candidats:
            return candidats[0]
        log("    yt-dlp : fichier introuvable apres tentative " + str(tentative))
        time.sleep(10)

    return None

# ============================================================
# BOUCLE PRINCIPALE
# ============================================================

def traiter(video_ids, gt):
    nb_ok = 0
    nb_skip = 0
    nb_erreurs = 0
    total = len(video_ids)

    for i, video_id in enumerate(video_ids, 1):
        out_path = OUT_DIR / (video_id + "_gemini.txt")
        prefixe = "[" + str(i) + "/" + str(total) + "] " + video_id

        # 1) Idempotence — si transcript existant : SKIP
        if out_path.exists() and out_path.stat().st_size > 0:
            nb_skip += 1
            log(prefixe + " SKIP (transcript existant)")
            continue

        log(prefixe + " -> telechargement...")

        # 2) Telechargement
        video_path = telecharger_video(video_id)
        if video_path is None:
            nb_erreurs += 1
            log(prefixe + " [ERREUR] telechargement impossible")
            continue

        # 3) Transcription Gemini
        try:
            resultat = gt.transcrire_video(video_path)
        except Exception as e:
            nb_erreurs += 1
            log(prefixe + " [ERREUR] transcription exception : " + str(e)[:160])
            try:
                video_path.unlink()
            except Exception:
                pass
            continue

        if resultat.get("erreur"):
            nb_erreurs += 1
            log(prefixe + " [ERREUR] " + str(resultat["erreur"])[:160])
            try:
                video_path.unlink()
            except Exception:
                pass
            continue

        # 4) Sauvegarde atomique du transcript
        tmp = Path(str(out_path) + ".tmp")
        tmp.write_text(resultat["transcript"], encoding="utf-8")
        tmp.replace(out_path)

        # 5) Suppression video temporaire
        try:
            video_path.unlink()
        except Exception:
            pass

        nb_ok += 1
        nb_visuel = resultat["transcript"].count("[VISUEL:")
        nb_regles = resultat["transcript"].count("[REGLE:")
        log(prefixe + " [OK] -> " + out_path.name +
            " (" + str(nb_visuel) + " VISUEL, " + str(nb_regles) + " REGLE)")

        # 6) Pause entre appels API (rate limiting)
        time.sleep(2)

    log("==== TERMINE  OK:" + str(nb_ok) + "  SKIP:" + str(nb_skip) +
        "  ERREURS:" + str(nb_erreurs) + "  TOTAL:" + str(total) + " ====")
    return nb_ok, nb_skip, nb_erreurs


def main():
    gt = charger_transcriber()

    ids = list(GROUPE_CLAUDE_NT8)

    # Mode --only ID
    if "--only" in sys.argv:
        idx = sys.argv.index("--only") + 1
        cible_id = sys.argv[idx]
        if cible_id not in ids:
            log("[ERREUR] ID '" + cible_id + "' non trouve dans la liste")
            sys.exit(1)
        ids = [cible_id]
    # Mode --test (1ere video uniquement)
    elif "--test" in sys.argv:
        ids = [ids[0]]

    log("================ BATCH LAYER3 NT8 — S31 ================")
    log("Dossier sortie : " + str(OUT_DIR))
    log("Videos a traiter : " + str(len(ids)))
    for vid in ids:
        log("  - " + vid + "  (https://youtu.be/" + vid + ")")

    traiter(ids, gt)


if __name__ == "__main__":
    main()
