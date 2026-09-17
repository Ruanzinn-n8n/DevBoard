@echo off

cd /d "%~dp0"
mode con: cols=90 lines=25
python "py/main.py"

pause