from automation.apps import open_app
from automation.browser import (
    open_website,
    google_search,
    youtube_search,
)
from automation.system import (
    open_desktop,
    open_downloads,
    take_screenshot,
    get_cpu,
    get_ram,
    get_disk,
    get_battery,
)
from automation.files import (
    create_folder,
    create_file,
    delete_file,
    delete_folder,
    list_files,
    open_file,
)


def execute(command):

    command = command.strip().lower()

    # ---------------- SYSTEM INFO ----------------

    if command == "cpu":
        print(get_cpu())
        return

    if command == "ram":
        print(get_ram())
        return

    if command == "disk":
        print(get_disk())
        return

    if command == "battery":
        print(get_battery())
        return

    # ---------------- SCREENSHOT ----------------

    if command == "take screenshot":

        path = take_screenshot()

        print(f"Screenshot saved at:\n{path}")

        return

    # ---------------- GOOGLE SEARCH ----------------

    if command.startswith("search "):

        query = command.replace("search ", "").strip()

        google_search(query)

        print(f"Searching Google: {query}")

        return

    # ---------------- YOUTUBE SEARCH ----------------

    if command.startswith("youtube "):

        query = command.replace("youtube ", "").strip()

        youtube_search(query)

        print(f"Searching YouTube: {query}")

        return

    # ---------------- LIST FILES ----------------

    if command.startswith("list files"):

        if " in " in command:

            location = command.split(" in ", 1)[1]

        else:

            location = "current"

        files = list_files(location)

        if files:

            print("\nFiles:\n")

            for file in files:
                print(file)

        else:

            print("No files found.")

        return

    # ---------------- OPEN FILE ----------------

    if command.startswith("open file "):

        path = command.replace("open file ", "").strip()

        if open_file(path):
            print("Opening file...")
        else:
            print("File not found.")

        return

    # ---------------- OPEN ----------------

    if command.startswith("open "):

        item = command.replace("open ", "").strip()

        if item == "desktop":
            open_desktop()
            return

        if item == "downloads":
            open_downloads()
            return

        if open_app(item):
            print(f"Opening {item}")
            return

        if open_website(item):
            print(f"Opening {item}")
            return

        print("Not Found")
        return

    # ---------------- CREATE FOLDER ----------------

    if command.startswith("create folder "):

        text = command.replace("create folder ", "")

        if " in " in text:
            folder, location = text.split(" in ", 1)
        else:
            folder = text
            location = "current"

        path = create_folder(folder.strip(), location.strip())

        if path:
            print(f"Folder created:\n{path}")
        else:
            print("Failed to create folder.")

        return

    # ---------------- CREATE FILE ----------------

    if command.startswith("create file "):

        text = command.replace("create file ", "")

        if " in " in text:
            filename, location = text.split(" in ", 1)
        else:
            filename = text
            location = "current"

        path = create_file(filename.strip(), location.strip())

        if path:
            print(f"File created:\n{path}")
        else:
            print("Failed to create file.")

        return

    # ---------------- DELETE FILE ----------------

    if command.startswith("delete file "):

        text = command.replace("delete file ", "")

        if " in " in text:
            filename, location = text.split(" in ", 1)
        else:
            filename = text
            location = "current"

        if delete_file(filename.strip(), location.strip()):
            print("File deleted.")
        else:
            print("File not found.")

        return

    # ---------------- DELETE FOLDER ----------------

    if command.startswith("delete folder "):

        text = command.replace("delete folder ", "")

        if " in " in text:
            folder, location = text.split(" in ", 1)
        else:
            folder = text
            location = "current"

        if delete_folder(folder.strip(), location.strip()):
            print("Folder deleted.")
        else:
            print("Folder not found.")

        return

    print("Unknown Command")