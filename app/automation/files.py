import os
import shutil
from pathlib import Path

HOME = Path.home()

LOCATIONS = {
    "desktop": HOME / "OneDrive" / "Desktop",
    "downloads": HOME / "Downloads",
    "documents": HOME / "Documents",
}

if not LOCATIONS["desktop"].exists():
    LOCATIONS["desktop"] = HOME / "Desktop"


def get_path(location):

    location = location.strip()

    if location.lower() in LOCATIONS:
        return LOCATIONS[location.lower()]

    custom = Path(location)

    if custom.exists():
        return custom

    return Path.cwd()


def create_folder(name, location="current"):

    path = get_path(location) / name
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def create_file(name, location="current"):

    path = get_path(location) / name
    path.touch(exist_ok=True)
    return str(path)


def delete_folder(name, location="current"):

    path = get_path(location) / name

    if path.exists():
        shutil.rmtree(path)
        return True

    return False


def delete_file(name, location="current"):

    path = get_path(location) / name

    if path.exists():
        path.unlink()
        return True

    return False


def list_files(location="current"):

    path = get_path(location)

    if not path.exists():
        return []

    return [file.name for file in path.iterdir()]


def open_file(path):

    try:
        os.startfile(path)
        return True
    except:
        return False