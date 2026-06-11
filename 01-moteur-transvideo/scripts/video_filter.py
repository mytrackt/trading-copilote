# -*- coding: utf-8 -*-
"""
video_filter.py
Filtre les vidéos par durée (3 à 50 minutes).
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\video_filter.py
"""

import logging

DURATION_MIN_SEC = 3 * 60    # 3 minutes
DURATION_MAX_SEC = 50 * 60   # 50 minutes

logger = logging.getLogger("transvideo.video_filter")


def is_trading_video(video: dict) -> tuple[bool, str]:
    """
    Évalue si une vidéo passe le filtre durée.
    Une durée à 0 est rejetée : live YouTube ou playlist (yt-dlp retourne 0).

    Returns:
        (bool, str) — (acceptée, raison)
    """
    duration = video.get("duration") or 0

    if duration == 0:
        return False, "duree inconnue (live ou playlist - rejete)"

    if duration < DURATION_MIN_SEC:
        return False, f"trop courte ({duration // 60}min < 3min)"
    if duration > DURATION_MAX_SEC:
        return False, f"trop longue ({duration // 60}min > 50min)"

    return True, f"duree OK ({duration // 60}min)"


def filter_videos(videos: list[dict], verbose: bool = True) -> list[dict]:
    """Retourne uniquement les vidéos qui passent le filtre durée."""
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
