"""
Batch Gemini Transcription — TRADEX-AI (Session S30)
Telecharge 203 videos YouTube en MP4 720p puis les transcrit via Gemini
multimodal (gemini_transcriber.transcrire_video) audio + visuel des charts.

Idempotent : un transcript .txt deja present => SKIP.
Le fichier video temporaire est supprime apres chaque transcription reussie.
Usage personnel uniquement. Pas de conseil financier.

Lancement :
    py C:\\trading-copilote\\01-pipeline\\batch_gemini.py            (batch complet)
    py C:\\trading-copilote\\01-pipeline\\batch_gemini.py --test     (1 seule video : cPceiD1PWrI)
    py C:\\trading-copilote\\01-pipeline\\batch_gemini.py --only ID  (1 video precise)
"""

import os
import sys
import time
import shutil
import subprocess
import importlib.util
from pathlib import Path

# ============================================================
# CHEMINS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # C:\trading-copilote

TRANSCRIBER_PATH = os.path.join(BASE_DIR, "05-saas", "utils", "gemini_transcriber.py")
TEMP_VIDEO_DIR = Path(BASE_DIR) / "_temp" / "videos_batch"
LOG_PATH = Path(BASE_DIR) / "01-pipeline" / "batch_gemini_log.txt"

NS = Path(BASE_DIR) / "03-transcriptions" / "nouvelles-sources"
TG_AUDIO_DIR = NS / "The Trading Geek" / "audio"

TEMP_VIDEO_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# IMPORT DU TRANSCRIBER (chemin avec tiret + chiffre => importlib)
# ============================================================

def charger_transcriber():
    """Charge gemini_transcriber.py par chemin absolu (le dossier 05-saas
    n'est pas importable normalement). Execute le module-level code
    (verif cle API, instanciation client genai)."""
    spec = importlib.util.spec_from_file_location("gemini_transcriber", TRANSCRIBER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# ============================================================
# LISTE DES VIDEOS PAR GROUPE (ordre de priorite SOURCES_TRIAGE_S30)
# ============================================================

GROUPE_F_KASPER = [
    "cPceiD1PWrI", "1SLbe0k6x4I", "TXLqKZRx6hg", "RQ36kizIDk0", "6_BCuy5QYPc",
]

GROUPE_B_TTRADES = [
    "q3nauvjT3q0", "-ocfPuD_oqE", "v1X8UMWgWmI", "HbOeD_JVens", "yH4eYwUgdTY", "9BY-MQRNy-Y",
    "PQiRV0JMhIQ", "eywpZT3z6GQ", "Kf4c41_qO1s", "vn1RYjhJUnQ", "-KKuZb5Z5aU", "w-JekHg6Ldk",
    "tyoxl1l-6iI", "SlWxhzhLo3A", "3eVxTV_7L2U", "FAKWJ-1NlLE", "qdQYhePcvGE", "MvD7fQQ0szE",
    "m4k_1pF5zFI", "8BWkRGhuj1k", "VD4xb9VfMHA", "TNybDCtwBnc", "4Gm8p6O7Ebs", "WFqLwOp2pXw",
    "JHVaSKtE1Ys", "-wr4xATE37g", "r_UF8U-hsL8", "5fnFOh5YuM0", "4jU547ocod4", "iEaMbuFZb24",
    "ubCe509_JLY", "Ibw4saRtYMk", "LKNQDAdId4s", "TfHlNgAZ_II", "caaS6_Q7O78", "sIcsLFSNoXM",
    "EYzP7c24AwM", "FGkb_50BfT8", "WwmS47Gb3M0", "mwmWNCTEYtY",
]

# Groupe A : 14 DaviddTech + 1 Alex Carter (GlkJMO_ufYA)
GROUPE_A_DAVIDDTECH = [
    "h6qUy92Maco", "G7zv25c7Z8M", "4z1I0u1UnXQ", "cXhEw2jF4go", "y_bsjZThP0o", "EUSXhJNwRqI",
    "vIX6ztULs4U", "HfEu7XPUnAU", "lH5wrfNwL3k", "R7O2TaM709Y", "tkAq6g2Gjz4", "3IgYhw5WqTY",
    "Ebzawm73H4I", "jnJF0W2XgqA",
]
GROUPE_A_ALEXCARTER = [
    "GlkJMO_ufYA",
]

GROUPE_C_LEWIS = [
    "ZVMTeDBmSrI", "6njREUQAFdg", "4vZZReXFKkQ", "reiPfBnUBys", "aDWJ6lLemJU",
]

GROUPE_D_RAYNER = [
    "k1TKN8iGDao", "lLOKH4ThTP0", "tAR_JREOjvE", "pGO9MwMCJKo", "ej1UdL-oj_o",
    "YxiJRWBy8ZA", "yF6fCCz3IJU", "yKk_HmtE-Zc", "M9DCW8TaWuE",
]

GROUPE_E_HUMBLED = [
    "IqvnryFzZD4", "Vxj7QD6Lbvk", "YGpiVS8BNLw", "i37xXd_wI5k", "Eico0SYYNnk", "vswa9HZv7q4",
    "uV84kDLUgZ4", "GVbWx5x2i-Q", "T3sCLOvsdus", "UWKNLR4jOI0", "ZP_3AIko08w", "_Dqiuf-9Lps",
    "OLS9w6DOpOg", "UpmJJjKvJxo", "o4bB5UsgnX4", "IEu3NHVE_lQ",
]


def ids_trading_geek():
    """Extrait les 113 IDs YouTube depuis les noms de MP3 du dossier audio.
    Format fichier : {ID 11 chars}_{titre}.mp3 -> les 11 premiers caracteres."""
    if not TG_AUDIO_DIR.exists():
        return []
    ids = []
    for mp3 in sorted(TG_AUDIO_DIR.glob("*.mp3")):
        vid = mp3.stem[:11]
        if vid:
            ids.append(vid)
    return ids


def construire_taches():
    """Retourne la liste ordonnee des taches (id_video, dossier_sortie)."""
    taches = []

    def ajouter(ids, dossier):
        out = NS / dossier
        for vid in ids:
            taches.append((vid, out))

    # Ordre de priorite (DECISION 3, SOURCES_TRIAGE_S30)
    ajouter(GROUPE_F_KASPER, "Kasper Gold")
    ajouter(GROUPE_B_TTRADES, "TTrades")
    ajouter(GROUPE_A_DAVIDDTECH, "DaviddTech")
    ajouter(GROUPE_A_ALEXCARTER, "Alex Carter")
    ajouter(GROUPE_C_LEWIS, "Lewis Jackson")
    ajouter(GROUPE_D_RAYNER, "Rayner Teo")
    ajouter(GROUPE_E_HUMBLED, "Humbled Trader")
    ajouter(ids_trading_geek(), "The Trading Geek/transcripts-gemini")

    return taches

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

    for tentative in range(1, 3):  # 2 tentatives
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
        # parfois l'extension differe : prendre le 1er fichier {id}.*
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

def traiter(taches, gt):
    nb_ok = 0
    nb_skip = 0
    nb_erreurs = 0
    total = len(taches)

    for i, (video_id, dossier_sortie) in enumerate(taches, 1):
        dossier_sortie.mkdir(parents=True, exist_ok=True)
        out_path = dossier_sortie / (video_id + "_gemini.txt")

        prefixe = "[" + str(i) + "/" + str(total) + "] " + video_id

        # 1) Idempotence
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

        # 5) Suppression de la video temporaire
        try:
            video_path.unlink()
        except Exception:
            pass

        nb_ok += 1
        nb_visuel = resultat["transcript"].count("[VISUEL:")
        nb_regles = resultat["transcript"].count("[REGLE:")
        log(prefixe + " [OK] -> " + out_path.name +
            " (" + str(nb_visuel) + " VISUEL, " + str(nb_regles) + " REGLE)")

        # 6) Pause entre appels API
        time.sleep(2)

    log("==== TERMINE  OK:" + str(nb_ok) + "  SKIP:" + str(nb_skip) +
        "  ERREURS:" + str(nb_erreurs) + "  TOTAL:" + str(total) + " ====")
    return nb_ok, nb_skip, nb_erreurs


def main():
    gt = charger_transcriber()
    taches = construire_taches()

    # Modes : --test (1 video Kasper) ou --only ID
    cible_id = None
    if "--test" in sys.argv:
        cible_id = "cPceiD1PWrI"
    elif "--only" in sys.argv:
        cible_id = sys.argv[sys.argv.index("--only") + 1]
    if cible_id:
        taches = [t for t in taches if t[0] == cible_id]
        if not taches:
            log("Aucune tache pour l'ID " + cible_id)
            sys.exit(1)

    log("================ BATCH GEMINI S30 ================")
    log("Videos a traiter : " + str(len(taches)))

    traiter(taches, gt)


if __name__ == "__main__":
    main()
