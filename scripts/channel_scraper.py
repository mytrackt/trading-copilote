# -*- coding: utf-8 -*-
"""
channel_scraper.py
Récupère les URLs de vidéos d'une chaîne YouTube par son nom.
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\channel_scraper.py
"""

import re
import subprocess
import json
import sys
import unicodedata

YTDLP_TIMEOUT = 120  # secondes


def _make_handle(channel_name: str) -> str:
    """
    Convertit un nom de chaîne en handle YouTube ASCII :
      "Élève Trader" → "EleveTrader"
      "Bourse-Direct" → "Bourse-Direct"
    """
    normalized = unicodedata.normalize("NFKD", channel_name)
    ascii_only = "".join(c for c in normalized if not unicodedata.combining(c))
    return re.sub(r"[^A-Za-z0-9._-]", "", ascii_only)


def _run_ytdlp(args: list, label: str) -> subprocess.CompletedProcess:
    """Lance yt-dlp avec timeout. Lève RuntimeError sur timeout."""
    try:
        return subprocess.run(
            args,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=YTDLP_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"{label} timeout ({YTDLP_TIMEOUT}s)")


def _scrape_channel_url(channel_url: str, max_videos: int, channel_name: str = "") -> list:
    """
    Scrape les vidéos d'une chaîne via son URL directe.

    Returns:
        Liste de dicts {url, title, duration, description, channel}
    """
    try:
        result = _run_ytdlp(
            [
                "yt-dlp",
                "--flat-playlist",
                "--dump-json",
                "--no-warnings",
                "--ignore-errors",
                "--playlist-end",
                str(max_videos),
                channel_url,
            ],
            label="yt-dlp channel scrape",
        )
    except RuntimeError as exc:
        print(f"      ↳ {exc}")
        return []

    if result.returncode != 0:
        stderr_snippet = (result.stderr or "")[-200:].strip()
        print(f"      ↳ yt-dlp returncode={result.returncode} : {stderr_snippet}")

    videos = []
    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)

            url = data.get("url") or data.get("webpage_url") or ""
            if not url:
                vid_id = data.get("id", "")
                if vid_id:
                    url = f"https://www.youtube.com/watch?v={vid_id}"
            if not url:
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

    return videos


def _find_channel_url_via_search(channel_name: str) -> str:
    """
    Fallback : ytsearch3 + extraction channel_url + validation par match de mots.
    Retourne chaîne vide si aucun résultat ne matche.
    """
    try:
        result = _run_ytdlp(
            [
                "yt-dlp",
                "--flat-playlist",
                "--dump-json",
                "--no-warnings",
                "--ignore-errors",
                f"ytsearch3:{channel_name}",
            ],
            label="yt-dlp ytsearch3",
        )
    except RuntimeError as exc:
        print(f"      ↳ {exc}")
        return ""

    if result.returncode != 0:
        stderr_snippet = (result.stderr or "")[-200:].strip()
        print(f"      ↳ yt-dlp ytsearch3 returncode={result.returncode} : {stderr_snippet}")

    channel_lower = channel_name.lower()
    keywords = [w for w in channel_lower.split() if len(w) > 3]

    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            # Validation : uploader doit contenir au moins un mot-clé du nom cherché
            uploader = (data.get("uploader") or data.get("channel") or "").lower()
            if keywords and uploader and not any(k in uploader for k in keywords):
                continue

            channel_url = data.get("channel_url") or data.get("uploader_url") or ""
            if channel_url:
                channel_url = channel_url.rstrip("/")
                if not channel_url.endswith("/videos"):
                    channel_url = channel_url + "/videos"
                return channel_url
        except (json.JSONDecodeError, KeyError):
            continue

    return ""


def get_channel_videos(channel_name: str, max_videos: int = 300) -> list:
    """
    Retourne la liste des vidéos d'une chaîne YouTube en 2 étapes :
      Étape 1 : URL directe https://www.youtube.com/@{handle}/videos
      Étape 2 : fallback via ytsearch3 si l'étape 1 échoue

    Args:
        channel_name: Nom de la chaîne (ex: "The Trading Geek")
        max_videos: Nombre maximum de vidéos à récupérer (défaut 300)
    """
    print(f"\n🔍 Recherche chaîne : '{channel_name}'")

    handle = _make_handle(channel_name)
    direct_url = f"https://www.youtube.com/@{handle}/videos"
    print(f"   ▶ Étape 1 — URL directe : {direct_url}")
    videos = _scrape_channel_url(direct_url, max_videos, channel_name)

    if not videos:
        print(f"   ⚠ Étape 1 échouée — fallback via ytsearch3")
        channel_url = _find_channel_url_via_search(channel_name)
        if channel_url:
            print(f"   ▶ Étape 2 — URL chaîne trouvée : {channel_url}")
            videos = _scrape_channel_url(channel_url, max_videos, channel_name)
        else:
            print(f"   ❌ Aucune chaîne trouvée pour '{channel_name}'")

    print(f"   ✅ {len(videos)} vidéos trouvées pour '{channel_name}'")
    return videos


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "ICT Trading"
    vids = get_channel_videos(name)
    for v in vids[:5]:
        mins = v["duration"] // 60 if v["duration"] else 0
        print(f"  [{mins}min] {v['title'][:60]}")
