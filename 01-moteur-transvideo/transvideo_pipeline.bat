@echo off
setlocal EnableExtensions DisableDelayedExpansion
chcp 65001 >nul 2>&1
title TRANSVIDEO PIPELINE - TRADEX-AI
color 0A

cd /d "%~dp0"
if errorlevel 1 (
    echo.
    echo  ERREUR : impossible d'acceder au dossier du lanceur.
    echo.
    pause
    exit /b 1
)

echo.
echo  ====================================================
echo    TRANSVIDEO PIPELINE - TRADEX-AI
echo    YouTube ^> Filtrage ^> Specifications Trading
echo  ====================================================
echo.

if not exist "scripts\agent.py" (
    echo  ERREUR : scripts\agent.py introuvable.
    echo  Lance ce fichier .bat depuis la racine du projet Transvideo.
    echo.
    pause
    exit /b 1
)

py --version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : Python non installe ou launcher py indisponible.
    echo  Telecharge sur https://python.org
    echo.
    pause
    exit /b 1
)

ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : ffmpeg non installe ou absent du PATH.
    echo  Telecharge sur https://ffmpeg.org/download.html
    echo.
    pause
    exit /b 1
)

yt-dlp --version >nul 2>&1
if errorlevel 1 (
    echo  ERREUR : yt-dlp non installe ou absent du PATH.
    echo  Lance : pip install yt-dlp
    echo.
    pause
    exit /b 1
)

if not defined ANTHROPIC_API_KEY (
    echo  Cle ANTHROPIC_API_KEY non detectee.
    echo.
    echo  Saisie masquee de la cle Anthropic - caracteres affiches comme * :
    for /f "delims=" %%i in ('powershell -NoProfile -Command "$s = Read-Host -AsSecureString; [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s))"') do set "ANTHROPIC_API_KEY=%%i"
    echo.
    if not defined ANTHROPIC_API_KEY (
        echo  ERREUR : aucune cle API saisie.
        echo.
        pause
        exit /b 1
    )
)

:MENU
echo  Choisis le mode :
echo    1. Analyser une chaine YouTube
echo    2. Analyser une video unique
echo.
set "MODE="
set /p "MODE= Ton choix (1 ou 2) : "

if "%MODE%"=="1" goto MODE_CHANNEL
if "%MODE%"=="2" goto MODE_URL

echo.
echo  ERREUR : choix invalide. Utilise 1 ou 2.
echo.
pause
exit /b 1

:MODE_CHANNEL
echo.
set "CHANNEL="
set /p "CHANNEL= Nom ou URL de la chaine YouTube : "

if "%CHANNEL%"=="" (
    echo.
    echo  ERREUR : aucune chaine saisie.
    echo.
    pause
    exit /b 1
)

echo.
echo  Lancement pour la chaine : "%CHANNEL%"
echo  ====================================================
echo.

py "scripts\agent.py" --channel "%CHANNEL%" --max-videos 200
set "PY_STATUS=%ERRORLEVEL%"
if not "%PY_STATUS%"=="0" (
    echo.
    echo  ====================================================
    echo  ERREUR : le pipeline Python a echoue ^(code %PY_STATUS%^).
    echo  ====================================================
    pause
    exit /b %PY_STATUS%
)
goto END_OK

:MODE_URL
echo.
set "VIDEO_URL="
set /p "VIDEO_URL= URL de la video YouTube : "

if "%VIDEO_URL%"=="" (
    echo.
    echo  ERREUR : aucune URL saisie.
    echo.
    pause
    exit /b 1
)

echo.
echo  Lancement pour la video : "%VIDEO_URL%"
echo  ====================================================
echo.

py "scripts\agent.py" --url "%VIDEO_URL%"
set "PY_STATUS=%ERRORLEVEL%"
if not "%PY_STATUS%"=="0" (
    echo.
    echo  ====================================================
    echo  ERREUR : le pipeline Python a echoue ^(code %PY_STATUS%^).
    echo  ====================================================
    pause
    exit /b %PY_STATUS%
)
goto END_OK

:END_OK
echo.
echo  ====================================================
echo  Termine. Appuie sur une touche pour fermer.
echo  ====================================================
pause >nul
exit /b 0
