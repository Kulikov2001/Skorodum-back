@echo off
echo User %USERNAME% on computer %COMPUTERNAME%>"%TEMP%\ipconfig.txt"
%SystemRoot%\System32\ipconfig.exe | findstr /i "IPv4">>"%TEMP%\ipconfig.txt"
type "%TEMP%\ipconfig.txt"
echo.
del "%TEMP%\ipconfig.txt"
pause