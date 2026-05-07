@echo off
setlocal

REM Get current folder
set "CURRENT_DIR=%~dp0"

REM Remove trailing backslash
if "%CURRENT_DIR:~-1%"=="\" set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

REM dist folder
set "TARGET=%CURRENT_DIR%\dist"

echo Adding:
echo %TARGET%
echo.

REM Add to user PATH
setx PATH "%PATH%;%TARGET%"

echo.
echo Done!
echo Restart your terminal for changes to take effect.

pause