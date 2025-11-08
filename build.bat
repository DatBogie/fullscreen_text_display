@echo off
python -m venv .venv
call .\.venv\Scripts\activate.bat
pip3 install -r requirements.txt
pyinstaller -F main.py -n dtext
