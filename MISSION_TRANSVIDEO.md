# MISSION : TRANSVIDEO PIPELINE — YouTube → Spécifications Trading
> **Pour Claude Code** — Exécute dans l'ordre exact. Ne saute aucune phase.

---

## ÉTAPE 0 — LIS CES FICHIERS EN PREMIER (obligatoire)

```
view C:\trading-copilote\CLAUDE.md
view C:\trading-copilote\scripts\disable-sleep.ps1
```

Raison : caler le style, encoding, conventions du projet avant d'écrire quoi que ce soit.

---

## Contexte vérifié

| Info | Valeur confirmée |
|------|-----------------|
| Racine projet | `C:\trading-copilote\` |
| Dossier scripts | `C:\trading-copilote\scripts\` |
| Fichiers existants dans scripts\ | `disable-sleep.ps1`, `restore-sleep.ps1` uniquement |
| Risque écrasement | **AUCUN** — pas de Python existant |
| Sortie finale | `C:\trading-copilote\07-nouvelles sources\[nom_chaine]\` |
| Modèle API | `claude-opus-4-6` (confirmé valide par l'utilisateur) |
| Durées vidéos | 3 à 50 minutes |
| Launcher | `transvideo_pipeline.bat` (double-clic à la racine) |

---

## Confirmation avant exécution (A2)

Avant de créer les fichiers, affiche ce message et attends :

```
Je vais créer 5 fichiers :
  - C:\trading-copilote\scripts\channel_scraper.py  (NOUVEAU)
  - C:\trading-copilote\scripts\video_filter.py     (NOUVEAU)
  - C:\trading-copilote\scripts\chunk_fuse.py       (NOUVEAU)
  - C:\trading-copilote\scripts\agent.py            (NOUVEAU)
  - C:\trading-copilote\transvideo_pipeline.bat     (NOUVEAU)

Aucun fichier existant ne sera écrasé. Confirmes-tu ? (oui/non)
```

---

## Ordre d'exécution OBLIGATOIRE

1. Lire CLAUDE.md + disable-sleep.ps1 (style)
2. Demander confirmation (ci-dessus)
3. Phase 0 — Vérifier dépendances CLI
4. Créer `scripts\channel_scraper.py`
5. Créer `scripts\video_filter.py`
6. Créer `scripts\chunk_fuse.py`
7. Créer `scripts\agent.py`
8. Créer `transvideo_pipeline.bat`
9. Validation (lint + imports)
10. Commit git

---

## Phase 0 — Vérification dépendances

```powershell
# Vérifier yt-dlp
yt-dlp --version

# Vérifier ffmpeg
ffmpeg -version

# Installer yt-dlp si absent
pip install yt-dlp
```

**Si ffmpeg absent :** afficher `ERREUR : ffmpeg manquant — installe sur https://ffmpeg.org/download.html` et stopper.

---

## Fichier 1 — `C:\trading-copilote\scripts\channel_scraper.py`

```python
# -*- coding: utf-8 -*-
"""
channel_scraper.py
Récupère les URLs de vidéos d'une chaîne YouTube par son nom.
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\channel_scraper.py
"""

import subprocess
import json
import sys


def get_channel_videos(channel_name: str, max_videos: int = 50) -> list:
    """
    Retourne la liste des vidéos d'une chaîne YouTube.

    Args:
        channel_name: Nom de la chaîne (ex: "ICT Trading")
        max_videos: Nombre maximum de vidéos à récupérer

    Returns:
        Liste de dicts {url, title, duration, description, channel}
    """
    print(f"\n🔍 Recherche chaîne : '{channel_name}'")

    result = subprocess.run(
        [
            "yt-dlp",
            "--flat-playlist",
            "--dump-json",
            "--no-warnings",
            "--ignore-errors",
            f"ytsearch{max_videos}:{channel_name} trading",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
    )

    videos = []
    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)

            # Construire l'URL
            url = data.get("url") or data.get("webpage_url") or ""
            if not url:
                vid_id = data.get("id", "")
                if vid_id:
                    url = f"https://www.youtube.com/watch?v={vid_id}"
            if not url:
                continue

            # Filtrer par chaîne si l'info est disponible
            uploader = (data.get("uploader") or data.get("channel") or "").lower()
            channel_lower = channel_name.lower()
            if uploader:
                words = [w for w in channel_lower.split() if len(w) > 3]
                if words and not any(w in uploader for w in words):
                    continue

            videos.append(
                {
                    "url": url,
                    "title": data.get("title") or "",
                    "duration": data.get("duration") or 0,
                    "description": (data.get("description") or "")[:500],
                    "channel": data.get("uploader") or data.get("channel") or channel_name,
                }
            )
        except (json.JSONDecodeError, KeyError):
            continue

    print(f"   ✅ {len(videos)} vidéos trouvées pour '{channel_name}'")
    return videos


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "ICT Trading"
    vids = get_channel_videos(name)
    for v in vids[:5]:
        mins = v["duration"] // 60 if v["duration"] else 0
        print(f"  [{mins}min] {v['title'][:60]}")
```

---

## Fichier 2 — `C:\trading-copilote\scripts\video_filter.py`

```python
# -*- coding: utf-8 -*-
"""
video_filter.py
Filtre les vidéos trading par mots-clés et durée.
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\video_filter.py
"""

TRADING_KEYWORDS = [
    # Indicateurs techniques
    "ema", "rsi", "macd", "bollinger", "stochastique", "stochastic",
    "ichimoku", "moyenne mobile", "moving average", "fibonacci", "atr",
    # Stratégies
    "scalping", "swing", "day trading", "price action", "setup",
    "strategie", "stratégie", "strategy", "configuration", "methode",
    # Patterns
    "cassure", "breakout", "divergence", "croisement", "crossover",
    "support", "resistance", "résistance", "tendance", "trend",
    "retracement", "canal", "channel",
    # Bougies
    "heikin", "candlestick", "bougie", "marubozu", "doji", "engulfing",
    # Gestion risque
    "stop loss", "take profit", "risk reward", "ratio",
    # Analyse
    "analyse technique", "technical analysis", "signal", "entree",
    "forex", "crypto", "indices", "futures", "cac", "nasdaq",
    # Méthodes spécifiques TRADEX-AI
    "belkhayate", "ict", "smart money", "wyckoff", "elliott", "vwap",
    "order block", "fair value gap", "fvg", "liquidity",
]

DURATION_MIN_SEC = 3 * 60    # 3 minutes
DURATION_MAX_SEC = 50 * 60   # 50 minutes


def is_trading_video(video: dict) -> tuple:
    """
    Évalue si une vidéo est une vidéo de trading.

    Returns:
        (bool, str) — (acceptée, raison)
    """
    title = (video.get("title") or "").lower()
    description = (video.get("description") or "").lower()
    duration = video.get("duration") or 0

    # Filtre durée
    if duration > 0:
        if duration < DURATION_MIN_SEC:
            return False, f"trop courte ({duration // 60}min < 3min)"
        if duration > DURATION_MAX_SEC:
            return False, f"trop longue ({duration // 60}min > 50min)"

    # Filtre mots-clés
    text = title + " " + description
    matches = [kw for kw in TRADING_KEYWORDS if kw in text]

    if not matches:
        return False, "aucun mot-clé trading détecté"

    return True, f"{len(matches)} mot(s)-clé(s) : {', '.join(matches[:3])}"


def filter_videos(videos: list, verbose: bool = True) -> list:
    """Retourne uniquement les vidéos de trading acceptées."""
    accepted = []
    for v in videos:
        ok, reason = is_trading_video(v)
        title_short = (v.get("title") or "")[:52]
        if ok:
            accepted.append(v)
            if verbose:
                print(f"   ✅ {title_short:<52} ({reason})")
        else:
            if verbose:
                print(f"   ❌ {title_short:<52} ({reason})")

    print(f"\n   🎯 Résultat filtre : {len(accepted)}/{len(videos)} vidéos retenues")
    return accepted
```

---

## Fichier 3 — `C:\trading-copilote\scripts\chunk_fuse.py`

```python
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
```

---

## Fichier 4 — `C:\trading-copilote\scripts\agent.py`

```python
# -*- coding: utf-8 -*-
"""
agent.py — Orchestrateur principal TRANSVIDEO
Usage  : python scripts\\agent.py "Nom de la Chaîne YouTube"
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\agent.py
"""

import os
import sys
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from channel_scraper import get_channel_videos
from video_filter    import filter_videos
from chunk_fuse      import process_video


def check_env() -> str:
    """Vérifie les prérequis. Retourne la clé API ou quitte."""
    # Clé API
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        print("\n❌  ANTHROPIC_API_KEY non définie.")
        print("    Dans PowerShell : $env:ANTHROPIC_API_KEY = \"sk-ant-...\"")
        sys.exit(1)

    # ffmpeg
    if not shutil.which("ffmpeg"):
        print("\n❌  ffmpeg non trouvé. Installe sur https://ffmpeg.org/download.html")
        sys.exit(1)

    # yt-dlp
    if not shutil.which("yt-dlp"):
        print("\n❌  yt-dlp non trouvé. Lance : pip install yt-dlp")
        sys.exit(1)

    return api_key


def run(channel_name: str) -> None:
    """Pipeline complet : chaîne → filtre → Chunk&Fuse → .md."""
    sep = "=" * 58
    print(f"\n{sep}")
    print(f"  🚀 TRANSVIDEO PIPELINE — TRADEX-AI")
    print(f"  Chaîne : {channel_name}")
    print(f"{sep}")

    api_key = check_env()
    print("✅ Environnement OK")

    # Étape 1 — Vidéos de la chaîne
    print(f"\n{'─' * 58}")
    print("ÉTAPE 1 — Récupération des vidéos")
    print(f"{'─' * 58}")
    videos = get_channel_videos(channel_name, max_videos=50)

    if not videos:
        print("❌  Aucune vidéo trouvée. Vérifie le nom de la chaîne.")
        sys.exit(0)

    # Étape 2 — Filtre trading
    print(f"\n{'─' * 58}")
    print("ÉTAPE 2 — Filtre vidéos trading")
    print(f"{'─' * 58}")
    trading = filter_videos(videos, verbose=True)

    if not trading:
        print("❌  Aucune vidéo trading après filtrage.")
        sys.exit(0)

    # Étape 3 — Chunk & Fuse
    print(f"\n{'─' * 58}")
    print(f"ÉTAPE 3 — Analyse Chunk & Fuse ({len(trading)} vidéos)")
    print(f"{'─' * 58}")

    results = []
    for i, video in enumerate(trading, 1):
        print(f"\n[{i}/{len(trading)}]")
        out = process_video(video["url"], channel_name, api_key)
        results.append(out)

    # Résumé
    success = [r for r in results if r]
    print(f"\n{sep}")
    print(f"  ✅  {len(success)}/{len(trading)} fichiers générés")
    print(f"  📁  C:\\trading-copilote\\07-nouvelles sources\\{channel_name}\\")
    print(f"{sep}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python scripts\\agent.py \"Nom de la Chaîne\"")
        sys.exit(1)
    run(" ".join(sys.argv[1:]))
```

---

## Fichier 5 — `C:\trading-copilote\transvideo_pipeline.bat`

```batch
@echo off
chcp 65001 >nul 2>&1
title TRANSVIDEO PIPELINE - TRADEX-AI
color 0A

echo.
echo  ====================================================
echo    TRANSVIDEO PIPELINE - TRADEX-AI
echo    YouTube ^> Filtrage ^> Specifications Trading
echo  ====================================================
echo.

:: Verification Python
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : Python non installe.
    echo  Telecharge sur https://python.org
    echo.
    pause
    exit /b 1
)

:: Verification ffmpeg
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : ffmpeg non installe.
    echo  Telecharge sur https://ffmpeg.org/download.html
    echo.
    pause
    exit /b 1
)

:: Cle API
if "%ANTHROPIC_API_KEY%"=="" (
    echo  Cle ANTHROPIC_API_KEY non detectee.
    echo.
    set /p "APIKEY= Entre ta cle API Anthropic (sk-ant-...) : "
    set ANTHROPIC_API_KEY=%APIKEY%
    echo.
)

:: Nom de la chaine
echo  Exemples : ICT Trading, Belkhayate, Anton Kreil
echo.
set /p "CHANNEL= Entre le nom de la chaine YouTube : "

if "%CHANNEL%"=="" (
    echo  Aucun nom saisi. Fermeture.
    pause
    exit /b 0
)

echo.
echo  Lancement pour : %CHANNEL%
echo  ====================================================
echo.

cd /d "C:\trading-copilote"
python scripts\agent.py "%CHANNEL%"

echo.
echo  ====================================================
echo  Termine. Appuie sur une touche pour fermer.
echo  ====================================================
pause >nul
```

---

## Phase 9 — Validation (obligatoire après création)

### Vérification 1 — Fichiers présents
```powershell
dir C:\trading-copilote\scripts\channel_scraper.py
dir C:\trading-copilote\scripts\video_filter.py
dir C:\trading-copilote\scripts\chunk_fuse.py
dir C:\trading-copilote\scripts\agent.py
dir C:\trading-copilote\transvideo_pipeline.bat
```
**Attendu :** 5 fichiers, taille > 0

### Vérification 2 — Syntaxe Python (lint)
```powershell
python -m py_compile C:\trading-copilote\scripts\channel_scraper.py && echo OK_1
python -m py_compile C:\trading-copilote\scripts\video_filter.py    && echo OK_2
python -m py_compile C:\trading-copilote\scripts\chunk_fuse.py      && echo OK_3
python -m py_compile C:\trading-copilote\scripts\agent.py           && echo OK_4
```
**Attendu :** `OK_1` `OK_2` `OK_3` `OK_4` (aucune erreur)

### Vérification 3 — Imports
```powershell
cd C:\trading-copilote
python -c "from scripts.channel_scraper import get_channel_videos; print('channel_scraper OK')"
python -c "from scripts.video_filter import filter_videos; print('video_filter OK')"
```
**Attendu :** `channel_scraper OK` et `video_filter OK`

---

## Rollback (si erreur)

```powershell
Remove-Item "C:\trading-copilote\scripts\channel_scraper.py" -ErrorAction SilentlyContinue
Remove-Item "C:\trading-copilote\scripts\video_filter.py"    -ErrorAction SilentlyContinue
Remove-Item "C:\trading-copilote\scripts\chunk_fuse.py"      -ErrorAction SilentlyContinue
Remove-Item "C:\trading-copilote\scripts\agent.py"           -ErrorAction SilentlyContinue
Remove-Item "C:\trading-copilote\transvideo_pipeline.bat"    -ErrorAction SilentlyContinue
```

---

## Commit après validation

```
git add . && git commit -m "feat: add transvideo pipeline chunk-fuse automation"
```

---
*MISSION_TRANSVIDEO.md v2 — TRADEX-AI | 15/05/2026*
