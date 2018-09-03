@echo off
echo =============================
echo        package program
echo =============================
pyinstaller -i server.ico -F .\server\ae_server.py
pyinstaller -i server.ico -F .\server\Startup.py
echo.
echo.

echo =============================
echo         copy program
echo =============================
copy .\dist\ae_server.exe .\Release\package /y
echo.
echo.

echo =============================
echo          zip program
echo =============================
for /f %%t in ('.\Release\package\ae_server.exe --version') do set version=%%t
rm .\Release\%version%.zip
.\7-Zip\7z.exe a .\Release\%version%.zip .\Release\package\*
echo.
echo.

echo =============================
echo           upload
echo =============================
echo %version%.zip
rm \\192.168.0.140\忆球工具\自动化剪辑工具\剪辑服务器\升级包\%version%.zip
copy .\Release\%version%.zip \\192.168.0.140\忆球工具\自动化剪辑工具\剪辑服务器\升级包 /y
pause
