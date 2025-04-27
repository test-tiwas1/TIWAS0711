@echo off
echo -------------------------------------
echo Installation et lancement de TIWAS
echo -------------------------------------
echo.

REM Vérifie si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé sur ce système.
    echo Merci de l'installer manuellement depuis https://www.python.org/downloads/
    pause
    exit /b
)

REM Création d'un environnement virtuel
python -m venv tiwas_env
call tiwas_env\\Scripts\\activate

REM Mise à jour de pip
python -m pip install --upgrade pip

REM Installation des dépendances
pip install -r requirements.txt

REM Lancement de l'application
streamlit run app.py

pause
