@echo off
:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing Python...
    powershell -Command "& { (New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe', 'python-installer.exe') }"
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
    echo Python has been installed. Please restart the script to continue.
    exit /b
)
cls
:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
cls
:: Install Pillow
echo Installing Pillow...
pip install pillow
cls
:: Install PyAutoGUI
echo Installing PyAutoGUI...
pip install pyautogui
cls
:: Prompt user to open slideshow in presentation mode
echo Make sure you open the slideshow to presentation mode in the next 15 seconds!
timeout /t 15 >nul
:: Run main.py
echo Running main.py...
python main.py
cls
echo Program terminated!
pause
