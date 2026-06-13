# Script : Transcription Whisper de tous les MP3 Belkhayate
# Modele : turbo (rapide, ~95% precision sur le francais)
# Durée estimée : 2-6h selon le nombre de vidéos (CPU)
# Lancer et laisser tourner (peut rouler la nuit)

$AUDIO_DIR  = "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\audio"
$OUTPUT_DIR = "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts"

New-Item -ItemType Directory -Force -Path $OUTPUT_DIR | Out-Null

$mp3files = Get-ChildItem -Path $AUDIO_DIR -Filter "*.mp3"
$total = $mp3files.Count
$done  = 0

Write-Host "=== DEBUT TRANSCRIPTION WHISPER ===" -ForegroundColor Cyan
Write-Host "Modele : turbo | Langue : fr | Fichiers : $total"
Write-Host "Sortie : $OUTPUT_DIR"
Write-Host ""

foreach ($file in $mp3files) {
    $done++
    $name = $file.BaseName
    $txtPath = Join-Path $OUTPUT_DIR "$name.txt"

    # Sauter si deja transcrit
    if (Test-Path $txtPath) {
        Write-Host "[$done/$total] SKIP (deja transcrit) : $name" -ForegroundColor Yellow
        continue
    }

    Write-Host "[$done/$total] Transcription : $name" -ForegroundColor Green

    whisper $file.FullName `
        --model turbo `
        --language fr `
        --output_dir $OUTPUT_DIR `
        --output_format txt `
        --fp16 False `
        --verbose False

    Start-Sleep -Seconds 1
}

Write-Host ""
Write-Host "=== TRANSCRIPTION TERMINEE ===" -ForegroundColor Green
Write-Host "Fichiers TXT dans : $OUTPUT_DIR"
Write-Host ""
Write-Host "=== LANCEMENT AUDIT QUALITE ===" -ForegroundColor Cyan
python "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\03_audit_qualite.py"
