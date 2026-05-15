# -*- coding: utf-8 -*-
"""
video_filter.py
Filtre les vidéos par durée (3 à 50 minutes).
Projet : TRADEX-AI
Chemin : C:\\trading-copilote\\scripts\\video_filter.py
"""

DURATION_MIN_SEC = 3 * 60    # 3 minutes
DURATION_MAX_SEC = 50 * 60   # 50 minutes


def is_trading_video(video: dict) -> tuple:
    """
    Évalue si une vidéo passe le filtre durée.
    Si durée inconnue (= 0), la vidéo est acceptée.

    Returns:
        (bool, str) — (acceptée, raison)
    """
    duration = video.get("duration") or 0

    if duration == 0:
        return True, "duree inconnue (acceptee)"

    if duration < DURATION_MIN_SEC:
        return False, f"trop courte ({duration // 60}min < 3min)"
    if duration > DURATION_MAX_SEC:
        return False, f"trop longue ({duration // 60}min > 50min)"

    return True, f"duree OK ({duration // 60}min)"


def filter_videos(videos: list, verbose: bool = True) -> list:
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
