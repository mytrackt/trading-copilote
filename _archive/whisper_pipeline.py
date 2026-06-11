"""
Pipeline : YouTube Audio -> Whisper Transcription
- Telecharge l'audio avec yt-dlp (anonyme, sans login)
- Transcrit avec Whisper API OpenAI (whisper-1)
- Sauvegarde dans transcripts/whisper_[video_id].txt
- Log succes/echecs dans transcripts/status.json
- Rate limiting : 2 secondes entre chaque video
"""

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

from openai import OpenAI

# --- Configuration ---
SCRIPT_DIR = Path(__file__).resolve().parent
VIDEOS_FILE = SCRIPT_DIR / "videos_a_transcrire.txt"
TRANSCRIPTS_DIR = SCRIPT_DIR / "transcripts"
STATUS_FILE = TRANSCRIPTS_DIR / "status.json"
AUDIO_TEMP_DIR = TRANSCRIPTS_DIR / "temp_audio"
RATE_LIMIT_SECONDS = 2
MAX_FILE_SIZE_MB = 25  # Whisper API limit


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERREUR: Variable d'environnement OPENAI_API_KEY non definie.")
        print("Execute dans PowerShell : setx OPENAI_API_KEY \"ta-cle-ici\"")
        sys.exit(1)
    return OpenAI(api_key=api_key)


def extract_video_id(url: str) -> str | None:
    """Extrait le video_id depuis une URL YouTube."""
    patterns = [
        r"youtu\.be/([a-zA-Z0-9_-]{11})",
        r"youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})",
        r"youtube\.com/live/([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def load_urls() -> list[tuple[str, str]]:
    """Charge les URLs et extrait les video_ids. Retourne [(url, video_id)]."""
    results = []
    with open(VIDEOS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            video_id = extract_video_id(line)
            if video_id:
                results.append((line, video_id))
            else:
                print(f"SKIP: URL non reconnue -> {line}")
    return results


def load_status() -> dict:
    """Charge le fichier status.json existant ou retourne un dict vide."""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_status(status: dict):
    """Sauvegarde le status.json."""
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, indent=2, ensure_ascii=False)


def download_audio(url: str, video_id: str) -> Path | None:
    """Telecharge l'audio avec yt-dlp. Retourne le chemin du fichier audio."""
    output_path = AUDIO_TEMP_DIR / f"{video_id}.%(ext)s"
    cmd = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "5",  # qualite moyenne = fichier plus petit
        "--no-playlist",
        "--output", str(output_path),
        "--no-warnings",
        "--quiet",
        url,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if result.returncode != 0:
            print(f"  yt-dlp erreur: {result.stderr.strip()}")
            return None
    except subprocess.TimeoutExpired:
        print("  yt-dlp timeout (5 min)")
        return None

    # Trouver le fichier telecharge
    for ext in ["mp3", "m4a", "webm", "opus", "wav"]:
        candidate = AUDIO_TEMP_DIR / f"{video_id}.{ext}"
        if candidate.exists():
            return candidate
    return None


def split_audio(audio_path: Path, chunk_duration_sec: int = 600) -> list[Path]:
    """Decoupe un fichier audio en morceaux de chunk_duration_sec secondes."""
    chunks = []
    chunk_dir = audio_path.parent / f"chunks_{audio_path.stem}"
    chunk_dir.mkdir(exist_ok=True)

    # Obtenir la duree totale
    probe_cmd = [
        "ffprobe", "-v", "quiet", "-print_format", "json",
        "-show_format", str(audio_path)
    ]
    try:
        result = subprocess.run(probe_cmd, capture_output=True, text=True, timeout=30)
        import json as _json
        info = _json.loads(result.stdout)
        duration = float(info["format"]["duration"])
    except Exception:
        duration = 7200  # fallback 2h

    num_chunks = int(duration / chunk_duration_sec) + 1
    for i in range(num_chunks):
        start = i * chunk_duration_sec
        chunk_path = chunk_dir / f"chunk_{i:03d}.mp3"
        cmd = [
            "ffmpeg", "-y", "-i", str(audio_path),
            "-ss", str(start), "-t", str(chunk_duration_sec),
            "-vn", "-acodec", "mp3", "-q:a", "5",
            str(chunk_path), "-loglevel", "quiet"
        ]
        subprocess.run(cmd, timeout=120)
        if chunk_path.exists() and chunk_path.stat().st_size > 1000:
            chunks.append(chunk_path)
    return chunks


def transcribe_audio(client: OpenAI, audio_path: Path) -> str | None:
    """Transcrit un fichier audio avec Whisper API. Decoupe si >25 MB."""
    file_size_mb = audio_path.stat().st_size / (1024 * 1024)

    if file_size_mb > MAX_FILE_SIZE_MB:
        print(f"  Fichier {file_size_mb:.1f} MB > {MAX_FILE_SIZE_MB} MB — decoupage en morceaux...")
        chunks = split_audio(audio_path)
        if not chunks:
            print("  Echec decoupage")
            return None
        print(f"  {len(chunks)} morceaux a transcrire...")
        texts = []
        for j, chunk in enumerate(chunks):
            print(f"    Morceau {j+1}/{len(chunks)} ({chunk.stat().st_size/(1024*1024):.1f} MB)...")
            try:
                with open(chunk, "rb") as f:
                    resp = client.audio.transcriptions.create(
                        model="whisper-1", file=f, language="fr"
                    )
                texts.append(resp.text)
                time.sleep(1.5)
            except Exception as e:
                print(f"    Erreur morceau {j+1}: {e}")
            finally:
                chunk.unlink(missing_ok=True)
        # Nettoyer le dossier chunks
        try:
            chunk.parent.rmdir()
        except Exception:
            pass
        return " ".join(texts) if texts else None

    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="fr",
        )
    return response.text


def cleanup_audio(audio_path: Path):
    """Supprime le fichier audio temporaire."""
    try:
        audio_path.unlink(missing_ok=True)
    except OSError:
        pass


def run_pipeline():
    """Execute le pipeline complet."""
    # Creer les dossiers
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    AUDIO_TEMP_DIR.mkdir(parents=True, exist_ok=True)

    # Charger
    urls = load_urls()
    status = load_status()
    client = get_openai_client()

    total = len(urls)
    done = 0
    skipped = 0
    failed = 0

    print(f"Pipeline Whisper : {total} videos a traiter")
    print(f"Transcripts deja existants : {sum(1 for v in status.values() if v.get('status') == 'success')}")
    print("-" * 60)

    for i, (url, video_id) in enumerate(urls, 1):
        transcript_path = TRANSCRIPTS_DIR / f"whisper_{video_id}.txt"

        # Skip si deja transcrit avec succes
        if video_id in status and status[video_id].get("status") == "success":
            if transcript_path.exists():
                skipped += 1
                print(f"[{i}/{total}] SKIP (deja fait) : {video_id}")
                continue

        print(f"[{i}/{total}] Traitement : {video_id}")

        # Etape 1 : Telecharger l'audio
        print("  1/2 Telechargement audio...")
        audio_path = download_audio(url, video_id)
        if not audio_path:
            failed += 1
            status[video_id] = {
                "status": "failed",
                "step": "download",
                "url": url,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            save_status(status)
            print(f"  ECHEC telechargement")
            time.sleep(RATE_LIMIT_SECONDS)
            continue

        # Etape 2 : Transcrire
        print(f"  2/2 Transcription Whisper ({audio_path.stat().st_size / (1024*1024):.1f} MB)...")
        try:
            text = transcribe_audio(client, audio_path)
        except Exception as e:
            text = None
            print(f"  Whisper erreur: {e}")

        cleanup_audio(audio_path)

        if not text:
            failed += 1
            status[video_id] = {
                "status": "failed",
                "step": "transcription",
                "url": url,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            save_status(status)
            print(f"  ECHEC transcription")
            time.sleep(RATE_LIMIT_SECONDS)
            continue

        # Sauvegarder le transcript
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(text)

        done += 1
        status[video_id] = {
            "status": "success",
            "url": url,
            "file": f"whisper_{video_id}.txt",
            "chars": len(text),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        save_status(status)
        print(f"  OK ({len(text)} caracteres)")

        # Rate limiting
        if i < total:
            time.sleep(RATE_LIMIT_SECONDS)

    # Resume final
    print("\n" + "=" * 60)
    print(f"TERMINE : {done} succes / {failed} echecs / {skipped} deja faits")
    print(f"Status log : {STATUS_FILE}")


if __name__ == "__main__":
    run_pipeline()
