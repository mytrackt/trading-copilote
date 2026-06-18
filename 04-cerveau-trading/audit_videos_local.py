# -*- coding: utf-8 -*-
"""
audit_videos_local.py — Audit des vidéos Belkhayate AVANT transcription Whisper medium.

Pipeline en 3 filtres (responsabilite unique par fonction) :
  - Exclusions absolues : OFTC / darija / arabe dans le nom -> HORS_PERIMETRE (aucune analyse)
  - Filtre 1 : deduplication par duree (interne) et titre (vs MANIFESTE, fuzzy >= 80)
  - Filtre 3 : echantillon 60s -> Whisper tiny -> classification FR / trading

Sortie : AUDIT_VIDEOS_LOCAL.csv (ecriture atomique).

NOTE de verite (verifie le 2026-06-18) :
  Le MANIFESTE ne contient PAS de colonne 'duree'. Le statut DOUBLON_EXACT par duree
  vs MANIFESTE est donc impossible et n'est pas simule. La detection de doublon vs
  MANIFESTE se fait uniquement par titre (DOUBLON_TITRE). Le DOUBLON_INTERNE par duree
  entre les videos locales reste pleinement actif.
"""

import os
import re
import csv
import json
import shutil
import subprocess
import tempfile

# ---------------------------------------------------------------------------
# Chemins
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # C:\trading-copilote
VIDEOS_DIR = r"D:\Belkhayate-Videos"
MANIFESTE = os.path.join(
    BASE_DIR, "03-transcriptions", "nouvelles-sources",
    "belkhayate-youtube", "MANIFESTE_TRANSCRITS.csv",
)
TEMP_DIR = os.path.join(BASE_DIR, "_temp")
OUTPUT_CSV = os.path.join(BASE_DIR, "04-cerveau-trading", "AUDIT_VIDEOS_LOCAL.csv")

VIDEO_EXTS = (".mp4", ".mov", ".m4v", ".avi", ".mkv", ".webm", ".flv", ".wmv")

# ---------------------------------------------------------------------------
# Constantes de classification
# ---------------------------------------------------------------------------
EXCLUSION_PATTERNS = ("oftc", "darija", "arabe")

TRADING_KEYWORDS = (
    "belkhayate", "gravity center", "pivot", "bande", "energie", "énergie",
    "resistance", "résistance", "support", "tendance", "signal", "indicateur",
    "trading", "marche", "marché", "bougie", "volume", "stop", "profit",
)

# Mots-outils francais courants pour confirmer "francais identifiable"
FRENCH_STOPWORDS = (
    " le ", " la ", " les ", " un ", " une ", " des ", " du ", " de ",
    " et ", " est ", " pour ", " que ", " qui ", " dans ", " avec ",
    " vous ", " nous ", " je ", " sur ", " ce ", " cette ", " pas ",
    " plus ", " mais ", " son ", " sa ", " ses ", " au ", " aux ",
)

ARABIC_RE = re.compile(r"[؀-ۿ]")

DUREE_TOLERANCE = 5.0   # secondes (DOUBLON_INTERNE)
FUZZY_SEUIL = 80        # ratio fuzzywuzzy (DOUBLON_TITRE)


# ---------------------------------------------------------------------------
# Filtre exclusions
# ---------------------------------------------------------------------------
def est_exclu(nom_fichier):
    """Retourne le motif d'exclusion (str) ou None. Insensible a la casse."""
    bas = nom_fichier.lower()
    for motif in EXCLUSION_PATTERNS:
        if motif in bas:
            return motif
    return None


# ---------------------------------------------------------------------------
# MANIFESTE : extraction des titres de reference
# ---------------------------------------------------------------------------
def charger_titres_manifeste():
    """
    Lit la colonne 'fichier' du MANIFESTE et en extrait un titre normalise.
    Format observe : '<ID>_<titre>.txt'. On retire le prefixe ID et l'extension.
    Retourne une liste de titres (str). Vide si MANIFESTE absent/illisible.
    """
    if not os.path.isfile(MANIFESTE):
        print(f"  [MANIFESTE] absent : {MANIFESTE}")
        return []
    titres = []
    try:
        with open(MANIFESTE, "r", encoding="utf-8-sig", newline="") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                brut = (row.get("fichier") or "").strip()
                if not brut:
                    continue
                titres.append(_titre_depuis_nom_manifeste(brut))
    except Exception as exc:  # lecture defensive, ne pas crasher
        print(f"  [MANIFESTE] erreur lecture : {exc}")
        return []
    return [t for t in titres if t]


def _titre_depuis_nom_manifeste(brut):
    """'-OIGv5rLLV8_Belkhayate : Lesson 46.txt' -> 'belkhayate : lesson 46'."""
    sans_ext = re.sub(r"\.txt$", "", brut, flags=re.IGNORECASE)
    # retirer le prefixe ID youtube (tout avant le premier '_')
    if "_" in sans_ext:
        sans_ext = sans_ext.split("_", 1)[1]
    return _normaliser_titre(sans_ext)


def _normaliser_titre(s):
    s = s.lower().strip()
    s = s.replace("：", ":")  # fullwidth colon present dans le manifeste
    s = re.sub(r"\s+", " ", s)
    return s


# ---------------------------------------------------------------------------
# ffprobe : metadonnees video
# ---------------------------------------------------------------------------
def sonder_video(chemin):
    """
    Retourne dict {duree_s, taille_mo, titre_metadata} ou {'erreur': msg}.
    Robuste : toute erreur ffprobe est capturee, ne crashe jamais le script.
    """
    taille_mo = round(os.path.getsize(chemin) / (1024 * 1024), 2)
    cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_streams", "-show_format", chemin,
    ]
    try:
        out = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=120,
        )
        if out.returncode != 0 or not out.stdout.strip():
            return {"erreur": "ffprobe rc!=0", "taille_mo": taille_mo}
        data = json.loads(out.stdout)
    except Exception as exc:
        return {"erreur": f"ffprobe: {exc}", "taille_mo": taille_mo}

    duree = None
    fmt = data.get("format", {})
    if fmt.get("duration"):
        try:
            duree = round(float(fmt["duration"]), 2)
        except (TypeError, ValueError):
            duree = None
    titre = (fmt.get("tags", {}) or {}).get("title", "") or ""
    return {
        "duree_s": duree,
        "taille_mo": taille_mo,
        "titre_metadata": titre.strip(),
    }


# ---------------------------------------------------------------------------
# Filtre 1 : doublons
# ---------------------------------------------------------------------------
def detecter_doublon_titre(titre_meta, titres_manifeste, fuzz):
    """Retourne (True, meilleur_ratio) si un titre du MANIFESTE matche >= seuil."""
    if not titre_meta or not titres_manifeste or fuzz is None:
        return False, 0
    cible = _normaliser_titre(titre_meta)
    if not cible:
        return False, 0
    meilleur = 0
    for ref in titres_manifeste:
        r = fuzz.ratio(cible, ref)
        if r > meilleur:
            meilleur = r
    return meilleur >= FUZZY_SEUIL, meilleur


# ---------------------------------------------------------------------------
# Filtre 3 : echantillon 60s + Whisper tiny
# ---------------------------------------------------------------------------
def extraire_echantillon(chemin_video, wav_path):
    """Extrait 60s audio mono 16kHz. Retourne True si le wav est cree."""
    cmd = [
        "ffmpeg", "-i", chemin_video, "-t", "60",
        "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav_path, "-y",
    ]
    try:
        out = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=180,
        )
        return out.returncode == 0 and os.path.isfile(wav_path) and os.path.getsize(wav_path) > 0
    except Exception as exc:
        print(f"    [ffmpeg] erreur : {exc}")
        return False


def transcrire_tiny(wav_path):
    """Lance Whisper tiny FR sur le wav, lit le .txt genere. Retourne le texte ou None."""
    cmd = [
        "whisper", wav_path, "--language", "fr", "--model", "tiny",
        "--output_format", "txt", "--output_dir", TEMP_DIR,
    ]
    try:
        out = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=600,
        )
    except Exception as exc:
        print(f"    [whisper] erreur : {exc}")
        return None
    base = os.path.splitext(os.path.basename(wav_path))[0]
    txt_path = os.path.join(TEMP_DIR, base + ".txt")
    if not os.path.isfile(txt_path):
        if out.returncode != 0:
            print(f"    [whisper] rc={out.returncode}")
        return None
    try:
        with open(txt_path, "r", encoding="utf-8", errors="replace") as fh:
            texte = fh.read()
    except Exception:
        texte = None
    _supprimer(txt_path)
    return texte


def classifier_transcript(texte):
    """Retourne (statut, raison) selon le contenu du transcript 60s."""
    if not texte or not texte.strip():
        return "HORS_PERIMETRE", "transcript vide"
    bas = " " + texte.lower() + " "

    if ARABIC_RE.search(texte) or "darija" in bas:
        return "HORS_PERIMETRE", "arabe/darija detecte dans l'audio"

    for kw in TRADING_KEYWORDS:
        if kw in bas:
            return "A_TRANSCRIRE", f"mot-cle trading: '{kw}'"

    francais = any(sw in bas for sw in FRENCH_STOPWORDS)
    if francais:
        return "FAIBLE_INTERET", "francais confirme, aucun mot-cle trading"
    return "HORS_PERIMETRE", "aucun mot francais identifiable"


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------
def _supprimer(path):
    try:
        if path and os.path.isfile(path):
            os.remove(path)
    except OSError:
        pass


def _slug(nom):
    """Nom de fichier sur pour le wav temporaire."""
    base = os.path.splitext(nom)[0]
    return re.sub(r"[^A-Za-z0-9_-]+", "_", base)[:80]


def ecrire_csv_atomique(lignes):
    """Ecrit le CSV via .tmp puis os.replace (atomique)."""
    champs = ["fichier", "taille_mo", "duree_s", "titre_metadata",
              "statut", "raison", "priorite"]
    tmp = OUTPUT_CSV + ".tmp"
    with open(tmp, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=champs)
        writer.writeheader()
        for l in lignes:
            writer.writerow({c: l.get(c, "") for c in champs})
    os.replace(tmp, OUTPUT_CSV)


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------
def main():
    os.makedirs(TEMP_DIR, exist_ok=True)

    try:
        from fuzzywuzzy import fuzz
    except ImportError:
        print("[AVERTISSEMENT] fuzzywuzzy absent : DOUBLON_TITRE desactive.")
        fuzz = None

    if not os.path.isdir(VIDEOS_DIR):
        print(f"[ERREUR] dossier video introuvable : {VIDEOS_DIR}")
        return

    videos = sorted(
        f for f in os.listdir(VIDEOS_DIR)
        if os.path.splitext(f)[1].lower() in VIDEO_EXTS
        and os.path.isfile(os.path.join(VIDEOS_DIR, f))
    )
    total = len(videos)
    print(f"[INFO] {total} videos detectees dans {VIDEOS_DIR}")

    titres_manifeste = charger_titres_manifeste()
    print(f"[INFO] {len(titres_manifeste)} titres charges du MANIFESTE")

    resultats = []
    durees_vues = []  # [(duree, nom_premier)] pour DOUBLON_INTERNE

    for idx, nom in enumerate(videos, 1):
        chemin = os.path.join(VIDEOS_DIR, nom)
        ligne = {
            "fichier": nom, "taille_mo": "", "duree_s": "",
            "titre_metadata": "", "statut": "", "raison": "", "priorite": "",
        }

        # --- Exclusions absolues (aucune analyse) ---
        motif = est_exclu(nom)
        if motif:
            ligne["taille_mo"] = round(os.path.getsize(chemin) / (1024 * 1024), 2)
            ligne["statut"] = "HORS_PERIMETRE"
            ligne["raison"] = f"exclusion nom: '{motif}'"
            resultats.append(ligne)
            print(f"[{idx}/{total}] {nom} -> HORS_PERIMETRE (exclu: {motif})")
            continue

        # --- ffprobe ---
        info = sonder_video(chemin)
        ligne["taille_mo"] = info.get("taille_mo", "")
        if "erreur" in info:
            ligne["statut"] = "ERREUR"
            ligne["raison"] = info["erreur"]
            resultats.append(ligne)
            print(f"[{idx}/{total}] {nom} -> ERREUR ({info['erreur']})")
            continue

        duree = info.get("duree_s")
        titre_meta = info.get("titre_metadata", "")
        ligne["duree_s"] = duree if duree is not None else ""
        ligne["titre_metadata"] = titre_meta

        # --- Filtre 1a : doublon interne par duree ---
        doublon_interne = None
        if duree is not None:
            for d_vue, nom_vue in durees_vues:
                if abs(d_vue - duree) <= DUREE_TOLERANCE:
                    doublon_interne = nom_vue
                    break
        if doublon_interne:
            ligne["statut"] = "DOUBLON_INTERNE"
            ligne["raison"] = f"meme duree (+/-{int(DUREE_TOLERANCE)}s) que '{doublon_interne}'"
            resultats.append(ligne)
            print(f"[{idx}/{total}] {nom} -> DOUBLON_INTERNE")
            continue
        if duree is not None:
            durees_vues.append((duree, nom))

        # --- Filtre 1b : doublon de titre vs MANIFESTE ---
        est_dup, ratio = detecter_doublon_titre(titre_meta, titres_manifeste, fuzz)
        if est_dup:
            ligne["statut"] = "DOUBLON_TITRE"
            ligne["raison"] = f"titre fuzzy {ratio} >= {FUZZY_SEUIL} vs MANIFESTE"
            resultats.append(ligne)
            print(f"[{idx}/{total}] {nom} -> DOUBLON_TITRE (ratio {ratio})")
            continue

        # --- Filtre 3 : echantillon 60s + Whisper tiny ---
        wav_path = os.path.join(TEMP_DIR, f"sample_{_slug(nom)}.wav")
        if not extraire_echantillon(chemin, wav_path):
            _supprimer(wav_path)
            ligne["statut"] = "ERREUR"
            ligne["raison"] = "extraction audio 60s echouee"
            resultats.append(ligne)
            print(f"[{idx}/{total}] {nom} -> ERREUR (ffmpeg)")
            continue

        texte = transcrire_tiny(wav_path)
        _supprimer(wav_path)  # nettoyage wav temporaire
        statut, raison = classifier_transcript(texte)
        ligne["statut"] = statut
        ligne["raison"] = raison
        resultats.append(ligne)
        print(f"[{idx}/{total}] {nom} -> {statut}")

    # --- Priorisation : A_TRANSCRIRE par duree ASC ---
    a_transcrire = [l for l in resultats if l["statut"] == "A_TRANSCRIRE"]
    a_transcrire.sort(key=lambda l: (l["duree_s"] if isinstance(l["duree_s"], (int, float)) else 1e12))
    for rang, l in enumerate(a_transcrire, 1):
        l["priorite"] = rang

    # CSV trie : A_TRANSCRIRE (courtes d'abord) puis le reste
    autres = [l for l in resultats if l["statut"] != "A_TRANSCRIRE"]
    lignes_csv = a_transcrire + autres
    ecrire_csv_atomique(lignes_csv)

    _afficher_resume(resultats, a_transcrire)


def _afficher_resume(resultats, a_transcrire):
    print("\n" + "=" * 60)
    print("RESUME DE L'AUDIT")
    print("=" * 60)

    par_statut = {}
    for l in resultats:
        par_statut[l["statut"]] = par_statut.get(l["statut"], 0) + 1
    print("\nNombre par statut :")
    for st in sorted(par_statut):
        print(f"  {st:<18} : {par_statut[st]}")

    print(f"\nVideos A_TRANSCRIRE : {len(a_transcrire)}")

    exclues = sum(
        1 for l in resultats
        if l["statut"] in ("HORS_PERIMETRE", "DOUBLON_INTERNE", "DOUBLON_TITRE")
    )
    print(f"Videos ecartees     : {exclues}")
    print(f"Heures economisees  : {exclues * 1.5:.1f} h (ecartees x 1.5h)")

    print("\nListe finale A_TRANSCRIRE (par duree croissante) :")
    if not a_transcrire:
        print("  (aucune)")
    for l in a_transcrire:
        d = l["duree_s"]
        d_str = f"{d:.0f}s ({d/60:.1f} min)" if isinstance(d, (int, float)) else "duree inconnue"
        print(f"  [{l['priorite']:>3}] {d_str:<20} {l['fichier']}")

    print(f"\nCSV ecrit : {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
