@echo off
setlocal

set "BATCH_PATH=%~dp0"
set "VSCODE_USER=%APPDATA%\Code\User"

python -m pip install -r "%BATCH_PATH%requirements.txt"

python "%BATCH_PATH%sync_filter.py" ^
    "%VSCODE_USER%\settings.json" ^
    "%BATCH_PATH%config\settings.json"

copy /Y ^
    "%VSCODE_USER%\keybindings.json" ^
    "%BATCH_PATH%config\keybindings.json"

endlocal

