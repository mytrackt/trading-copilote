# ============================================================
# DISABLE-SLEEP.PS1 — À lancer AVANT de démarrer le scraping
# Empêche Windows de mettre le PC en veille pendant 6 jours
# À copier dans C:\trading-skills-factory\ si tu veux
# ============================================================

Write-Host ""
Write-Host "⏳ Configuration en cours..." -ForegroundColor Yellow

# Désactiver la mise en veille (sur secteur)
powercfg /change standby-timeout-ac 0

# Désactiver l'hibernation (sur secteur)
powercfg /change hibernate-timeout-ac 0

# Garder l'écran allumé 2h max (économie d'énergie raisonnable)
powercfg /change monitor-timeout-ac 120

# Désactiver l'hibernation globale
powercfg /hibernate off

Write-Host ""
Write-Host "✅ Mise en veille DÉSACTIVÉE." -ForegroundColor Green
Write-Host "✅ Hibernation DÉSACTIVÉE." -ForegroundColor Green
Write-Host "✅ Ton PC restera allumé pendant tout le scraping." -ForegroundColor Green
Write-Host ""
Write-Host "⚠️  IMPORTANT : Dans 6 jours, lance restore-sleep.ps1" -ForegroundColor Red
Write-Host "    pour restaurer tes paramètres normaux." -ForegroundColor Red
Write-Host ""
