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
