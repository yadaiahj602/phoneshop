@echo off
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Please run setup.bat first.
    pause
    exit /b
)

echo Starting Phone Shop...

start "Phone Shop Server" /min "%~dp0venv\Scripts\python.exe" "%~dp0manage.py" runserver 127.0.0.1:8000

timeout /t 4 /nobreak >nul

start "" "http://127.0.0.1:8000/products/index/"

exit