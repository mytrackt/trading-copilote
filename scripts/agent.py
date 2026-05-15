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
