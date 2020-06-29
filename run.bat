@echo off
echo "Opening Mumu..."

set myvar=1
for /f %%i in ('tasklist^|findstr NemuPlayer')do set myvar=%%i
if not %myvar%==1 (goto 1)

:: Starting Mumu
start "1" /min "D:\Program Files (x86)\MuMu\emulator\nemu\EmulatorShell\NemuPlayer.exe"
timeout /t 30

:1
echo "Mumu opened"
adb connect 127.0.0.1:7555
CALL conda.bat activate base
cd /D D:\Work\Code\fgo\auto\
echo %cd%
python ".\main.py" -fgo

echo "Jobs done, closing Mumu..."
timeout /t 10
taskkill /IM NemuPlayer.exe /F
taskkill /IM NemuHeadless.exe /F
taskkill /IM NemuSVC.exe /F
taskkill /IM NemuService.exe /F



