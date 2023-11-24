@ECHO OFF
REM BFCPEOPTIONSTART
REM Advanced BAT to EXE Converter www.BatToExeConverter.com
REM BFCPEEXE=
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
@ECHO OFF

py -m ensurepip --default-pip
py -m pip install --upgrade pip setuptools wheel
py -m pip install Django
pip install euclid3
pip install Pillow
pip install fiona
pip install psycopg2
pip install unidecode
pip install shapefile


cls
cd  /d D:\misDocs\2023\GENERALIZACION\inegi 
start "GENERALIZACION" /WAIT /B /HIGH py manage.py runserver
start "SISTEMA WEB" /HIGH chrome http://127.0.0.1:8000/dicc --window-size=1100,800

pause
