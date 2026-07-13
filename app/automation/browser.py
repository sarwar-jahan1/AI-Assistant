import webbrowser


WEBSITES = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "linkedin": "https://linkedin.com",
}


def open_website(name):

    name = name.lower()

    if name in WEBSITES:
        webbrowser.open(WEBSITES[name])
        return True

    return False