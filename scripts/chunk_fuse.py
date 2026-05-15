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
import base64
import subprocess
import tempfile
import shutil
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

# ── Configuration ──────────────────────────────────────────────────────────
OUTPUT_BASE    = r"C:\trading-copilote\07-nouvelles sources"
MAX_FRAMES     = 28            # Frames max par vidéo
RESOLUTION     = 800           # Largeur en pixels
MODEL          = "claude-opus-4-6"
MAX_SIZE_MB    = 500           # Guardrail taille vidéo
WINDOW_BEFORE  = 5             # Secondes avant la frame
WINDOW_AFTER   = 20            # Secondes après la frame
API_TIMEOUT    = 60            # Timeout appel API (secondes)

# ── Prompt analyse pairée (Phase 4) ────────────────────────────────────────
PROMPT_PAIR = """Tu analyses une frame extraite d'une vidéo de trading.
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
  "stop_loss": "INCONNU",
  "take_profit": "INCONNU",
  "note": ""
}}

RÈGLES ABSOLUES :
- est_setup_trading = true SEULEMENT si un setup de trading réel est visible
- Toute valeur non visible ou non dite = "INCONNU"
- Ne pas inventer. Ne pas déduire. Seulement ce qui est visible ou dit.
- Les indicateurs sont une liste : [{{"nom": "EMA", "periode": 50, "couleur": "bleue"}}]"""

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


# ── Utilitaires ─────────────────────────────────────────────────────────────

def get_duration(video_path: str) -> float:
    """Retourne la durée de la vidéo en secondes."""
    result = subprocess.run(
        ["ffprobe", "-v", "error",
         "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1",
         video_path],
        capture_output=True, text=True, encoding="utf-8"
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 600.0


def sec_to_hms(sec: float) -> str:
    """Convertit des secondes en HH:MM:SS."""
    s = int(sec)
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def get_title(url: str) -> str:
    """Retourne le titre nettoyé de la vidéo."""
    result = subprocess.run(
        ["yt-dlp", "--get-title", "--no-playlist", url],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore"
    )
    title = result.stdout.strip() or "video_sans_titre"
    for char in r'\/:*?"<>|':
        title = title.replace(char, "_")
    return title[:80]


# ── Phase 1 : Téléchargement ────────────────────────────────────────────────

def download_video(url: str, out_dir: str) -> str:
    """Télécharge la vidéo. Lève RuntimeError si échec ou fichier trop grand."""
    print("   📥 Téléchargement...")
    out_tmpl = os.path.join(out_dir, "video.%(ext)s")

    result = subprocess.run(
        ["yt-dlp",
         "-f", "best[height<=720][ext=mp4]/best[height<=720]/best",
         "--no-playlist", "-o", out_tmpl, url],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore"
    )
    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp échoué : {result.stderr[:150]}")

    for ext in [".mp4", ".webm", ".mkv", ".mov", ".avi"]:
        path = os.path.join(out_dir, f"video{ext}")
        if os.path.exists(path):
            size_mb = os.path.getsize(path) / (1024 * 1024)
            if size_mb > MAX_SIZE_MB:
                raise RuntimeError(f"Vidéo trop grande ({size_mb:.0f}MB > {MAX_SIZE_MB}MB)")
            return path

    raise RuntimeError("Fichier vidéo introuvable après téléchargement")


# ── Phase 2 : Extraction keyframes ──────────────────────────────────────────

def extract_frames(video_path: str, out_dir: str) -> list:
    """
    Extrait des frames à intervalle régulier selon la durée.
    Retourne liste de {path, ts_sec, ts_str}.
    """
    frames_dir = Path(out_dir) / "frames"
    frames_dir.mkdir(exist_ok=True)

    duration = get_duration(video_path)
    target   = min(MAX_FRAMES, 25)
    interval = max(5, int(duration / target))

    print(f"   🎬 Extraction frames (1 toutes les {interval}s sur {duration:.0f}s)...")

    subprocess.run(
        ["ffmpeg", "-i", video_path,
         "-vf", f"fps=1/{interval},scale={RESOLUTION}:-1",
         "-q:v", "2",
         str(frames_dir / "frame_%04d.jpg")],
        capture_output=True, text=True
    )

    frames = sorted(frames_dir.glob("frame_*.jpg"))
    result = []
    for i, f in enumerate(frames):
        ts_sec = float(i * interval)
        result.append({
            "path": str(f),
            "ts_sec": ts_sec,
            "ts_str": sec_to_hms(ts_sec),
        })

    print(f"   ✅ {len(result)} frames extraites")
    return result


# ── Phase 3 : Transcription ──────────────────────────────────────────────────

def get_segments(url: str, out_dir: str) -> list:
    """
    Récupère la transcription SRT avec timestamps.
    Retourne liste de {start, end, text} (en secondes).
    """
    print("   📝 Récupération transcription SRT...")
    srt_base = os.path.join(out_dir, "subs")

    subprocess.run(
        ["yt-dlp",
         "--write-auto-sub", "--sub-lang", "fr,fr-FR,en,en-US",
         "--skip-download", "--convert-subs", "srt",
         "--no-playlist", "-o", srt_base, url],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore"
    )

    segments = []
    pattern = (
        r"(\d{2}):(\d{2}):(\d{2}),\d+"
        r"\s*-->\s*"
        r"(\d{2}):(\d{2}):(\d{2}),\d+"
        r"\s*\n(.*?)(?=\n\n|\Z)"
    )

    for srt_file in Path(out_dir).glob("*.srt"):
        with open(srt_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        for m in re.finditer(pattern, content, re.DOTALL):
            start = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
            end   = int(m.group(4)) * 3600 + int(m.group(5)) * 60 + int(m.group(6))
            text  = re.sub(r"<[^>]+>", "", m.group(7)).strip().replace("\n", " ")
            if text:
                segments.append({"start": start, "end": end, "text": text})
        break  # Premier fichier SRT suffit

    if segments:
        print(f"   ✅ {len(segments)} segments de transcription")
    else:
        print("   ⚠️  Pas de transcription — analyse images uniquement")

    return segments


def get_window(segments: list, ts_sec: float) -> str:
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
    """Appel à l'API Claude. Lève RuntimeError si échec."""
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req  = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        return result["content"][0]["text"]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"API HTTP {e.code} : {body[:200]}")


def analyze_frame(api_key: str, frame: dict, window: str) -> dict:
    """Phase 4 : analyse une frame + sa fenêtre de transcription."""
    ts     = frame["ts_str"]
    prompt = (PROMPT_PAIR
              .replace("{ts}", ts)
              .replace("{transcript}", window[:600]))

    payload = {
        "model": MODEL,
        "max_tokens": 600,
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
                {"type": "text", "text": prompt},
            ],
        }],
    }

    raw = call_api(api_key, payload)
    raw = re.sub(r"```json|```", "", raw).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "timestamp": ts,
            "est_setup_trading": False,
            "note": f"erreur parsing JSON : {raw[:100]}",
        }


# ── Phase 5 : Fusion ────────────────────────────────────────────────────────

def merge_analyses(api_key: str, analyses: list, title: str) -> str:
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
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + content)

    return str(filepath)


# ── Fonction principale ──────────────────────────────────────────────────────

def process_video(url: str, channel_name: str, api_key: str):
    """
    Pipeline complet pour une vidéo.
    Retourne le chemin du .md généré, ou None si erreur.
    """
    tmp_dir = tempfile.mkdtemp(prefix="tradex_cf_")
    try:
        print(f"\n   🎯 {url[:65]}")

        title = get_title(url)
        print(f"   📌 {title}")

        video_path = download_video(url, tmp_dir)
        frames     = extract_frames(video_path, tmp_dir)

        if not frames:
            raise RuntimeError("Aucune frame extraite")

        segments = get_segments(url, tmp_dir)

        print(f"   🤖 Analyse {len(frames)} frames...")
        analyses = []
        for i, frame in enumerate(frames, 1):
            window   = get_window(segments, frame["ts_sec"])
            analysis = analyze_frame(api_key, frame, window)
            mark     = "✅" if analysis.get("est_setup_trading") else "·"
            print(f"      {mark} [{frame['ts_str']}] ({i}/{len(frames)})", end="\r")
            analyses.append(analysis)

        found = sum(1 for a in analyses if a.get("est_setup_trading"))
        print(f"\n   📊 {found}/{len(frames)} frames avec setup")

        print("   🔀 Génération guide technique...")
        specs_md  = merge_analyses(api_key, analyses, title)
        out_path  = save_md(specs_md, title, channel_name, url)

        print(f"   ✅ {out_path}")
        return out_path

    except Exception as exc:
        print(f"   ❌ Erreur : {exc}")
        return None
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
