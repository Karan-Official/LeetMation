import os
import subprocess
import json
import shutil
from pathlib import Path
import ctypes

# Creates hidden folder for windows
def create_hidden_folder():
    appdata_path = os.path.join(os.environ['LOCALAPPDATA'], "LeetMation")
    if not os.path.exists(appdata_path):
        os.makedirs(appdata_path)
        print(f"Folder 'LeetMation' created")
        subprocess.run(["attrib", "+H", appdata_path], check=True, shell=True)  # Hide on Windows
    return appdata_path

# Function to save credentials
def save_credentials(appdata_path):
    credentials_path = os.path.join(appdata_path, "credentials.json")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    credentials = {"username": username, "password": password}
    try:
        with open(credentials_path, "w") as f:
            json.dump(credentials, f)
        print("Credentials saved successfully.")
        current_path = os.path.join(os.getcwd(), "credentials.json")
        if os.path.exists(current_path):
            os.remove(current_path)
    except Exception as e:
        print(f"Failed to save credentials: {e}")

# Move Files to the hidden folder created
def move_files(appdata_path):
    file_list = ["reLogin.py", "leetcodeProblemAutomation.py", "leetcodeDailyAutomation.py", "cookies.json"]
    try:
        if not os.path.exists(appdata_path):
            os.makedirs(appdata_path)
        for file in file_list:
            source_path = os.path.join(os.getcwd(), file)
            if os.path.exists(source_path):
                shutil.move(source_path, os.path.join(appdata_path, file))
                print(f"Moved {file} to {appdata_path}")
            else:
                print(f"File {file} not found in the current directory.")
    except Exception as e:
        print(f"Failed to move files: {e}")

# Get the desktop path for windows and mac
def get_desktop_path():
    CSIDL_DESKTOP = 0  # CSIDL for Desktop
    SHGFP_TYPE_CURRENT = 0
    buf = ctypes.create_unicode_buffer(260)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, SHGFP_TYPE_CURRENT, buf)
    return buf.value

# Create a .bat or .sh file to run the automation
def create_executable(appdata_path):
    desktop_path = get_desktop_path()

    script_path = os.path.join(desktop_path, "LeetMation")

    script_path += ".bat"
    bat_content = f"""@echo off
setlocal enabledelayedexpansion
echo =============================================================================================================
echo    _        ______    ______    _______    __  __               _______    ______      _____     __    __  
echo   ^| ^|      ^|  ____^|  ^|  ____^|  ^|__   __^|  ^|  \/  ^|      /\     ^|__   __^|  ^|______^|    /     \   ^|  \  ^|  ^| 
echo   ^| ^|      ^| ^|___    ^| ^|___       ^| ^|     ^| ^|\/^| ^|     /  \       ^| ^|        ^|^|      ^|       ^|  ^|   \_^|  ^| 
echo   ^| ^|      ^|  ___^|   ^|  ___^|      ^| ^|     ^| ^|  ^| ^|    / /\ \      ^| ^|        ^|^|      ^|       ^|  ^|   _    ^| 
echo   ^| ^|____  ^| ^|____   ^| ^|____      ^| ^|     ^| ^|  ^| ^|   / ____ \     ^| ^|      __^|^|__    ^|       ^|  ^|  ^| \   ^|
echo   ^|______^| ^|______^|  ^|______^|     ^|_^|     ^|_^|  ^|_^|  /_/    \_\    ^|_^|     ^|______^|    \_____/   ^|__^|  \__^| 
echo.
echo                                      - By Karan Prajapati
echo =============================================================================================================
echo.
echo Note: If the submission fails once or twice, please try again. If the issue persists, feel free to contact us. This may be due to an internal error or a network-related problem.
echo.
echo Guidelines: Read ReadME.md file on my Github Page - https://github.com/Karan-Official/LeetMation
echo.
echo Select an option:
echo 1. Solve Daily Problem
echo 2. Solve Problem by ID
set /p choice=Enter your choice: 
if "%choice%"=="1" (
    python "{os.path.join(appdata_path, 'leetcodeDailyAutomation.py').replace("\\", "\\\\")}"
) else if "%choice%"=="2" (
    set /p problem_id=Enter problem ID: 
    python "{os.path.join(appdata_path, 'leetcodeProblemAutomation.py').replace("\\", "\\\\")}" "!problem_id!"
) else (
    echo Invalid choice!
)
rmdir /s /q "%CD%\\downloaded_files"
pause
"""
    
    try:
        # Ensure the Desktop path exists
        os.makedirs(os.path.dirname(script_path), exist_ok=True)

        with open(script_path, "w") as f:
            f.write(bat_content)
        
        print(f"Executable created at: {script_path}")

    except Exception as e:
        print(f"Failed to create executable: {e}")

def main():
    address = create_hidden_folder()
    save_credentials(address)
    move_files(address)
    create_executable(address)

main()