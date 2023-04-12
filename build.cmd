pyinstaller main.spec 
del releases\beamin_launcher.exe /q
xcopy .\dist\beamin_launcher.exe releases
rmdir /s/q .\dist 
rmdir /s/q .\build
pause