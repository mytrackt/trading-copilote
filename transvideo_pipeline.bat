@echo off
chcp 65001 >nul 2>&1
title TRANSVIDEO PIPELINE - TRADEX-AI
color 0A

echo.
echo  ====================================================
echo    TRANSVIDEO PIPELINE - TRADEX-AI
echo    YouTube ^> Filtrage ^> Specifications Trading
echo  ====================================================
echo.

:: Verification Python
py --version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : Python non installe.
    echo  Telecharge sur https://python.org
    echo.
    pause
    exit /b 1
)

:: Verification ffmpeg
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : ffmpeg non installe.
    echo  Telecharge sur https://ffmpeg.org/download.html
    echo.
    pause
    exit /b 1
)

:: Verification yt-dlp
yt-dlp --version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : yt-dlp non installe.
    echo  Lance : pip install yt-dlp
    echo.
    pause
    exit /b 1
)

:: Auto-update yt-dlp (quiet, non bloquant si pas de reseau)
echo  Verification mise a jour yt-dlp...
py -m pip install -q -U yt-dlp >nul 2>&1

:: Cle API - saisie masquee via PowerShell Read-Host -AsSecureString
if "%ANTHROPIC_API_KEY%"=="" (
    echo  Cle ANTHROPIC_API_KEY non detectee.
    echo.
    echo  Saisie masquee de la cle Anthropic ^(sk-ant-...^) - caracteres affiches comme * :
    for /f "delims=" %%i in ('powershell -NoProfile -Command "$s = Read-Host -AsSecureString; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))"') do set "ANTHROPIC_API_KEY=%%i"
    echo.
)

:: Menu de selection mode
echo  Choisis le mode :
echo    1. Analyser une chaine YouTube complete
echo    2. Analyser une video unique (URL)
echo.
set /p "MODE= Ton choix (1 ou 2) : "

if "%MODE%"=="1" goto MODE_CHANNEL
if "%MODE%"=="2" goto MODE_URL

echo  Choix invalide. Fermeture.
pause
exit /b 1

:MODE_CHANNEL
echo.
echo  Exemples : ICT Trading, Belkhayate, Anton Kreil
echo.
set /p "CHANNEL= Entre le nom de la chaine YouTube : "

if "%CHANNEL%"=="" (
    echo  Aucun nom saisi. Fermeture.
    pause
    exit /b 0
)

echo.
echo  Lancement pour la chaine : %CHANNEL%
echo  ====================================================
echo.

cd /d "C:\trading-copilote"
py scripts\agent.py --channel "%CHANNEL%"
goto END

:MODE_URL
echo.
echo  Exemple : https://www.youtube.com/watch?v=...
echo.
set /p "VIDEO_URL= Entre l'URL de la video : "

if "%VIDEO_URL%"=="" (
    echo  Aucune URL saisie. Fermeture.
    pause
    exit /b 0
)

echo.
echo  Lancement pour la video : %VIDEO_URL%
echo  ====================================================
echo.

cd /d "C:\trading-copilote"
py scripts\agent.py --url "%VIDEO_URL%"
goto END

:END

echo.
echo  ====================================================
echo  Termine. Appuie sur une touche pour fermer.
echo  ====================================================
pause >nul
