import subprocess
import os

SYSTEM_APPS = {
    "notepad": "notepad",
    "calculator": "calc",
    "calc": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
    "explorer": "explorer",
}


def open_app(app_name):

    app_name = app_name.lower().strip()

    # Google Chrome
    if app_name == "chrome":
        try:
            subprocess.Popen("start chrome", shell=True)
            return True
        except:
            return False

    # VS Code
    if app_name in ["vscode", "vs code", "code"]:
        try:
            subprocess.Popen("code", shell=True)
            return True
        except:
            return False

    # Built-in Windows Apps
    if app_name in SYSTEM_APPS:
        try:
            subprocess.Popen(SYSTEM_APPS[app_name], shell=True)
            return True
        except:
            return False

    return False