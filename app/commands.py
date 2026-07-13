from automation.apps import open_app
from automation.browser import open_website
from automation.system import open_desktop, open_downloads


def execute(command):

    command = command.lower().strip()

    if command.startswith("open "):

        item = command[5:].strip()

        if item == "desktop":
            open_desktop()
            return

        if item == "downloads":
            open_downloads()
            return

        if open_app(item):
            print(f"Opening {item}...")
            return

        if open_website(item):
            print(f"Opening {item}...")
            return

        print(f"'{item}' was not found.")
        return

    print("Unknown command.")