@ECHO OFF
REM BFCPEOPTIONSTART
REM Advanced BAT to EXE Converter www.BatToExeConverter.com
REM BFCPEEXE=D:\misDocs\2023\GENERALIZACION\SKEL\polyskel\Silence.exe
REM BFCPEICON=
REM BFCPEICONINDEX=-1
REM BFCPEEMBEDDISPLAY=0
REM BFCPEEMBEDDELETE=1
REM BFCPEADMINEXE=0
REM BFCPEINVISEXE=0
REM BFCPEVERINCLUDE=0
REM BFCPEVERVERSION=1.0.0.0
REM BFCPEVERPRODUCT=Product Name
REM BFCPEVERDESC=Product Description
REM BFCPEVERCOMPANY=Your Company
REM BFCPEVERCOPYRIGHT=Copyright Info
REM BFCPEOPTIONEND
@ECHO ON
@echo off
mode con:cols=80 lines=25
REM ADVANCED batch file: LaunchSilent example
rem Launches NotePad completely silent in the backround
rem with no options and do not wait for it to finish
rem before exiting. Close with Task Manager.
rem 
rem Some applications may open a second dialog that
rem will not remain hidden. Use the HideWindow
rem extended command example to solve this problem.
echo: Launching Notepad in backround...
rem LaunchSilent notepad.exe "" 0
cls
