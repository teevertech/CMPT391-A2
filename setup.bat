@echo off
REM Exit on error
setlocal enabledelayedexpansion

REM Create virtual environment if not exists
if not exist venv (
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip and install packages
python -m pip install --upgrade pip
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install mlxtend

REM Freeze dependencies
pip freeze > requirements.txt

echo Virtual environment setup complete. Activate it with: run.bat
pause
