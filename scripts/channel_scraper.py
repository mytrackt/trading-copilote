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


def _scrape_channel_url(channel_url: str, max_videos: int, channel_name: str = "") -> list:
    """
    Scrape les vidéos d'une chaîne via son URL directe.

    Args:
        channel_url: URL de la page /videos de la chaîne
        max_videos: Nombre max de vidéos à récupérer
        channel_name: Nom de la chaîne (fallback pour le champ 'channel')

    Returns:
        Liste de dicts {url, title, duration, description, channel}
    """
    result = subprocess.run(
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
    Fallback : cherche la chaîne via ytsearch3 et extrait l'URL de la chaîne
    depuis les résultats.

    Args:
        channel_name: Nom de la chaîne à chercher

    Returns:
        URL de la page /videos de la chaîne, ou chaîne vide si introuvable
    """
    result = subprocess.run(
        [
            "yt-dlp",
            "--flat-playlist",
            "--dump-json",
            "--no-warnings",
            "--ignore-errors",
            f"ytsearch3:{channel_name}",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore",
    )

    for line in result.stdout.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
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

    Returns:
        Liste de dicts {url, title, duration, description, channel}
    """
    print(f"\n🔍 Recherche chaîne : '{channel_name}'")

    # Étape 1 — URL directe @handle
    handle = channel_name.replace(" ", "")
    direct_url = f"https://www.youtube.com/@{handle}/videos"
    print(f"   ▶ Étape 1 — URL directe : {direct_url}")
    videos = _scrape_channel_url(direct_url, max_videos, channel_name)

    # Étape 2 — fallback via recherche
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
