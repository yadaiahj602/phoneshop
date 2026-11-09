@echo off
cd /d "%~dp0"

echo Installing Phone Shop...

python -m venv venv

call venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

echo.
echo Phone Shop setup completed!
pause