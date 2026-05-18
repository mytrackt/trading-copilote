# -*- coding: utf-8 -*-
"""
chunk_fuse.py
Pipeline Chunk & Fuse : Video → Spécifications Trading
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\chunk_fuse.py

PIPELINE 5 PHASES :
  Phase 1 : Téléchargement vidéo (yt-dlp)
  Phase 2 : Extraction keyframes à intervalle dynamique (ffmpeg)
  Phase 3 : Transcription SRT avec timestamps (yt-dlp subtitles)
  Phase 4 : N appels Claude ciblés — 1 frame + fenêtre transcript alignée
  Phase 5 : Fusion → guide technique .md structuré
"""

import os
import re
import sys
import json
import time
import base64
import random
import logging
import subprocess
import tempfile
import shutil
import urllib.request
import urllib.error
import traceback
from pathlib import Path
from datetime import datetime
from typing import TypedDict, Optional

# ── BASE_DIR (P2.10 / CLAUDE.md règle) ──────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _env_int(name: str, default: int) -> int:
    """Lit un entier depuis l'env. Retourne default si absent ou invalide."""
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default


# ── Configuration (P2.4 - tous overridables via TRANSVIDEO_*) ───────────────
OUTPUT_BASE    = os.path.join(BASE_DIR, "07-nouvelles sources")
MAX_FRAMES     = _env_int("TRANSVIDEO_MAX_FRAMES", 28)
RESOLUTION     = _env_int("TRANSVIDEO_RESOLUTION", 800)
MODEL          = os.getenv("TRANSVIDEO_MODEL", "claude-sonnet-4-6")
MAX_SIZE_MB    = _env_int("TRANSVIDEO_MAX_SIZE_MB", 500)
WINDOW_BEFORE  = _env_int("TRANSVIDEO_WINDOW_BEFORE", 5)
WINDOW_AFTER   = _env_int("TRANSVIDEO_WINDOW_AFTER", 20)
API_TIMEOUT    = _env_int("TRANSVIDEO_API_TIMEOUT", 60)
API_MAX_RETRIES = _env_int("TRANSVIDEO_API_MAX_RETRIES", 3)
FFPROBE_TIMEOUT = _env_int("TRANSVIDEO_FFPROBE_TIMEOUT", 30)
FFMPEG_TIMEOUT  = _env_int("TRANSVIDEO_FFMPEG_TIMEOUT", 300)
YTDLP_TITLE_TIMEOUT    = _env_int("TRANSVIDEO_YTDLP_TITLE_TIMEOUT", 60)
YTDLP_DOWNLOAD_TIMEOUT = _env_int("TRANSVIDEO_YTDLP_DOWNLOAD_TIMEOUT", 900)
YTDLP_PREVIEW_TIMEOUT  = _env_int("TRANSVIDEO_YTDLP_PREVIEW_TIMEOUT", 180)


# ── Types (P2.6) ────────────────────────────────────────────────────────────
class VideoEntry(TypedDict):
    url: str
    title: str
    duration: int
    description: str
    channel: str


class TranscriptSegment(TypedDict):
    start: int
    end: int
    text: str


class FrameInfo(TypedDict):
    path: str
    axis_path: str
    axis_wide_path: str
    ts_sec: float
    ts_str: str


# ── Logger (P2.2) ───────────────────────────────────────────────────────────
logger = logging.getLogger("transvideo.chunk_fuse")


# Cache module-level pour list_existing_content (P1.5)
_EXISTING_KB_CACHE: Optional[list] = None

# ── Prompts analyse 2 passes (Phase 4) ─────────────────────────────────────
PROMPT_PASS_A = """Tu analyses une frame extraite d'une vidéo de trading.
Timestamp de cette frame : [{ts}]
Transcription alignée (paroles prononcées autour de ce moment) :
\"\"\"{transcript}\"\"\"

Réponds UNIQUEMENT avec un objet JSON valide. Aucun texte avant ou après.
{{
  "timestamp": "{ts}",
  "est_setup_trading": false,
  "timeframe": "INCONNU",
  "indicateurs": [],
  "action_prix": "INCONNU",
  "signal": "INCONNU",
  "condition_entree": "INCONNU",
  "note": ""
}}

RÈGLES ABSOLUES :
- est_setup_trading = true SEULEMENT si un setup de trading réel est visible
- Toute valeur non visible ou non dite = "INCONNU"
- Ne pas inventer. Ne pas déduire. Seulement ce qui est visible ou dit.
- Les indicateurs sont une liste : [{{"nom": "EMA", "periode": 50, "couleur": "bleue"}}]
- NE PAS REMPLIR stop_loss / take_profit ici : ces valeurs seront extraites séparément."""

PROMPT_PASS_B = """Tu analyses la même frame que précédemment pour identifier
UNIQUEMENT les niveaux de Stop Loss (SL) et Take Profit (TP).
Timestamp : [{ts}]

Contexte identifié (Passe A) :
- Timeframe : {timeframe}
- Direction : {signal}
- Indicateurs : {indicators}

Sur cette base, identifie maintenant le Stop Loss et le Take Profit.

Mentions SL/TP repérées dans la transcription (par proximité ou globale) :
{transcript_mentions}

Regarde les lignes horizontales sur ce graphique. Lis le prix exact sur l'axe
droit pour chaque ligne. Identifie :
  - Stop Loss : au-dessus du prix actuel si VENTE, en-dessous si ACHAT
  - Take Profit : INVERSE du Stop Loss
Donne les valeurs numériques exactes. Si aucune ligne visible → réponds INCONNU.

Réponds UNIQUEMENT avec un objet JSON valide. Aucun texte avant ou après.
{{
  "stop_loss": "INCONNU",
  "take_profit": "INCONNU",
  "source_sl": "INCONNU",
  "source_tp": "INCONNU"
}}

RÈGLES :
- "source_sl" / "source_tp" = "AXE" si lu sur l'axe droit, "TRANSCRIPT" si déduit
  de la transcription, "INCONNU" sinon.
- Aucune invention. Si flou ou non lisible → INCONNU."""

PROMPT_HAS_LEVELS = """Regarde l'axe des prix (côté droit). Y a-t-il des chiffres
visibles sur cet axe ? Réponds UNIQUEMENT en JSON :
{"has_levels": true/false, "confidence": "high"|"low", "price_levels": []}"""

SL_KEYWORDS = [
    "stop", "stop loss", "sl", "risque", "risk", "invalidation",
    "above", "below", "au-dessus", "en-dessous", "above the high",
    "below the low", "swing high", "swing low", "above this",
    "below this", "protected", "invalidate", "failure", "wrong",
]
TP_KEYWORDS = [
    "target", "objectif", "take profit", "tp", "cible",
    "profit", "sortie", "exit", "niveau", "zone", "fair value gap",
    "fvg", "liquidity", "draw on liquidity", "first target",
    "second target", "partial", "scale out", "that's my target",
    "looking for", "expecting price",
]
_NUMBER_RE = re.compile(r"\d+[\.,]\d+")

# ── Prompt fusion finale (Phase 5) ─────────────────────────────────────────
PROMPT_FUSION = """Tu reçois les analyses de toutes les frames d'une vidéo de trading.
Titre : \"{title}\"

INSTRUCTIONS :
1. Garde SEULEMENT les frames où est_setup_trading = true
2. Fusionne les frames consécutives décrivant le MÊME setup (écart < 45 secondes)
3. Si aucun setup → réponds exactement : "# Aucun setup trading identifié dans cette vidéo."

FORMAT pour chaque setup (respecte exactement) :

---
### SETUP #{{N}} : {{nom_court_descriptif}} [Timestamp : {{HH:MM:SS}}]

#### 1. Contexte Visuel Détecté
- **Timeframe :** {{valeur ou INCONNU}}
- **Indicateurs Actifs :**
  - {{nom}} : Période {{periode}}, Couleur {{couleur}}
- **Action du Prix :** {{description précise}}

#### 2. Logique Algorithmique
```pseudo-code
// Condition de Tendance
Si (Price.Close {{opérateur}} {{indicateur}}) Alors Tendance = {{HAUSSIÈRE/BAISSIÈRE}};

// Condition de Déclenchement
Si ({{condition_entree}}) Alors
    Action = {{ACHAT/VENTE}};
FinSi
```

#### 3. Gestion du Risque
- **Stop Loss (SL) :** {{règle ou INCONNU}}
- **Take Profit (TP) :** {{règle ou INCONNU}}

---

Commence directement par SETUP #1. Aucune introduction. Aucune conclusion."""

# ── Prompt pré-screen (Phase 0) ────────────────────────────────────────────
PROMPT_PRESCREEN = """Tu vois 5 frames extraites des 3 premieres minutes d'une video de trading.

Transcription des 3 premieres minutes :
\"\"\"{transcript}\"\"\"

Contenus deja traites dans la KB (titres + extrait) :
{existing}

Decide si cette video doit etre analysee en entier.

Reponds UNIQUEMENT avec un objet JSON valide. Aucun texte avant ou apres.
{{
  "utile": false,
  "doublon": false,
  "raison": ""
}}

REGLES :
- utile = true SEULEMENT si la video enseigne du trading concret (setup, indicateur, methode, money management, gestion du risque). Sinon false.
- doublon = true si le sujet exact a deja ete traite dans la KB (meme indicateur + meme methode). Sinon false.
- raison : 1 phrase claire (max 150 caracteres)."""


# ── Utilitaires ─────────────────────────────────────────────────────────────

def get_duration(video_path: str) -> float:
    """Retourne la durée de la vidéo en secondes. Lève RuntimeError sur échec."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error",
             "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1",
             video_path],
            capture_output=True, text=True, encoding="utf-8",
            timeout=FFPROBE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"ffprobe timeout ({FFPROBE_TIMEOUT}s)")
    try:
        return float(result.stdout.strip())
    except ValueError as exc:
        stderr = (result.stderr or "")[:200].strip()
        raise RuntimeError(f"ffprobe duration parse failed : {stderr}") from exc


def sec_to_hms(sec: float) -> str:
    """Convertit des secondes en HH:MM:SS."""
    s = int(sec)
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def get_title(url: str) -> str:
    """Retourne le titre nettoyé de la vidéo. Fallback si timeout."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--remote-components", "ejs:github",
             "--get-title", "--no-playlist", url],
            capture_output=True, text=True,
            encoding="utf-8", errors="ignore",
            timeout=YTDLP_TITLE_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return "video_sans_titre"
    title = result.stdout.strip() or "video_sans_titre"
    for char in r'\/:*?"<>|':
        title = title.replace(char, "_")
    return title[:80]


# ── Phase 1 : Téléchargement ────────────────────────────────────────────────

def download_video(url: str, out_dir: str) -> str:
    """Télécharge la vidéo. Lève RuntimeError si échec ou fichier trop grand."""
    print("   📥 Téléchargement...")
    out_tmpl = os.path.join(out_dir, "video.%(ext)s")

    try:
        result = subprocess.run(
            ["yt-dlp", "--remote-components", "ejs:github",
             "-f", "best[height<=720][ext=mp4]/best[height<=720]/best",
             "--no-playlist", "-o", out_tmpl, url],
            capture_output=True, text=True,
            encoding="utf-8", errors="ignore",
            timeout=YTDLP_DOWNLOAD_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"yt-dlp download timeout ({YTDLP_DOWNLOAD_TIMEOUT}s)")

    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp échoué : {result.stderr[:150]}")

    for ext in [".mp4", ".webm", ".mkv", ".mov", ".avi"]:
        path = os.path.join(out_dir, f"video{ext}")
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            if size_mb > MAX_SIZE_MB:
                try:
                    os.unlink(path)
                except OSError:
                    pass
                raise RuntimeError(f"Vidéo trop grande ({size_mb:.0f}MB > {MAX_SIZE_MB}MB)")
            return path

    raise RuntimeError("Fichier vidéo introuvable après téléchargement")


# ── Phase 2 : Extraction keyframes ──────────────────────────────────────────

def extract_frames(video_path: str, out_dir: str) -> list[FrameInfo]:
    """
    Extrait des frames à intervalle régulier selon la durée. Pour chaque frame,
    extrait aussi 2 crops de l'axe droit (fallback en cas d'illisibilité) :
      Narrow : crop=in_w*0.15:in_h:in_w*0.85:0,scale=400:-1 → frame_XXXX_axis.jpg
      Wide   : crop=in_w*0.20:in_h:in_w*0.80:0,scale=600:-1 → frame_XXXX_axis_wide.jpg
    Retourne liste de {path, axis_path, axis_wide_path, ts_sec, ts_str}.
    """
    frames_dir = Path(out_dir) / "frames"
    frames_dir.mkdir(exist_ok=True)

    duration = get_duration(video_path)
    target   = min(MAX_FRAMES, 25)
    interval = max(5, int(duration / target))

    print(f"   🎬 Extraction frames (1 toutes les {interval}s sur {duration:.0f}s)...")

    # ── Passe 1 : frames principales ────────────────────────────────────────
    try:
        result = subprocess.run(
            ["ffmpeg", "-i", video_path,
             "-vf", f"fps=1/{interval},scale={RESOLUTION}:-1",
             "-q:v", "2",
             str(frames_dir / "frame_%04d.jpg")],
            capture_output=True, text=True,
            timeout=FFMPEG_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"ffmpeg extract_frames timeout ({FFMPEG_TIMEOUT}s)")
    if result.returncode != 0:
        stderr = (result.stderr or "")[-200:].strip() if result.stderr else ""
        raise RuntimeError(f"ffmpeg extract_frames échoué : {stderr}")

    # ── Passe 2 : crop axe droit narrow (15% de droite, 400px) ──────────────
    try:
        result_axis = subprocess.run(
            ["ffmpeg", "-i", video_path,
             "-vf", f"fps=1/{interval},crop=in_w*0.15:in_h:in_w*0.85:0,scale=400:-1",
             "-q:v", "2",
             str(frames_dir / "frame_%04d_axis.jpg")],
            capture_output=True, text=True,
            timeout=FFMPEG_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"ffmpeg extract_axis timeout ({FFMPEG_TIMEOUT}s)")
    if result_axis.returncode != 0:
        stderr = (result_axis.stderr or "")[-200:].strip() if result_axis.stderr else ""
        raise RuntimeError(f"ffmpeg extract_axis échoué : {stderr}")

    # ── Passe 3 : crop axe droit wide (20% de droite, 600px) ────────────────
    try:
        result_wide = subprocess.run(
            ["ffmpeg", "-i", video_path,
             "-vf", f"fps=1/{interval},crop=in_w*0.20:in_h:in_w*0.80:0,scale=600:-1",
             "-q:v", "2",
             str(frames_dir / "frame_%04d_axis_wide.jpg")],
            capture_output=True, text=True,
            timeout=FFMPEG_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"ffmpeg extract_axis_wide timeout ({FFMPEG_TIMEOUT}s)")
    if result_wide.returncode != 0:
        stderr = (result_wide.stderr or "")[-200:].strip() if result_wide.stderr else ""
        raise RuntimeError(f"ffmpeg extract_axis_wide échoué : {stderr}")

    # Filtre strict frame_NNNN.jpg (exclut tous les variants _axis* et _axis_wide*)
    _frame_re = re.compile(r"^frame_\d+$")
    frames = sorted(frames_dir.glob("frame_[0-9]*.jpg"))
    frames = [f for f in frames if _frame_re.match(f.stem)]
    result = []
    for i, f in enumerate(frames):
        ts_sec = float(i * interval)
        axis_file      = f.parent / f"{f.stem}_axis.jpg"
        axis_wide_file = f.parent / f"{f.stem}_axis_wide.jpg"
        result.append({
            "path": str(f),
            "axis_path":      str(axis_file)      if axis_file.exists()      else "",
            "axis_wide_path": str(axis_wide_file) if axis_wide_file.exists() else "",
            "ts_sec": ts_sec,
            "ts_str": sec_to_hms(ts_sec),
        })

    print(f"   ✅ {len(result)} frames extraites (+ axes narrow + wide)")
    return result


# ── Phase 3 : Transcription ──────────────────────────────────────────────────

def get_segments(url: str, out_dir: str) -> list[TranscriptSegment]:
    """
    Récupère la transcription avec fallback en 3 tentatives :
      1. Sous-titres natifs YouTube (fr,fr-FR,en,en-US)
      2. Sous-titres auto-générés YouTube (fr,en)
      3. Extraction audio + Whisper API (OpenAI)
    Retourne liste de {start, end, text} (en secondes).
    """
    segments = _try_native_subs(url, out_dir)
    if segments:
        print(f"   ✅ {len(segments)} segments (sous-titres natifs)")
        return segments

    # Anti-429 : pause avant tentative auto-générés (rate-limit YouTube)
    pause = random.uniform(4, 8)
    print(f"   ⏳ Pause anti-429 ({pause:.1f}s) avant tentative 2/3...")
    time.sleep(pause)

    segments = _try_auto_subs(url, out_dir)
    if segments:
        print(f"   ✅ {len(segments)} segments (sous-titres auto-générés)")
        return segments

    # Anti-429 : pause plus longue avant Whisper (charge réseau + audio upload)
    pause = random.uniform(6, 12)
    print(f"   ⏳ Pause anti-429 ({pause:.1f}s) avant tentative 3/3 Whisper...")
    time.sleep(pause)

    segments = _try_whisper(out_dir)
    if segments:
        print(f"   ✅ {len(segments)} segments (Whisper API)")
        return segments

    print("   ⚠️  Pas de transcription — analyse images uniquement")
    return []


def _parse_srt_files(out_dir: str, lang_priority: Optional[list[str]] = None) -> list[TranscriptSegment]:
    """
    Parse les sous-titres .srt OU .vtt selon une priorité de langues.
    yt-dlp génère subs_<base>.<lang>.srt — on choisit dans l'ordre lang_priority.
    Si pas de .srt (ex: convert-subs aborté à cause d'un 429 sur une autre lang),
    on parse les .vtt directement (même structure, séparateur décimal ',' ou '.').
    """
    if lang_priority is None:
        lang_priority = ["fr", "fr-FR", "en", "en-US"]

    # Priorité .srt (post-converted) puis .vtt (raw download)
    sub_files = list(Path(out_dir).glob("*.srt")) or list(Path(out_dir).glob("*.vtt"))
    if not sub_files:
        return []

    chosen = None
    for lang in lang_priority:
        for sub in sub_files:
            parts = sub.stem.split(".")
            if len(parts) >= 2 and parts[-1] == lang:
                chosen = sub
                break
        if chosen:
            break
    if chosen is None:
        chosen = sub_files[0]

    # Pattern compatible SRT (',') et VTT ('.') pour le séparateur décimal
    pattern = (
        r"(\d{2}):(\d{2}):(\d{2})[,.]\d+"
        r"\s*-->\s*"
        r"(\d{2}):(\d{2}):(\d{2})[,.]\d+"
        r"[^\n]*\n(.*?)(?=\n\n|\Z)"
    )
    segments: list[TranscriptSegment] = []
    with open(chosen, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for m in re.finditer(pattern, content, re.DOTALL):
        start = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        end   = int(m.group(4)) * 3600 + int(m.group(5)) * 60 + int(m.group(6))
        text  = re.sub(r"<[^>]+>", "", m.group(7)).strip().replace("\n", " ")
        if text:
            segments.append({"start": start, "end": end, "text": text})
    return segments


def _cleanup_srt(out_dir: str) -> None:
    """Supprime les .srt et .vtt résiduels avant une nouvelle tentative."""
    for pattern in ("*.srt", "*.vtt"):
        for sub in Path(out_dir).glob(pattern):
            try:
                sub.unlink()
            except OSError:
                pass


def _log_ytdlp_failure(label: str, result: subprocess.CompletedProcess) -> None:
    """Affiche un extrait de stderr de yt-dlp quand aucun .srt n'est produit."""
    stderr = (result.stderr or "").strip()
    if not stderr:
        print(f"      ↳ yt-dlp ({label}) : aucune erreur, aucun sous-titre produit")
        return
    relevant = [
        line.strip() for line in stderr.splitlines()
        if any(tag in line for tag in ("ERROR", "WARNING", "HTTP"))
    ]
    snippet = " | ".join(relevant[-3:]) if relevant else stderr[-300:]
    print(f"      ↳ yt-dlp ({label}) : {snippet[:300]}")


def _try_native_subs(url: str, out_dir: str) -> list[TranscriptSegment]:
    """Tentative 1 : sous-titres natifs YouTube."""
    print("   📝 Tentative 1/3 : sous-titres natifs...")
    _cleanup_srt(out_dir)
    srt_base = os.path.join(out_dir, "subs_native")
    result = subprocess.run(
        ["yt-dlp", "--remote-components", "ejs:github",
         "--write-sub", "--sub-lang", "fr,fr-FR,en,en-US",
         "--skip-download", "--convert-subs", "srt",
         "--no-playlist", "-o", srt_base, url],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore"
    )
    segments = _parse_srt_files(out_dir, ["fr", "fr-FR", "en", "en-US"])
    if not segments:
        _log_ytdlp_failure("natifs", result)
    return segments


def _try_auto_subs(url: str, out_dir: str) -> list[TranscriptSegment]:
    """Tentative 2 : sous-titres auto-générés YouTube."""
    print("   📝 Tentative 2/3 : sous-titres auto-générés...")
    _cleanup_srt(out_dir)
    srt_base = os.path.join(out_dir, "subs_auto")
    result = subprocess.run(
        ["yt-dlp", "--remote-components", "ejs:github",
         "--write-auto-sub", "--sub-lang", "fr,en",
         "--skip-download", "--convert-subs", "srt",
         "--no-playlist", "-o", srt_base, url],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore"
    )
    segments = _parse_srt_files(out_dir, ["fr", "en"])
    if not segments:
        _log_ytdlp_failure("auto-générés", result)
    return segments


def _try_whisper(out_dir: str) -> list[TranscriptSegment]:
    """Tentative 3 : extraction audio + transcription via Whisper API."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("   ⚠️  OPENAI_API_KEY non définie — fallback Whisper ignoré")
        return []

    video_path = None
    for stem in ("video", "preview"):
        for ext in (".mp4", ".webm", ".mkv", ".mov", ".avi"):
            candidate = os.path.join(out_dir, f"{stem}{ext}")
            if os.path.exists(candidate):
                video_path = candidate
                break
        if video_path:
            break

    if not video_path:
        print("   ⚠️  Vidéo introuvable dans out_dir pour extraction audio")
        return []

    print("   📝 Tentative 3/3 : extraction audio + Whisper API...")
    audio_path = os.path.join(out_dir, "audio.mp3")

    result = subprocess.run(
        ["ffmpeg", "-y", "-i", video_path, "-q:a", "0", "-map", "a", audio_path],
        capture_output=True, text=True
    )
    if not os.path.exists(audio_path):
        print(f"   ⚠️  Extraction audio échouée : {result.stderr[:120]}")
        return []

    # FIX 413 : si audio > 20MB, découper en chunks de 18MB
    try:
        audio_size = os.path.getsize(audio_path)
    except OSError:
        audio_size = 0
    try:
        if audio_size > 20_000_000:
            return _whisper_transcribe_chunked(audio_path, api_key)
        return _whisper_transcribe(audio_path, api_key)
    except Exception as exc:
        print(f"   ⚠️  Whisper API échouée : {exc}")
        return []


def _whisper_transcribe_chunked(audio_path: str, api_key: str) -> list[TranscriptSegment]:
    """
    Découpe audio_path en chunks de ~18MB via ffmpeg (segment muxer),
    transcrit chaque chunk via Whisper API, puis concatène les segments
    en ajustant les timestamps via offset cumulé (durée des chunks précédents).
    """
    audio_dir = os.path.dirname(audio_path)
    chunk_tmpl = os.path.join(audio_dir, "chunk_%03d.mp3")

    size_mb = os.path.getsize(audio_path) / (1024 * 1024)
    print(f"   ✂️  Audio {size_mb:.1f}MB > 20MB — découpage en chunks 18MB...")

    try:
        result = subprocess.run(
            ["ffmpeg", "-y", "-i", audio_path,
             "-f", "segment", "-segment_size", "18000000",
             "-c", "copy", chunk_tmpl],
            capture_output=True, text=True,
            timeout=FFMPEG_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"ffmpeg chunking timeout ({FFMPEG_TIMEOUT}s)")
    if result.returncode != 0:
        stderr = (result.stderr or "")[-200:].strip()
        raise RuntimeError(f"ffmpeg chunking échoué : {stderr}")

    chunks = sorted(Path(audio_dir).glob("chunk_*.mp3"))
    if not chunks:
        raise RuntimeError("ffmpeg chunking : aucun chunk produit")

    print(f"   ✂️  {len(chunks)} chunks à transcrire")

    all_segments: list[TranscriptSegment] = []
    offset = 0.0
    for i, chunk in enumerate(chunks, 1):
        chunk_str = str(chunk)
        try:
            chunk_duration = get_duration(chunk_str)
        except RuntimeError:
            chunk_duration = 0.0

        print(f"   📝 Chunk {i}/{len(chunks)} ({chunk_duration:.0f}s) → Whisper...")
        chunk_segments = _whisper_transcribe(chunk_str, api_key)

        # Offset des timestamps par durée cumulée des chunks précédents
        for seg in chunk_segments:
            seg["start"] = int(seg["start"] + offset)
            seg["end"]   = int(seg["end"]   + offset)
        all_segments.extend(chunk_segments)

        offset += chunk_duration

    return all_segments


def _whisper_transcribe(audio_path: str, api_key: str) -> list[TranscriptSegment]:
    """Envoie audio_path à l'API Whisper et retourne les segments timestampés."""
    with open(audio_path, "rb") as f:
        audio_data = f.read()

    boundary = "----WhisperBoundary" + os.urandom(12).hex()

    def _field(name: str, value: str) -> bytes:
        return (
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
            f"{value}\r\n"
        ).encode("utf-8")

    parts = [
        _field("model", "whisper-1"),
        _field("response_format", "verbose_json"),
        _field("timestamp_granularities[]", "segment"),
        (
            f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="file"; filename="audio.mp3"\r\n'
            "Content-Type: audio/mpeg\r\n\r\n"
        ).encode("utf-8"),
        audio_data,
        b"\r\n",
        f"--{boundary}--\r\n".encode("utf-8"),
    ]
    body = b"".join(parts)

    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
    )

    with urllib.request.urlopen(req, timeout=600) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    segments = []
    for s in result.get("segments", []):
        text = (s.get("text") or "").strip()
        if not text:
            continue
        segments.append({
            "start": int(s.get("start", 0)),
            "end":   int(s.get("end", 0)),
            "text":  text,
        })
    return segments


def get_window(segments: list[TranscriptSegment], ts_sec: float) -> str:
    """Retourne le texte prononcé dans [ts_sec - BEFORE, ts_sec + AFTER]."""
    w_start = ts_sec - WINDOW_BEFORE
    w_end   = ts_sec + WINDOW_AFTER
    texts   = [
        s["text"] for s in segments
        if s["end"] >= w_start and s["start"] <= w_end
    ]
    return " ".join(texts) if texts else "[Pas de transcription pour cette frame]"


# ── Phase 4 : Appels Claude ciblés ──────────────────────────────────────────

def b64_image(path: str) -> str:
    """Encode une image en base64."""
    with open(path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def call_api(api_key: str, payload: dict) -> str:
    """
    Appel à l'API Claude avec retry exponentiel sur 429 / 5xx / erreurs réseau.
    Lève RuntimeError après API_MAX_RETRIES échecs.
    """
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }

    last_error = "unknown"
    for attempt in range(API_MAX_RETRIES):
        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=data,
            headers=headers,
        )
        try:
            with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            return result["content"][0]["text"]

        except urllib.error.HTTPError as e:
            # Pas de body dans l'erreur : peut contenir request_id / rate-limit
            last_error = f"HTTP {e.code}"
            if e.code in (429, 500, 502, 503, 504) and attempt < API_MAX_RETRIES - 1:
                wait = 2 ** attempt
                logger.warning("API %s retry %d/%d after %ds", last_error, attempt + 1, API_MAX_RETRIES, wait)
                print(f"      ⏳ API {last_error} — retry dans {wait}s ({attempt + 1}/{API_MAX_RETRIES})")
                time.sleep(wait)
                continue
            logger.error("API failed permanently: %s", last_error)
            raise RuntimeError(f"API {last_error}")

        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last_error = type(e).__name__
            if attempt < API_MAX_RETRIES - 1:
                wait = 2 ** attempt
                logger.warning("API network %s retry %d/%d after %ds", last_error, attempt + 1, API_MAX_RETRIES, wait)
                print(f"      ⏳ API network {last_error} — retry dans {wait}s ({attempt + 1}/{API_MAX_RETRIES})")
                time.sleep(wait)
                continue
            logger.error("API network failed permanently: %s", last_error)
            raise RuntimeError(f"API network : {last_error}")

    logger.error("API max retries exceeded: %s", last_error)
    raise RuntimeError(f"API max retries dépassés : {last_error}")


def _check_axis_levels(api_key: str, axis_path: str) -> bool:
    """
    Appel API léger sur UN seul crop axe. Bénéfice du doute :
    True si has_levels=True OU confidence='low' (image potentiellement floue).
    """
    if not axis_path or not os.path.exists(axis_path):
        return False
    payload = {
        "model": MODEL,
        "max_tokens": 150,
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": b64_image(axis_path),
                    },
                },
                {"type": "text", "text": PROMPT_HAS_LEVELS},
            ],
        }],
    }
    try:
        raw = call_api(api_key, payload)
    except RuntimeError:
        return False
    raw = re.sub(r"```json|```", "", raw).strip()
    try:
        verdict = json.loads(raw)
    except json.JSONDecodeError:
        return False
    if verdict.get("has_levels", False):
        return True
    # Bénéfice du doute : low confidence => on suppose qu'il y a des niveaux
    if verdict.get("confidence") == "low":
        return True
    return False


def has_price_levels(
    api_key: str,
    axis_path: str,
    axis_wide_path: str = "",
) -> bool:
    """
    Détecteur léger SL/TP : tente d'abord le crop narrow (axis_path), puis
    fallback vers le crop wide (axis_wide_path) si le premier échoue.
    Retourne True si l'un des deux retourne True (avec bénéfice du doute sur
    confidence='low'). Retourne False uniquement si les deux échouent.
    """
    if _check_axis_levels(api_key, axis_path):
        return True
    if axis_wide_path and _check_axis_levels(api_key, axis_wide_path):
        return True
    return False


def _pick_best_axis(
    api_key: str,
    frame: FrameInfo,
) -> str:
    """
    Choisit le meilleur crop axe à attacher en Passe B :
      narrow d'abord, wide en fallback. Retourne "" si aucun ne fonctionne.
    """
    axis_n = frame.get("axis_path", "")
    axis_w = frame.get("axis_wide_path", "")
    if axis_n and _check_axis_levels(api_key, axis_n):
        return axis_n
    if axis_w and _check_axis_levels(api_key, axis_w):
        return axis_w
    return ""


def find_sltp_in_transcript(
    segments: list[TranscriptSegment],
    frame_ts: Optional[float],
) -> list[dict]:
    """
    Recherche SL/TP dans toute la transcription. Garde seulement les segments
    contenant : keyword SL/TP + nombre décimal.

    Modes :
      - frame_ts is None  → recherche GLOBALE : tri par densité de keywords,
                            top 5 marqués {"global_search": True}.
      - frame_ts is float → tri par proximité temporelle, top 5. Si vide →
                            fallback automatique en recherche globale.
    Chaque résultat : {"ts": int, "text": str, "type": "SL"|"TP"|"BOTH"}.
    """
    if not segments:
        return []

    all_keywords = SL_KEYWORDS + TP_KEYWORDS
    hits = []
    for s in segments:
        text_low = s["text"].lower()
        if not _NUMBER_RE.search(s["text"]):
            continue
        has_sl = any(k in text_low for k in SL_KEYWORDS)
        has_tp = any(k in text_low for k in TP_KEYWORDS)
        if not (has_sl or has_tp):
            continue
        kind = "BOTH" if (has_sl and has_tp) else ("SL" if has_sl else "TP")
        kw_score = sum(1 for k in all_keywords if k in text_low)
        hits.append({
            "ts": int(s["start"]),
            "text": s["text"][:200],
            "type": kind,
            "_dist": (abs(s["start"] - frame_ts)
                      if frame_ts is not None else 0),
            "_score": kw_score,
        })

    if not hits:
        return []

    # Recherche globale forcée : tri par densité de keywords (score décroissant)
    if frame_ts is None:
        hits.sort(key=lambda h: -h["_score"])
        top = hits[:5]
        for h in top:
            h["global_search"] = True
            h.pop("_dist", None)
            h.pop("_score", None)
        return top

    # Recherche temporelle : tri par proximité, top 5
    hits.sort(key=lambda h: h["_dist"])
    top = hits[:5]
    for h in top:
        h.pop("_dist", None)
        h.pop("_score", None)

    # Fallback global automatique si rien à proximité
    if not top:
        return find_sltp_in_transcript(segments, frame_ts=None)
    return top


def _format_sltp_mentions(mentions: list[dict]) -> str:
    """Formate les mentions SL/TP pour injection dans le prompt Passe B."""
    if not mentions:
        return "(aucune mention SL/TP trouvée dans la transcription)"
    lines = []
    for m in mentions:
        ts_str = sec_to_hms(m["ts"])
        lines.append(f"- [{ts_str}] ({m['type']}) : {m['text']}")
    return "\n".join(lines)


def _run_pass_b(
    api_key: str,
    frame: FrameInfo,
    result_a: dict,
    segments: Optional[list[TranscriptSegment]],
    force_global_search: bool = False,
) -> dict:
    """
    Exécute Passe B (SL/TP) avec :
      - contexte Passe A injecté dans le prompt (timeframe / direction / indicateurs)
      - mentions SL/TP de la transcription (proximité ou globale)
      - meilleur crop axe attaché (narrow d'abord, wide fallback)
    Retourne {} en cas d'erreur API ou JSON invalide.
    """
    ts = frame["ts_str"]

    if force_global_search:
        mentions = find_sltp_in_transcript(segments or [], frame_ts=None)
    else:
        mentions = find_sltp_in_transcript(segments or [], frame["ts_sec"])
    mentions_str = _format_sltp_mentions(mentions)

    indicators_list = result_a.get("indicateurs", []) or []
    indicators_str = ", ".join(
        i.get("nom", "?") for i in indicators_list if isinstance(i, dict)
    ) or "(aucun)"

    prompt_b = (PROMPT_PASS_B
                .replace("{ts}", ts)
                .replace("{timeframe}", str(result_a.get("timeframe", "INCONNU")))
                .replace("{signal}", str(result_a.get("signal", "INCONNU")))
                .replace("{indicators}", indicators_str)
                .replace("{transcript_mentions}", mentions_str))

    # Détection axis : narrow d'abord, wide fallback. Attache celui qui marche.
    best_axis = _pick_best_axis(api_key, frame)

    content_b = [
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": b64_image(frame["path"]),
            },
        },
    ]
    if best_axis:
        content_b.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": b64_image(best_axis),
            },
        })
    content_b.append({"type": "text", "text": prompt_b})

    payload_b = {
        "model": MODEL,
        "max_tokens": 200,
        "messages": [{"role": "user", "content": content_b}],
    }
    try:
        raw_b = call_api(api_key, payload_b)
    except RuntimeError:
        return {}
    raw_b = re.sub(r"```json|```", "", raw_b).strip()
    try:
        return json.loads(raw_b)
    except json.JSONDecodeError:
        return {}


def analyze_frame(
    api_key: str,
    frame: FrameInfo,
    window: str,
    segments: Optional[list[TranscriptSegment]] = None,
) -> dict:
    """
    Phase 4 : analyse une frame en 2 passes séquentielles.
      Passe A : contexte global (timeframe, indicateurs, signal) max_tokens=400
      Passe B : SL/TP focalisée — TOUJOURS exécutée (avec contexte Passe A injecté
                et meilleur crop axe attaché si lisible) max_tokens=200
    Les résultats sont fusionnés en un seul JSON final.
    """
    ts = frame["ts_str"]

    # ── PASSE A : contexte global (image complète seule) ────────────────────
    prompt_a = (PROMPT_PASS_A
                .replace("{ts}", ts)
                .replace("{transcript}", window[:600]))
    payload_a = {
        "model": MODEL,
        "max_tokens": 400,
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": b64_image(frame["path"]),
                    },
                },
                {"type": "text", "text": prompt_a},
            ],
        }],
    }
    raw_a = call_api(api_key, payload_a)
    raw_a = re.sub(r"```json|```", "", raw_a).strip()
    try:
        result_a = json.loads(raw_a)
    except json.JSONDecodeError:
        return {
            "timestamp": ts,
            "est_setup_trading": False,
            "stop_loss": "INCONNU",
            "take_profit": "INCONNU",
            "note": f"passe A : JSON invalide ({raw_a[:80]})",
        }

    # Valeurs par défaut SL/TP
    result_a.setdefault("stop_loss", "INCONNU")
    result_a.setdefault("take_profit", "INCONNU")
    result_a.setdefault("source_sl", "INCONNU")
    result_a.setdefault("source_tp", "INCONNU")

    # ── PASSE B : SL/TP — TOUJOURS exécutée (Phase 2 spec) ──────────────────
    result_b = _run_pass_b(api_key, frame, result_a, segments, force_global_search=False)

    # Fusion : Passe B écrase SL/TP si valeurs non vides
    for key in ("stop_loss", "take_profit", "source_sl", "source_tp"):
        if key in result_b and result_b[key]:
            result_a[key] = result_b[key]

    return result_a


# ── Phase 5 : Fusion ────────────────────────────────────────────────────────

def merge_analyses(api_key: str, analyses: list[dict], title: str) -> str:
    """Phase 5 : fusionne toutes les analyses et génère le guide .md."""
    setups = [a for a in analyses if a.get("est_setup_trading")]
    if not setups:
        return "# Aucun setup trading identifié dans cette vidéo.\n"

    prompt  = PROMPT_FUSION.replace("{title}", title)
    content = (
        f"Titre vidéo : {title}\n\n"
        f"Analyses ({len(setups)} frames avec setup) :\n"
        f"{json.dumps(setups, indent=2, ensure_ascii=False)}"
        f"\n\n{prompt}"
    )
    payload = {
        "model": MODEL,
        "max_tokens": 4000,
        "messages": [{"role": "user", "content": content}],
    }
    return call_api(api_key, payload)


# ── Sauvegarde ──────────────────────────────────────────────────────────────

def save_md(content: str, title: str, channel_name: str, url: str) -> str:
    """
    Sauvegarde le fichier .md.
    Nom fichier = titre de la vidéo (format A).
    Chemin = 07-nouvelles sources\[channel_name]\titre.md
    """
    safe_title   = re.sub(r'[\\/:*?"<>|]', "_", title)
    safe_title   = re.sub(r"\s+", "_", safe_title).strip("_")
    safe_channel = re.sub(r'[\\/:*?"<>|]', "_", channel_name).strip()

    out_dir = Path(OUTPUT_BASE) / safe_channel
    out_dir.mkdir(parents=True, exist_ok=True)

    filepath = out_dir / f"{safe_title}.md"
    header = (
        f"# {title}\n\n"
        f"> **Chaîne :** {channel_name}  \n"
        f"> **Source :** {url}  \n"
        f"> **Généré le :** {datetime.now().strftime('%d/%m/%Y à %H:%M')}  \n"
        f"> **Pipeline :** TRANSVIDEO Chunk&Fuse | TRADEX-AI\n\n---\n\n"
    )

    # Écriture atomique : tempfile dans le même dir puis os.replace (CLAUDE.md)
    payload = header + content
    tmp_path = str(filepath) + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(payload)
        os.replace(tmp_path, str(filepath))
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Mise à jour du cache KB pour les pre-screens suivants (P1.5)
    if _EXISTING_KB_CACHE is not None:
        snippet = re.sub(r"\s+", " ", payload).strip()[:300]
        _EXISTING_KB_CACHE.append({"title": title, "snippet": snippet})

    return str(filepath)


# ── Phase 0 : Pré-screen ────────────────────────────────────────────────────

def list_existing_content(refresh: bool = False) -> list[dict]:
    """
    Liste les .md deja generes dans 07-nouvelles sources (titre + extrait court).
    Cache module-level pour éviter I/O répété sur la KB à chaque pre-screen.
    refresh=True force la relecture disque.
    """
    global _EXISTING_KB_CACHE
    if not refresh and _EXISTING_KB_CACHE is not None:
        return _EXISTING_KB_CACHE

    base = Path(OUTPUT_BASE)
    if not base.exists():
        _EXISTING_KB_CACHE = []
        return _EXISTING_KB_CACHE

    items = []
    for md_file in base.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read(2000)
        except OSError:
            continue
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else md_file.stem
        snippet = re.sub(r"\s+", " ", content).strip()[:300]
        items.append({"title": title, "snippet": snippet})

    _EXISTING_KB_CACHE = items
    return _EXISTING_KB_CACHE


def pre_screen_video(url: str, api_key: str) -> dict[str, object]:
    """
    Pré-screen rapide avant pipeline complet.
    Télécharge les 3 premières minutes, extrait 5 frames, demande à Claude :
      - utile   : la vidéo enseigne-t-elle du trading concret ?
      - doublon : sujet déjà traité dans la KB ?
    En cas d'erreur technique, retourne utile=True pour ne pas bloquer.

    Returns:
        {"utile": bool, "doublon": bool, "raison": str}
    """
    tmp_dir = tempfile.mkdtemp(prefix="tradex_prescreen_")
    try:
        # 3 premières minutes uniquement
        out_tmpl = os.path.join(tmp_dir, "preview.%(ext)s")
        try:
            result = subprocess.run(
                ["yt-dlp", "--remote-components", "ejs:github",
                 "-f", "best[height<=480][ext=mp4]/best[height<=480]/best",
                 "--download-sections", "*0-180",
                 "--force-keyframes-at-cuts",
                 "--no-playlist", "-o", out_tmpl, url],
                capture_output=True, text=True,
                encoding="utf-8", errors="ignore",
                timeout=YTDLP_PREVIEW_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            return {"utile": True, "doublon": False,
                    "raison": f"pre-screen : timeout {YTDLP_PREVIEW_TIMEOUT}s, on tente la video"}
        if result.returncode != 0:
            return {"utile": True, "doublon": False,
                    "raison": "pre-screen : telechargement echoue, on tente la video"}

        video_path = None
        for ext in [".mp4", ".webm", ".mkv", ".mov", ".avi"]:
            path = os.path.join(tmp_dir, f"preview{ext}")
            if os.path.exists(path):
                video_path = path
                break
        if not video_path:
            return {"utile": True, "doublon": False,
                    "raison": "pre-screen : fichier preview introuvable, on tente la video"}

        # 5 frames réparties sur la preview
        frames_dir = Path(tmp_dir) / "frames"
        frames_dir.mkdir(exist_ok=True)
        duration = get_duration(video_path)
        interval = max(10, int(duration / 5))
        try:
            subprocess.run(
                ["ffmpeg", "-i", video_path,
                 "-vf", f"fps=1/{interval},scale={RESOLUTION}:-1",
                 "-q:v", "2",
                 "-frames:v", "5",
                 str(frames_dir / "frame_%02d.jpg")],
                capture_output=True, text=True,
                timeout=60,
            )
        except subprocess.TimeoutExpired:
            return {"utile": True, "doublon": False,
                    "raison": "pre-screen : ffmpeg preview timeout, on tente la video"}
        frames = sorted(frames_dir.glob("frame_*.jpg"))[:5]
        if not frames:
            return {"utile": True, "doublon": False,
                    "raison": "pre-screen : aucune frame extraite, on tente la video"}

        # Transcription courte des 3 premières minutes
        segments = get_segments(url, tmp_dir)
        short_transcript = " ".join(
            s["text"] for s in segments if s["start"] < 180
        )[:1500] or "[Pas de transcription]"

        # Contenus déjà traités
        existing = list_existing_content()
        if existing:
            existing_text = "\n".join(
                f"- {item['title']} :: {item['snippet']}" for item in existing
            )[:4000]
        else:
            existing_text = "(aucun contenu deja traite)"

        # Appel Claude : frames + transcription + KB
        content_blocks = []
        for f in frames:
            content_blocks.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": b64_image(str(f)),
                },
            })
        prompt = (PROMPT_PRESCREEN
                  .replace("{transcript}", short_transcript)
                  .replace("{existing}", existing_text))
        content_blocks.append({"type": "text", "text": prompt})

        payload = {
            "model": MODEL,
            "max_tokens": 400,
            "messages": [{"role": "user", "content": content_blocks}],
        }
        raw = call_api(api_key, payload)
        raw = re.sub(r"```json|```", "", raw).strip()
        try:
            verdict = json.loads(raw)
        except json.JSONDecodeError:
            return {"utile": True, "doublon": False,
                    "raison": f"pre-screen : JSON invalide ({raw[:80]}), on tente la video"}

        return {
            "utile":   bool(verdict.get("utile", False)),
            "doublon": bool(verdict.get("doublon", False)),
            "raison":  str(verdict.get("raison", ""))[:200],
        }

    except Exception as exc:
        return {"utile": True, "doublon": False,
                "raison": f"pre-screen : {type(exc).__name__} ({exc}), on tente la video"}
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


# ── Fonction principale ──────────────────────────────────────────────────────

def process_video(url: str, channel_name: str, api_key: str) -> Optional[str]:
    """
    Pipeline complet pour une vidéo.
    Retourne le chemin du .md généré, None si erreur ou pré-screen négatif.
    """
    print(f"\n   🎯 {url[:65]}")

    title = get_title(url)
    print(f"   📌 {title}")

    # Pré-screen avant pipeline complet
    print("   🔍 Pré-screen (3min + 5 frames + dedup KB)...")
    verdict = pre_screen_video(url, api_key)
    if not verdict["utile"] or verdict["doublon"]:
        flag = "doublon" if verdict["doublon"] else "non utile"
        print(f"   ⏭️  Ignorée ({flag}) : {verdict['raison']}")
        return None
    print(f"   ✅ Pré-screen OK : {verdict['raison']}")

    tmp_dir = tempfile.mkdtemp(prefix="tradex_cf_")
    try:
        video_path = download_video(url, tmp_dir)
        frames     = extract_frames(video_path, tmp_dir)

        if not frames:
            raise RuntimeError("Aucune frame extraite")

        segments = get_segments(url, tmp_dir)

        print(f"   🤖 Analyse {len(frames)} frames...")
        analyses = []
        for i, frame in enumerate(frames, 1):
            window   = get_window(segments, frame["ts_sec"])
            analysis = analyze_frame(api_key, frame, window, segments)
            mark     = "✅" if analysis.get("est_setup_trading") else "·"
            print(f"      {mark} [{frame['ts_str']}] ({i}/{len(frames)})", end="\r")
            analyses.append(analysis)

        found = sum(1 for a in analyses if a.get("est_setup_trading"))
        print(f"\n   📊 {found}/{len(frames)} frames avec setup")

        # ── Phase 4 : retry SL/TP INCONNU avec recherche globale forcée ─────
        # Pré-calcul : si la transcription ne contient AUCUNE mention SL/TP
        # globale, inutile de relancer Passe B — on garde "INCONNU".
        global_mentions = find_sltp_in_transcript(segments, frame_ts=None)
        if global_mentions:
            retry_count = 0
            for i, analysis in enumerate(analyses):
                sl = analysis.get("stop_loss", "INCONNU")
                tp = analysis.get("take_profit", "INCONNU")
                if sl != "INCONNU" and tp != "INCONNU":
                    continue
                retry = _run_pass_b(
                    api_key, frames[i], analysis, segments,
                    force_global_search=True,
                )
                if not retry:
                    continue
                new_sl = retry.get("stop_loss", "INCONNU")
                new_tp = retry.get("take_profit", "INCONNU")
                if sl == "INCONNU" and new_sl != "INCONNU":
                    analyses[i]["stop_loss"] = new_sl
                    analyses[i]["source_sl"] = retry.get("source_sl", "TRANSCRIPT")
                    retry_count += 1
                if tp == "INCONNU" and new_tp != "INCONNU":
                    analyses[i]["take_profit"] = new_tp
                    analyses[i]["source_tp"] = retry.get("source_tp", "TRANSCRIPT")
                    retry_count += 1
            if retry_count:
                print(f"   🔁 Retry SL/TP : {retry_count} valeur(s) récupérée(s)")

        print("   🔀 Génération guide technique...")
        specs_md  = merge_analyses(api_key, analyses, title)
        out_path  = save_md(specs_md, title, channel_name, url)

        print(f"   ✅ {out_path}")
        return out_path

    except Exception as exc:
        logger.error("process_video failed for %s: %s", url, exc, exc_info=True)
        print(f"   ❌ Erreur ({type(exc).__name__}) : {exc}")
        traceback.print_exc(limit=3)
        return None
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
