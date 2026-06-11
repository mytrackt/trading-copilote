# -*- coding: utf-8 -*-
"""
agent.py — Orchestrateur principal TRANSVIDEO
Usage  :
  py scripts\\agent.py --channel "Nom de la Chaîne YouTube" [--limit N]
  py scripts\\agent.py --url "https://www.youtube.com/watch?v=..."
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\agent.py
"""

import os
import re
import sys
import json
import shutil
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from channel_scraper import get_channel_videos
from video_filter    import filter_videos
from chunk_fuse      import process_video


# ── BASE_DIR + paths (P2.10) ────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = Path(BASE_DIR) / "logs"
CHECKPOINT_FILE = LOGS_DIR / "transvideo_checkpoint.json"
OUTPUT_BASE = Path(BASE_DIR).parent / "03-transcriptions" / "nouvelles-sources"


# ── Logging (P2.2) ──────────────────────────────────────────────────────────
def setup_logging() -> Path:
    """Configure le root logger avec fichier daté dans logs\\."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f"transvideo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    # On évite les doublons si l'agent est relancé dans la même session Python
    for h in list(root.handlers):
        root.removeHandler(h)

    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
    ))
    root.addHandler(handler)
    return log_file


logger = logging.getLogger("transvideo.agent")


# ── Validation CLI YouTube ──────────────────────────────────────────────────
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def _with_scheme(value: str) -> str:
    """Ajoute https:// si l'utilisateur donne une URL sans schéma."""
    text = value.strip()
    if text.startswith(("http://", "https://")):
        return text
    if text.startswith(("www.youtube.com/", "youtube.com/", "m.youtube.com/", "youtu.be/")):
        return "https://" + text
    return text


def _is_url(value: str) -> bool:
    parsed = urlparse(_with_scheme(value))
    return bool(parsed.scheme and parsed.netloc)


def _is_youtube_host(host: str) -> bool:
    host = host.lower()
    return host == "youtu.be" or host == "youtube.com" or host.endswith(".youtube.com")


def _clean_video_id(value: str) -> str:
    video_id = value.strip().split("/")[0].split("?")[0].split("&")[0]
    return video_id if VIDEO_ID_RE.match(video_id) else ""


def normalize_video_url(value: str) -> str:
    """
    Retourne une URL watch canonique pour watch, youtu.be et shorts.
    Retourne "" si l'entrée n'est pas une URL vidéo YouTube supportée.
    """
    parsed = urlparse(_with_scheme(value))
    host = parsed.netloc.lower()
    path = parsed.path.strip("/")

    if host == "youtu.be":
        video_id = _clean_video_id(path)
        return f"https://www.youtube.com/watch?v={video_id}" if video_id else ""

    if not _is_youtube_host(host):
        return ""

    if parsed.path == "/watch":
        video_id = _clean_video_id(parse_qs(parsed.query).get("v", [""])[0])
        return f"https://www.youtube.com/watch?v={video_id}" if video_id else ""

    if path.startswith("shorts/"):
        video_id = _clean_video_id(path.split("/", 1)[1])
        return f"https://www.youtube.com/watch?v={video_id}" if video_id else ""

    return ""


def is_channel_url(value: str) -> bool:
    """Détecte les formats chaîne YouTube explicitement supportés."""
    parsed = urlparse(_with_scheme(value))
    if not _is_youtube_host(parsed.netloc):
        return False
    parts = [p for p in parsed.path.strip("/").split("/") if p]
    if not parts:
        return False
    first = parts[0]
    return (
        first.startswith("@")
        or first in {"channel", "c", "user"}
    )


def normalize_channel_input(value: str) -> str:
    """
    Valide le mode --channel. Les noms simples sont conservés tels quels.
    Les URLs de vidéos sont refusées pour éviter un basculement silencieux.
    """
    text = value.strip()
    if not text:
        raise ValueError("entrée --channel vide")

    if normalize_video_url(text):
        raise ValueError("une URL de vidéo a été fournie avec --channel ; utilise --url")

    if _is_url(text):
        parsed = urlparse(_with_scheme(text))
        if not _is_youtube_host(parsed.netloc):
            raise ValueError("--channel accepte un nom de chaîne ou une URL YouTube de chaîne")
        if not is_channel_url(text):
            raise ValueError("URL YouTube non reconnue comme URL de chaîne")
        return _with_scheme(text)

    return text


def normalize_url_input(value: str) -> str:
    """Valide le mode --url et retourne une URL vidéo canonique."""
    text = value.strip()
    if not text:
        raise ValueError("entrée --url vide")

    if is_channel_url(text):
        raise ValueError("une URL de chaîne a été fournie avec --url ; utilise --channel")

    normalized = normalize_video_url(text)
    if not normalized:
        raise ValueError(
            "--url attend une URL vidéo YouTube watch, youtu.be ou Shorts valide"
        )
    return normalized


# ── Checkpoint reprise crash (P2.7) ─────────────────────────────────────────
def load_checkpoint(channel_name: str) -> set:
    """Retourne le set des URLs déjà traitées pour cette chaîne."""
    if not CHECKPOINT_FILE.exists():
        return set()
    try:
        data = json.loads(CHECKPOINT_FILE.read_text(encoding="utf-8"))
        return set(data.get(channel_name, []))
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("checkpoint load failed: %s", exc)
        return set()


def save_checkpoint(channel_name: str, processed_urls: set) -> None:
    """Persiste les URLs traitées (écriture atomique)."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    data: dict = {}
    if CHECKPOINT_FILE.exists():
        try:
            data = json.loads(CHECKPOINT_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            data = {}
    data[channel_name] = sorted(processed_urls)

    tmp = str(CHECKPOINT_FILE) + ".tmp"
    Path(tmp).write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    os.replace(tmp, str(CHECKPOINT_FILE))


# ── Vérifications environnement ─────────────────────────────────────────────
def check_env() -> str:
    """Vérifie les prérequis. Retourne la clé API ou quitte."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        print("\n❌  ANTHROPIC_API_KEY non définie.")
        print("    Dans PowerShell : $env:ANTHROPIC_API_KEY = \"sk-ant-...\"")
        sys.exit(1)

    if not shutil.which("ffmpeg"):
        print("\n❌  ffmpeg non trouvé. Installe sur https://ffmpeg.org/download.html")
        sys.exit(1)

    if not shutil.which("yt-dlp"):
        print("\n❌  yt-dlp non trouvé. Lance : pip install yt-dlp")
        sys.exit(1)

    return api_key


def run(channel_name: str, limit: Optional[int] = None, max_videos: int = 300) -> None:
    """
    Pipeline complet : chaîne → filtre → Chunk&Fuse → .md.

    Args:
        channel_name: Nom de la chaîne YouTube
        limit: Si défini, ne traite que les `limit` premières vidéos après filtre
        max_videos: Nombre max de vidéos récupérées par le scraper (défaut 300)
    """
    log_file = setup_logging()
    logger.info("==== TRANSVIDEO start | channel='%s' max_videos=%d limit=%s ====",
                channel_name, max_videos, limit)

    sep = "=" * 58
    print(f"\n{sep}")
    print(f"  🚀 TRANSVIDEO PIPELINE — TRADEX-AI")
    print(f"  Chaîne : {channel_name}")
    print(f"  Log    : {log_file}")
    print(f"{sep}")

    api_key = check_env()
    print("✅ Environnement OK")

    # Étape 1 — Vidéos de la chaîne
    print(f"\n{'─' * 58}")
    print("ÉTAPE 1 — Récupération des vidéos")
    print(f"{'─' * 58}")
    videos = get_channel_videos(channel_name, max_videos=max_videos)

    if not videos:
        logger.warning("aucune vidéo trouvée pour '%s'", channel_name)
        print("❌  Aucune vidéo trouvée. Vérifie le nom de la chaîne.")
        sys.exit(1)

    # Étape 2 — Filtre trading
    print(f"\n{'─' * 58}")
    print("ÉTAPE 2 — Filtre vidéos trading")
    print(f"{'─' * 58}")
    trading = filter_videos(videos, verbose=True)

    if not trading:
        logger.warning("aucune vidéo après filtrage")
        print("❌  Aucune vidéo trading après filtrage.")
        sys.exit(1)

    # Limite optionnelle (CLI --limit N)
    if limit is not None and limit > 0:
        if len(trading) > limit:
            print(f"\n   ⚠  Limit appliquée : {limit} premières sur {len(trading)} (--limit)")
            logger.info("limit applied: %d/%d", limit, len(trading))
            trading = trading[:limit]

    # Étape 3 — Chunk & Fuse avec checkpoint
    print(f"\n{'─' * 58}")
    print(f"ÉTAPE 3 — Analyse Chunk & Fuse ({len(trading)} vidéos)")
    print(f"{'─' * 58}")

    processed = load_checkpoint(channel_name)
    if processed:
        print(f"   ↩ Checkpoint : {len(processed)} vidéos déjà traitées, reprise au reste")
        logger.info("checkpoint resumed: %d already processed", len(processed))

    results = []
    skipped = 0
    for i, video in enumerate(trading, 1):
        url = video["url"]
        if url in processed:
            skipped += 1
            print(f"\n[{i}/{len(trading)}] ⏭️  Déjà traitée : {video['title'][:50]}")
            continue

        print(f"\n[{i}/{len(trading)}]")
        out = process_video(url, channel_name, api_key)
        results.append(out)

        if out:
            processed.add(url)
            save_checkpoint(channel_name, processed)

    # Résumé
    success = [r for r in results if r]
    logger.info("TRANSVIDEO done | success=%d skipped=%d total=%d",
                len(success), skipped, len(trading))

    print(f"\n{sep}")
    print(f"  ✅  {len(success)}/{len(trading) - skipped} fichiers générés ({skipped} skippées via checkpoint)")
    print(f"  📁  {OUTPUT_BASE / channel_name}")
    print(f"  📋  Log complet : {log_file}")
    print(f"{sep}\n")


def run_single_url(url: str) -> None:
    """Pipeline pour une vidéo unique (mode --url). Skip channel_scraper + video_filter."""
    log_file = setup_logging()
    logger.info("==== TRANSVIDEO start | mode=single-url | url='%s' ====", url)

    sep = "=" * 58
    print(f"\n{sep}")
    print(f"  🚀 TRANSVIDEO PIPELINE — TRADEX-AI (mode URL unique)")
    print(f"  URL    : {url}")
    print(f"  Log    : {log_file}")
    print(f"{sep}")

    api_key = check_env()
    print("✅ Environnement OK")

    print(f"\n{'─' * 58}")
    print("ÉTAPE — Chunk & Fuse (vidéo unique)")
    print(f"{'─' * 58}")

    out = process_video(url, "Single Videos", api_key)

    logger.info("TRANSVIDEO done | success=%s", bool(out))

    print(f"\n{sep}")
    if out:
        print(f"  ✅  Fichier généré : {out}")
    else:
        print(f"  ⏭️  Aucun fichier généré (pré-screen négatif ou erreur)")
        sys.exit(1)
    print(f"  📁  {OUTPUT_BASE / 'Single Videos'}")
    print(f"  📋  Log complet : {log_file}")
    print(f"{sep}\n")


def _build_parser() -> argparse.ArgumentParser:
    """Argparse : --channel et --url mutuellement exclusifs."""
    parser = argparse.ArgumentParser(
        prog="agent.py",
        description="TRANSVIDEO — pipeline YouTube vers specs trading (TRADEX-AI)"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--channel",
        metavar="NAME",
        help="Nom ou URL de chaîne YouTube à scraper entièrement"
    )
    group.add_argument(
        "--url",
        metavar="URL",
        help="URL d'une vidéo unique YouTube watch, youtu.be ou Shorts"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Limite le nombre de vidéos traitées (mode --channel uniquement)"
    )
    parser.add_argument(
        "--max-videos",
        type=int,
        default=300,
        metavar="N",
        help="Nombre max de vidéos récupérées par le scraper YouTube (défaut 300, mode --channel uniquement)"
    )
    return parser


if __name__ == "__main__":
    parser = _build_parser()
    args = parser.parse_args()

    try:
        if args.url:
            args.url = normalize_url_input(args.url)
        else:
            args.channel = normalize_channel_input(args.channel)
    except ValueError as exc:
        parser.error(str(exc))

    if args.url:
        if args.limit is not None:
            print("⚠  --limit ignoré en mode --url")
        if args.max_videos != 300:
            print("⚠  --max-videos ignoré en mode --url")
        run_single_url(args.url)
    else:
        run(args.channel, limit=args.limit, max_videos=args.max_videos)
