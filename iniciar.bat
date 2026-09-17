@echo off

cd /d "%~dp0"
mode con: cols=45 lines=12
python "py/main.py"

pause