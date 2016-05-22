@echo off
hello.exe
if errorlevel 1 goto err
if errorlevel 0 goto ok
goto fin
:err
echo ERROR!
goto fin
:ok
echo OK
:fin
