# Script : Téléchargement audio de toutes les vidéos Belkhayate
# Exécuter depuis PowerShell dans n'importe quel dossier
# Durée estimée : 15-30 min selon la connexion

$OUTPUT_DIR = "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio"
$URLS_FILE  = "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\urls.txt"

New-Item -ItemType Directory -Force -Path $OUTPUT_DIR | Out-Null

Write-Host "=== DEBUT TELECHARGEMENT AUDIO BELKHAYATE ===" -ForegroundColor Cyan
Write-Host "Destination : $OUTPUT_DIR"
Write-Host "Nombre de videos : $(Get-Content $URLS_FILE | Measure-Object -Line | Select-Object -ExpandProperty Lines)"

yt-dlp `
    --batch-file $URLS_FILE `
    -x `
    --audio-format mp3 `
    --audio-quality 0 `
    -o "$OUTPUT_DIR\%(id)s_%(title)s.%(ext)s" `
    --write-info-json `
    --no-playlist `
    --ignore-errors `
    --sleep-interval 2 `
    --progress

Write-Host ""
Write-Host "=== TELECHARGEMENT TERMINE ===" -ForegroundColor Green
Write-Host "Fichiers MP3 dans : $OUTPUT_DIR"
Write-Host "Prochaine etape : executer 02_transcribe_whisper.ps1"
