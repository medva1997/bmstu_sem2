@echo off
palindrome.exe < in_%1.txt > Out.txt
fc out.txt out_%1.txt
pause