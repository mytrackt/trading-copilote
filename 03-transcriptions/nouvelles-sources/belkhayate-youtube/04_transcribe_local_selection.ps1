<#
.SYNOPSIS
  Transcrit (Whisper medium, FR) UNIQUEMENT les videos marquees A_TRANSCRIRE
  dans AUDIT_VIDEOS_LOCAL.csv, dans l'ordre de priorite (duree croissante).

.NOTES
  - Source statuts : C:\trading-copilote\04-cerveau-trading\AUDIT_VIDEOS_LOCAL.csv
  - Skip si le transcript .txt existe deja (reprise sans recalcul).
  - Aucune suppression : ce script ne fait que lire le CSV et ecrire des .txt.
#>

$ErrorActionPreference = "Stop"

# --- Chemins ---
$CSV       = "C:\trading-copilote\04-cerveau-trading\AUDIT_VIDEOS_LOCAL.csv"
$VIDEO_DIR = "D:\Belkhayate-Videos"
$OUT_DIR   = "C:\trading-copilote\03-transcriptions\nouvelles-sources\belkhayate-youtube\transcripts"

# --- Verifications prealables ---
if (-not (Test-Path $CSV))       { throw "CSV introuvable : $CSV" }
if (-not (Test-Path $VIDEO_DIR)) { throw "Dossier video introuvable : $VIDEO_DIR" }
if (-not (Get-Command whisper -ErrorAction SilentlyContinue)) { throw "Commande 'whisper' introuvable dans le PATH." }
if (-not (Test-Path $OUT_DIR))   { New-Item -ItemType Directory -Path $OUT_DIR -Force | Out-Null }

# --- Selection A_TRANSCRIRE, ordre de priorite (duree croissante) ---
$videos = Import-Csv $CSV |
    Where-Object { $_.statut -eq "A_TRANSCRIRE" } |
    Sort-Object { [int]$_.priorite }

$total = $videos.Count
if ($total -eq 0) { Write-Host "Aucune video A_TRANSCRIRE dans le CSV."; exit 0 }

Write-Host "=== $total videos A_TRANSCRIRE -> Whisper medium (FR) ===" -ForegroundColor Cyan
Write-Host "Sortie : $OUT_DIR`n"

$idx = 0
$ok = 0; $skip = 0; $err = 0
foreach ($v in $videos) {
    $idx++
    $nom = $v.fichier
    $videoPath = Join-Path $VIDEO_DIR $nom
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($nom)
    $txtPath = Join-Path $OUT_DIR ("{0}.txt" -f $stem)

    # Skip si deja transcrit
    if (Test-Path $txtPath) {
        $skip++
        Write-Host ("[{0}/{1}] {2} -> SKIP (deja transcrit)" -f $idx, $total, $nom) -ForegroundColor DarkGray
        continue
    }

    # Verifier que la video existe
    if (-not (Test-Path $videoPath)) {
        $err++
        Write-Host ("[{0}/{1}] {2} -> ABSENT (video introuvable)" -f $idx, $total, $nom) -ForegroundColor Red
        continue
    }

    Write-Host ("[{0}/{1}] {2} ..." -f $idx, $total, $nom) -ForegroundColor Yellow
    whisper $videoPath --language fr --model medium --output_format txt --output_dir $OUT_DIR

    if ($LASTEXITCODE -eq 0 -and (Test-Path $txtPath)) {
        $ok++
        Write-Host ("[{0}/{1}] {2} -> OK" -f $idx, $total, $nom) -ForegroundColor Green
    } else {
        $err++
        Write-Host ("[{0}/{1}] {2} -> ECHEC (whisper rc=$LASTEXITCODE)" -f $idx, $total, $nom) -ForegroundColor Red
    }
}

Write-Host "`n=== RESUME ===" -ForegroundColor Cyan
Write-Host "Transcrites : $ok"
Write-Host "Ignorees    : $skip (deja presentes)"
Write-Host "Echecs      : $err"
Write-Host "Dossier     : $OUT_DIR"
