import subprocess
import webbrowser
import os


WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "chatgpt": "https://chatgpt.com",
    "linkedin": "https://linkedin.com",
    "reddit": "https://reddit.com",
}


def execute(command):

    command = command.lower()

    if command == "hello":
        print("Hello Sarwar!")
        return

    if command == "how are you":
        print("I'm doing great!")
        return

    if command == "open calculator":
        subprocess.Popen("calc", shell=True)
        return

    if command == "open notepad":
        subprocess.Popen("notepad", shell=True)
        return

    if command == "open chrome":
        subprocess.Popen("start chrome", shell=True)
        return

    if command == "open downloads":
        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
        return

    if command == "open desktop":
        os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
        return

    if command.startswith("open "):

        website = command.replace("open ", "")

        if website in WEBSITES:
            print(f"Opening {website}...")
            webbrowser.open(WEBSITES[website])
            return

    print("Sorry, I don't understand.")