"""
Gemini Multimodal Transcriber — TRADEX-AI
Transcription audio + visuel des videos Belkhayate via Gemini 2.5 Flash.
Construit en 3 phases — Phase 1 : squelette et utilitaires.
Audit v2.2 applique — toutes corrections bloquantes integrees.
Chunking automatique pour videos > 50 min (limite 1M tokens Gemini).
Usage personnel uniquement. Pas de conseil financier.
"""

import os
import sys
import time
import re
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from google import genai
from dotenv import load_dotenv

# Charger .env — chemin absolu obligatoire (Windows)
load_dotenv(r"C:\trading-copilote\.env")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# CONFIGURATION
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY manquant dans C:\\trading-copilote\\.env\n"
        "Ajouter la ligne : GEMINI_API_KEY=AIzaSy..."
    )

VIDEO_DIR = Path(r"D:\Belkhayate-Videos")
OUTPUT_DIR = Path(
    r"C:\trading-copilote\03-transcriptions"
    r"\nouvelles-sources\belkhayate-youtube\transcripts-gemini"
)
RAPPORT_PATH = Path(
    r"C:\trading-copilote\03-transcriptions"
    r"\nouvelles-sources\belkhayate-youtube\RAPPORT_QUALITE_GEMINI.md"
)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Modele stable (pas experimental)
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_NAME = "gemini-2.5-flash"

# Timeouts et retry
MAX_PROCESSING_WAIT_SECONDS = 300   # 5 min max pour l'upload Gemini
MAX_RETRIES = 3
RETRY_BACKOFF = [10, 30, 60]        # secondes entre tentatives

# Mots-cles detection video live
KEYWORDS_LIVE = ["live", "5 days challenge", "5 days", "session live", "trading live"]

# Limite Gemini : 1M tokens = environ 55 min de video (video 258 tok/s + audio 32 tok/s)
# On fixe la limite a 50 min avec marge de securite
DUREE_MAX_DIRECTE = 3000          # 50 min en secondes
CHUNK_DUREE = 2700                 # 45 min par chunk (marge securite)
TAILLE_SEUIL_OCTET = 200 * 1024 * 1024  # 200 Mo = declencheur verif duree

# ============================================================
# WRAPPER ASCII — evite l'erreur codec sur noms accentues
# ============================================================

class _AsciiFileWrapper:
    """
    Passe un nom ASCII au SDK Gemini lors de l'upload.
    Le SDK lit file.name pour l'en-tete HTTP Content-Disposition ;
    les noms accentues (Lecon, Marche...) declenchent une erreur ascii codec.
    Ce wrapper ouvre le fichier avec le vrai chemin Unicode mais expose
    un nom ASCII neutre -- zero copie, zero overhead disque.
    """
    def __init__(self, path: Path):
        self._f = open(str(path), "rb")
        self.name = "upload.mp4"   # nom ASCII neutre expose au SDK
        self.mode = "rb"

    def read(self, n=-1):
        return self._f.read(n)

    def seek(self, *args):
        return self._f.seek(*args)

    def tell(self):
        return self._f.tell()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self._f.close()

    def close(self):
        self._f.close()


# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================

def detecter_qualite(video_path: Path) -> str:
    """
    Evalue la qualite probable de la video par taille.
    Retourne FAIBLE_APPROX / MOYENNE_APPROX / BONNE_APPROX.
    Note : taille = proxy imparfait (H.265 compresse peut etre HD a 15 Mo).
    Le suffixe _APPROX rappelle que c'est une estimation.
    """
    taille_mo = video_path.stat().st_size / (1024 * 1024)
    if taille_mo < 30:
        return "FAIBLE_APPROX"
    elif taille_mo < 150:
        return "MOYENNE_APPROX"
    else:
        return "BONNE_APPROX"


def est_live(nom_fichier: str) -> bool:
    """
    Detecte si la video est un live trading par son nom.
    Insensible a la casse.
    """
    nom_lower = nom_fichier.lower()
    return any(kw.lower() in nom_lower for kw in KEYWORDS_LIVE)


def get_duree_video(video_path: Path) -> float:
    """
    Retourne la duree de la video en secondes via ffprobe.
    Retourne 0.0 si ffprobe est indisponible ou si la lecture echoue.
    """
    try:
        res = subprocess.run(
            ['ffprobe', '-v', 'quiet', '-print_format', 'json',
             '-show_format', str(video_path)],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(res.stdout)
        return float(data.get('format', {}).get('duration', 0))
    except Exception:
        return 0.0


def decouper_en_chunks(video_path: Path) -> list:
    """
    Decoupe la video en chunks de CHUNK_DUREE secondes via ffmpeg (-c copy).
    Utilise un dossier temp systeme — nettoye apres traitement.
    Retourne une liste de (Path_chunk, numero) ou [] si echec.
    """
    duree = get_duree_video(video_path)
    if duree == 0:
        return []

    temp_dir = Path(tempfile.mkdtemp(prefix="gemini_chunk_"))
    chunks = []
    n = 0

    while True:
        start = n * CHUNK_DUREE
        if start >= duree:
            break
        chunk_path = temp_dir / ("chunk" + str(n + 1).zfill(2) + "_upload.mp4")
        cmd = [
            'ffmpeg', '-y',
            '-i', str(video_path),
            '-ss', str(start),
            '-t', str(CHUNK_DUREE),
            '-c', 'copy',
            str(chunk_path)
        ]
        try:
            subprocess.run(cmd, capture_output=True, timeout=300, check=True)
            if chunk_path.exists() and chunk_path.stat().st_size > 1024:
                chunks.append((chunk_path, n + 1))
        except Exception as e:
            print(f"  Erreur decoupage chunk {n + 1} : {str(e)[:80]}")
            break
        n += 1

    return chunks


def flaguer_chiffres_visuels(texte: str) -> str:
    """
    Dans chaque bloc [VISUEL: ...], ajoute le flag A_VERIFIER
    apres chaque chiffre. Insensible a la casse (re.IGNORECASE).
    Multiligne (re.DOTALL) pour les blocs qui s'etendent sur plusieurs lignes.

    Exemple :
      Entree : [VISUEL: COG a 1852, prix actuel 1848]
      Sortie : [VISUEL: COG a 1852A_VERIFIER, prix actuel 1848A_VERIFIER]
    """
    def remplacer_chiffres(match):
        bloc = match.group(0)
        return re.sub(r'\b(\d+[\.,]?\d*)\b', r'\1A_VERIFIER', bloc)

    return re.sub(
        r'\[VISUEL:.*?\]',
        remplacer_chiffres,
        texte,
        flags=re.DOTALL | re.IGNORECASE
    )


# ============================================================
# CONSTRUCTION DU PROMPT
# ============================================================

def construire_prompt(nom_fichier: str, est_live_video: bool) -> str:
    """
    Construit le prompt Gemini adapte au type de video.
    Les videos live ont une instruction supplementaire pour les moments rapides.
    """
    instruction_live = ""
    if est_live_video:
        instruction_live = (
            "\nIMPORTANT - VIDEO LIVE TRADING : L'ecran peut changer tres rapidement. "
            "Si tu ne peux pas decrire precisement ce qui est affiche a un instant "
            "donne, ecris [ECRAN_CHANGE_RAPIDE] et continue avec la transcription "
            "audio. Ne jamais inventer une description visuelle si tu n'es pas "
            "certain de ce que tu vois.\n"
        )

    return """Tu es un transcripteur expert de videos de trading financier en francais.
Transcris cette video de Mustapha Belkhayate en integrant a la fois
l'audio ET le contenu visuel de l'ecran.

REGLE FONDAMENTALE :
Belkhayate enseigne en montrant son ecran (NinjaTrader, TradingView, etc.).
Quand il dit "vous voyez ici", "regardez la", "ici on a" etc., il fait
reference a quelque chose de visible sur son ecran. Tu dois decrire ce
que tu vois sur l'ecran a ce moment precis AVANT de retranscrire ses mots.

FORMAT OBLIGATOIRE :
- Pour chaque passage avec reference visuelle, utilise :
  [VISUEL: description precise de ce que tu vois a l'ecran]
  puis continue avec la transcription audio
- Pour les passages sans reference visuelle :
  transcris simplement ce que Belkhayate dit
- Quand Belkhayate enonce une regle claire et autonome, mets-la en evidence :
  [REGLE: formulation complete de la regle]

DESCRIPTIONS VISUELLES - CE QU'IL FAUT DECRIRE :
- Quel indicateur est visible ? (Belkhayate Trend, COG/Centre de Gravite,
  VWAP, Pivots, Volume Profile, Delta, Footprint)
- Quelle couleur a l'indicateur ? (vert = haussier, rouge = baissier,
  bleu/blanc = neutre)
- Le prix est-il au-dessus ou en dessous du COG / VWAP / moyenne mobile ?
- Y a-t-il une acceleration de volume visible ?
- Quelle est la tendance generale visible sur le graphique ?
- Quel marche est affiche ? (Or GC, Ble ZW, Petrole CL, Cuivre HG,
  SP500 ES, Dollar DX, VIX VX)
- Quel timeframe est affiche ? (5min, 15min, 1h, daily, range bars)

POUR LES PRIX ET NIVEAUX PRECIS - REGLE STRICTE :
NE JAMAIS donner un prix ou niveau chiffre exact lu a l'ecran.
Tu peux te tromper sur les decimales et cela serait dangereux
si ce chiffre etait utilise dans une decision de trading.
A la place, decris UNIQUEMENT en termes relatifs :
  AUTORISE  : "le prix est nettement au-dessus du Centre de Gravite"
  AUTORISE  : "le Centre de Gravite est en zone haute du graphique"
  AUTORISE  : "grand volume visible, bien superieur a la moyenne"
  INTERDIT  : "le COG est a 1852" ou "le prix est a 2340.5"
Exception unique : si Belkhayate PRONONCE lui-meme le chiffre verbalement
dans l'audio tu peux le transcrire (c'est de l'audio, pas du visuel).
""" + instruction_live + """
Exemple de sortie attendue :
  [VISUEL: Graphique Or GC 5min sur NinjaTrader. Belkhayate Trend rouge.
  Prix sous la moyenne mobile. Volume faible.]
  "Vous voyez ici on est en tendance baissiere sur l'or."
  [REGLE: Quand Belkhayate Trend est rouge et le prix est sous la MM,
  on cherche uniquement des signaux de vente.]
  "Donc dans cette configuration on ne cherche pas a acheter."

Transcris maintenant la video complete. Sois exhaustif.
"""


# ============================================================
# TRANSCRIPTION INTERNE (chunks + video entiere)
# ============================================================

def _transcrire_chunk(chunk_path, qualite, live, numero, nb_total):
    """
    Transcrit un chunk individuel. Retourne le texte brut ou None si echec.
    Gere upload, attente PROCESSING, retry et suppression Gemini.
    Les chunks ont des noms ASCII (chunk01_upload.mp4) — pas de probleme codec.
    """
    video_file = None
    try:
        with _AsciiFileWrapper(chunk_path) as _f:
            video_file = client.files.upload(
                file=_f,
                config={"mime_type": "video/mp4", "display_name": "chunk_upload.mp4"}
            )
        debut = time.time()
        while video_file.state.name == "PROCESSING":
            if time.time() - debut > MAX_PROCESSING_WAIT_SECONDS:
                return None
            time.sleep(5)
            video_file = client.files.get(name=video_file.name)
        if video_file.state.name == "FAILED":
            return None

        nom_affichage = "[chunk " + str(numero) + "/" + str(nb_total) + "] " + chunk_path.name
        prompt = construire_prompt(nom_affichage, live)

        for tentative in range(MAX_RETRIES):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=[video_file, prompt],
                    config=genai.types.GenerateContentConfig(
                        temperature=0.1,
                        max_output_tokens=32768
                    )
                )
                return response.text
            except Exception as e:
                if tentative < MAX_RETRIES - 1:
                    attente = 60 if ("429" in str(e)) else RETRY_BACKOFF[tentative]
                    print("    Chunk " + str(numero) + " tentative " + str(tentative + 1) + " : " + str(e)[:80])
                    time.sleep(attente)
        return None

    except Exception:
        return None
    finally:
        if video_file is not None:
            try:
                client.files.delete(name=video_file.name)
            except Exception:
                pass


def _transcrire_par_chunks(video_path, qualite, live):
    """
    Transcrit une video trop longue en la decoupant en chunks de CHUNK_DUREE secondes.
    Concatene les transcripts avec des marqueurs de coupure.
    Nettoie le dossier temp dans tous les cas (finally).
    """
    chunks = decouper_en_chunks(video_path)
    if not chunks:
        return {
            "erreur": (
                "Impossible de decouper la video. Verifier que ffmpeg et ffprobe "
                "sont installes et dans le PATH Windows."
            ),
            "qualite": qualite, "live": live
        }

    temp_dir = chunks[0][0].parent
    transcripts = []

    try:
        nb_total = len(chunks)
        for chunk_path, numero in chunks:
            taille_mo = chunk_path.stat().st_size / (1024 * 1024)
            print("  Chunk " + str(numero) + "/" + str(nb_total) + " upload (" + str(int(taille_mo)) + " Mo)...")
            texte = _transcrire_chunk(chunk_path, qualite, live, numero, nb_total)
            if texte:
                marqueur_debut = "[DEBUT_CHUNK_" + str(numero) + "/" + str(nb_total) + "]"
                marqueur_fin = "[FIN_CHUNK_" + str(numero) + "/" + str(nb_total) + "]"
                transcripts.append(marqueur_debut + "\n" + texte + "\n" + marqueur_fin)
                print("  Chunk " + str(numero) + "/" + str(nb_total) + " OK")
            else:
                transcripts.append("[CHUNK_" + str(numero) + "/" + str(nb_total) + "_ERREUR: transcription impossible]")
                print("  Chunk " + str(numero) + "/" + str(nb_total) + " ERREUR")
            time.sleep(2)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    if not any("DEBUT_CHUNK" in t for t in transcripts):
        return {"erreur": "Tous les chunks ont echoue", "qualite": qualite, "live": live}

    transcript_brut = "\n\n".join(transcripts)
    transcript_final = flaguer_chiffres_visuels(transcript_brut)

    nb_total = len(chunks)
    type_video = "LIVE_TRADING" if live else "COURS_PEDAGOGIQUE"
    entete = (
        "[QUALITE_VIDEO: " + qualite + "]\n"
        "[TYPE: " + type_video + "]\n"
        "[MODELE: " + MODEL_NAME + "]\n"
        "[DATE_TRANSCRIPTION: " + time.strftime('%Y-%m-%d') + "]\n"
        "[SOURCE: " + video_path.name + "]\n"
        "[TRAITEMENT: " + str(nb_total) + " CHUNKS x " + str(CHUNK_DUREE // 60) + " min]\n"
        "---\n"
    )

    return {
        "transcript": entete + transcript_final,
        "qualite": qualite, "live": live, "erreur": None
    }


# ============================================================
# TRANSCRIPTION PRINCIPALE
# ============================================================

def transcrire_video(video_path: Path) -> dict:
    """
    Transcrit une video avec Gemini 2.5 Flash.
    Retourne un dict :
      Success : {"transcript": str, "qualite": str, "live": bool, "erreur": None}
      Echec   : {"erreur": str, "qualite": str, "live": bool}

    Garde-fous integres :
    - Verif duree avant upload (chunking auto si > 50 min)
    - Timeout 300s sur la boucle PROCESSING (evite boucle infinie)
    - Retry 3x avec backoff exponentiel sur erreurs API
    - Pause 60s si erreur 429 (quota depasse)
    - max_output_tokens = 32768 (videos longues jusqu'a 2h)
    - Suppression du fichier Gemini dans finally (evite les fuites)
    """
    nom = video_path.name
    qualite = detecter_qualite(video_path)
    live = est_live(nom)
    video_file = None  # initialiser pour le bloc finally

    print(f"  Qualite estimee : {qualite}")
    print(f"  Type live       : {'OUI' if live else 'NON'}")

    # --- VERIFIER DUREE avant upload (toutes videos, sans seuil taille) ---
    # Bug fix : le seuil 200 Mo manquait les videos longues < 200 Mo (ex: OFTC Lesson 14)
    duree = get_duree_video(video_path)
    if duree > DUREE_MAX_DIRECTE:
        nb_chunks = int(duree / CHUNK_DUREE) + 1
        print("  Duree estimee   : " + str(int(duree / 60)) + " min — depasserait la limite Gemini (1M tokens)")
        print("  Decoupage auto  : " + str(nb_chunks) + " chunks de " + str(CHUNK_DUREE // 60) + " min")
        return _transcrire_par_chunks(video_path, qualite, live)

    try:
        # --- UPLOAD ---
        print(f"  Upload en cours vers Gemini Files API...")
        # _AsciiFileWrapper expose un nom ASCII au SDK (file.name = "upload.mp4")
        # Evite l'erreur 'ascii codec can't encode' sur les noms de fichiers accentues
        with _AsciiFileWrapper(video_path) as _f:
            video_file = client.files.upload(
                file=_f,
                config={"mime_type": "video/mp4", "display_name": "video_upload.mp4"}
            )

        # --- ATTENTE PROCESSING avec timeout ---
        debut_attente = time.time()
        while video_file.state.name == "PROCESSING":
            if time.time() - debut_attente > MAX_PROCESSING_WAIT_SECONDS:
                return {
                    "erreur": (
                        f"Timeout : fichier bloque en PROCESSING "
                        f"apres {MAX_PROCESSING_WAIT_SECONDS}s"
                    ),
                    "qualite": qualite,
                    "live": live
                }
            time.sleep(5)
            video_file = client.files.get(name=video_file.name)

        if video_file.state.name == "FAILED":
            return {
                "erreur": "Upload Gemini echoue (state=FAILED)",
                "qualite": qualite,
                "live": live
            }

        print(f"  Upload OK — transcription en cours...")

        # --- APPEL API avec retry ---
        prompt = construire_prompt(nom, live)
        transcript_brut = None

        for tentative in range(MAX_RETRIES):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=[video_file, prompt],
                    config=genai.types.GenerateContentConfig(
                        temperature=0.1,        # fidelite maximale
                        max_output_tokens=32768 # suffisant pour videos 2h
                    )
                )
                transcript_brut = response.text
                break  # succes -> sortir du retry

            except Exception as api_err:
                err_str = str(api_err)
                if tentative < MAX_RETRIES - 1:
                    # Pause longue si quota depasse
                    attente = (
                        60 if ("429" in err_str or "quota" in err_str.lower())
                        else RETRY_BACKOFF[tentative]
                    )
                    print(
                        f"  Erreur API (tentative {tentative + 1}/{MAX_RETRIES}) : "
                        f"{err_str[:120]}"
                    )
                    print(f"  Prochaine tentative dans {attente}s...")
                    time.sleep(attente)
                else:
                    return {
                        "erreur": f"Echec apres {MAX_RETRIES} tentatives : {err_str[:200]}",
                        "qualite": qualite,
                        "live": live
                    }

        if transcript_brut is None:
            return {
                "erreur": "Boucle retry terminee sans transcript (cas inattendu)",
                "qualite": qualite,
                "live": live
            }

        # --- POST-TRAITEMENT ---
        transcript_final = flaguer_chiffres_visuels(transcript_brut)

        type_video = "LIVE_TRADING" if live else "COURS_PEDAGOGIQUE"
        entete_lignes = [
            "[QUALITE_VIDEO: " + qualite + "]",
            "[TYPE: " + type_video + "]",
            "[MODELE: " + MODEL_NAME + "]",
            "[DATE_TRANSCRIPTION: " + time.strftime('%Y-%m-%d') + "]",
            "[SOURCE: " + nom + "]",
            "---"
        ]
        if "FAIBLE" in qualite:
            entete_lignes.append(
                "[ATTENTION: qualite video faible - verifier manuellement les [VISUEL]]"
            )
            entete_lignes.append("---")
        if live:
            entete_lignes.append(
                "[ATTENTION: video live - descriptions visuelles peuvent etre incompletes]"
            )
            entete_lignes.append("---")

        entete = "\n".join(entete_lignes) + "\n"

        return {
            "transcript": entete + transcript_final,
            "qualite": qualite,
            "live": live,
            "erreur": None
        }

    except Exception as e:
        return {
            "erreur": "Erreur inattendue : " + str(e)[:300],
            "qualite": qualite,
            "live": live
        }

    finally:
        if video_file is not None:
            try:
                client.files.delete(name=video_file.name)
            except Exception:
                pass


# ==========================================================
# RAPPORT ET BOUCLE PRINCIPALE
# ==========================================================

def generer_rapport(rapport: list, nb_ok: int, nb_skip: int,
                    nb_erreurs: int, duree_totale: float, nb_total: int):
    """Genere RAPPORT_QUALITE_GEMINI.md apres le traitement."""
    lignes = [
        "# RAPPORT QUALITE TRANSCRIPTIONS GEMINI",
        "",
        "- Date : " + time.strftime('%Y-%m-%d %H:%M'),
        "- Modele : " + MODEL_NAME,
        "- Total : " + str(nb_total) + " | OK : " + str(nb_ok) + " | Skip : " + str(nb_skip) + " | Erreurs : " + str(nb_erreurs),
        "- Duree : " + str(round(duree_totale / 60, 1)) + " minutes",
        "",
        "## Resultats par video",
        "",
        "| Fichier | Statut | Qualite | Live | Detail |",
        "|---------|--------|---------|------|--------|"
    ]
    for r in rapport:
        live_str = "OUI" if r.get("live") else "NON"
        lignes.append(
            "| " + r['fichier'] + " | " + r['statut'] + " | " + r.get('qualite', '?') +
            " | " + live_str + " | " + r.get('detail', '') + " |"
        )
    lignes += [
        "",
        "## Precautions de lecture",
        "",
        "- Chiffre A_VERIFIER : confirmer sur la video originale avant KB",
        "- [REGLE: ...] : passages les plus exploitables pour la KB TRADEX-AI",
        "- Descriptions relatives (haussier/baissier) : fiables",
        "- Chiffres exacts visuels : interdits - utiliser descriptions uniquement"
    ]
    RAPPORT_PATH.write_text("\n".join(lignes), encoding="utf-8")


def main():
    """Boucle principale : transcrit toutes les videos MP4 de VIDEO_DIR."""
    videos = sorted(VIDEO_DIR.glob("*.mp4"))
    if not videos:
        print(f"Aucun MP4 trouve dans {VIDEO_DIR}")
        sys.exit(1)

    cout_min = len(videos) * 0.02
    cout_max = len(videos) * 0.10
    duree_min = len(videos) * 3
    duree_max = len(videos) * 6

    print("=" * 60)
    print("  GEMINI TRANSCRIBER -- TRADEX-AI")
    print("=" * 60)
    print(f"  Modele       : {MODEL_NAME}")
    print(f"  Videos       : {len(videos)} fichiers dans {VIDEO_DIR}")
    print(f"  Sortie       : {OUTPUT_DIR}")
    print(f"  Cout estime  : {cout_min:.2f}EUR -- {cout_max:.2f}EUR")
    print(f"  Duree estimee: {duree_min} -- {duree_max} minutes")
    print()

    deja_faites = sum(
        1 for v in videos
        if (OUTPUT_DIR / f"{v.stem}_gemini.txt").exists()
    )
    if deja_faites > 0:
        print(f"  {deja_faites} video(s) deja traitees -- seront sautees (SKIP)")
        print(f"  {len(videos) - deja_faites} video(s) restantes a traiter")
    print()

    confirmation = input("Confirmes-tu le lancement ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("Annule.")
        sys.exit(0)
    print()

    rapport = []
    nb_ok = 0
    nb_skip = 0
    nb_erreurs = 0
    debut_global = time.time()

    for i, video in enumerate(videos, 1):
        out_path = OUTPUT_DIR / f"{video.stem}_gemini.txt"

        if out_path.exists():
            nb_skip += 1
            print(f"[{i:3d}/{len(videos)}] SKIP : {video.name}")
            continue

        print(f"[{i:3d}/{len(videos)}] {video.name}")
        debut_video = time.time()
        resultat = transcrire_video(video)
        duree_video = time.time() - debut_video

        if resultat.get("erreur"):
            nb_erreurs += 1
            err_msg = resultat["erreur"]
            print(f"  ERREUR : {err_msg}")
            rapport.append({
                "fichier": video.name,
                "statut": "ERREUR",
                "qualite": resultat.get("qualite", "?"),
                "live": resultat.get("live", False),
                "detail": resultat["erreur"][:120]
            })
        else:
            tmp_path = Path(str(out_path) + ".tmp")
            tmp_path.write_text(resultat["transcript"], encoding="utf-8")
            tmp_path.replace(out_path)
            nb_ok += 1
            nb_visuel = resultat["transcript"].count("[VISUEL:")
            nb_regles = resultat["transcript"].count("[REGLE:")
            print(f"  OK ({duree_video:.0f}s)")
            rapport.append({
                "fichier": video.name,
                "statut": "OK",
                "qualite": resultat["qualite"],
                "live": resultat["live"],
                "detail": f"{nb_visuel} VISUEL, {nb_regles} REGLE"
            })

        time.sleep(2)

    duree_totale = time.time() - debut_global
    generer_rapport(rapport, nb_ok, nb_skip, nb_erreurs, duree_totale, len(videos))

    print()
    print("=" * 60)
    print(f"  TERMINE -- OK: {nb_ok} | Skip: {nb_skip} | Erreurs: {nb_erreurs}")
    print(f"  Duree totale : {duree_totale / 60:.1f} minutes")
    print(f"  Rapport : {RAPPORT_PATH}")
    print("=" * 60)


# ==========================================================
# POINT D'ENTREE
# ==========================================================

if __name__ == "__main__":
    main()
