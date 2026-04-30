# ============================================================
# RESTORE-SLEEP.PS1 — À lancer APRÈS les 6 jours de scraping
# Restaure les paramètres normaux de veille Windows
# ============================================================

Write-Host ""
Write-Host "⏳ Restauration en cours..." -ForegroundColor Yellow

# Restaurer la mise en veille à 30 minutes (valeur Windows standard)
powercfg /change standby-timeout-ac 30

# Restaurer l'hibernation à 60 minutes
powercfg /change hibernate-timeout-ac 60

# Restaurer l'écran à 15 minutes
powercfg /change monitor-timeout-ac 15

# Réactiver l'hibernation
powercfg /hibernate on

Write-Host ""
Write-Host "✅ Paramètres de veille RESTAURÉS." -ForegroundColor Green
Write-Host "✅ Veille : 30 min" -ForegroundColor Green
Write-Host "✅ Hibernation : 60 min" -ForegroundColor Green
Write-Host "✅ Écran : 15 min" -ForegroundColor Green
Write-Host ""
Write-Host "Ton PC fonctionne à nouveau normalement." -ForegroundColor Cyan
Write-Host ""
