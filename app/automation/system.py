import os
from pathlib import Path
import pyautogui
import psutil

HOME = Path.home()

DESKTOP = HOME / "OneDrive" / "Desktop"

if not DESKTOP.exists():
    DESKTOP = HOME / "Desktop"


def open_desktop():
    os.startfile(DESKTOP)


def open_downloads():
    os.startfile(HOME / "Downloads")


def take_screenshot():

    screenshot = pyautogui.screenshot()

    path = DESKTOP / "screenshot.png"

    screenshot.save(path)

    return str(path)


def get_cpu():

    return f"CPU Usage : {psutil.cpu_percent(interval=1)}%"


def get_ram():

    ram = psutil.virtual_memory()

    return f"RAM Usage : {ram.percent}% ({round(ram.used/1024**3,2)} GB / {round(ram.total/1024**3,2)} GB)"


def get_disk():

    disk = psutil.disk_usage("/")

    return f"Disk Usage : {disk.percent}%"


def get_battery():

    battery = psutil.sensors_battery()

    if battery:

        return f"Battery : {battery.percent}%"

    return "Battery information unavailable."