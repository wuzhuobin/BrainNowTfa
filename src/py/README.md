# py part

1. install packages and run
```
pip install .
tfa <path>
```
2. directly run
```
python tfa <path>
```
3. pyinstaller
```
cd tfa
pyinstaller -F -n tfa --hidden-import=xlrd --hidden-import=openpyxl __main__.py
./tfa.exe <path>
pyinstaller tfa.spec
```
or
```
pyinstaller tfa.spec
./tfa.exe <path>
```
