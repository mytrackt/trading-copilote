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
python --version >nul 2>&1
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

:: Cle API
if "%ANTHROPIC_API_KEY%"=="" (
    echo  Cle ANTHROPIC_API_KEY non detectee.
    echo.
    set /p "APIKEY= Entre ta cle API Anthropic (sk-ant-...) : "
    set ANTHROPIC_API_KEY=%APIKEY%
    echo.
)

:: Nom de la chaine
echo  Exemples : ICT Trading, Belkhayate, Anton Kreil
echo.
set /p "CHANNEL= Entre le nom de la chaine YouTube : "

if "%CHANNEL%"=="" (
    echo  Aucun nom saisi. Fermeture.
    pause
    exit /b 0
)

echo.
echo  Lancement pour : %CHANNEL%
echo  ====================================================
echo.

cd /d "C:\trading-copilote"
python scripts\agent.py "%CHANNEL%"

echo.
echo  ====================================================
echo  Termine. Appuie sur une touche pour fermer.
echo  ====================================================
pause >nul
