pyinstaller -F main.py -n CardPrintAssistance -w
rm CardPrintAssistance.exe
rm CardPrintAssistance.spec
rm main.spec
mv ./dist/CardPrintAssistance.exe ./
rm ./dist
rmdir ./build -Recurse -Force
