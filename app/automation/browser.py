import webbrowser
from urllib.parse import quote

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "linkedin": "https://www.linkedin.com",
    "chatgpt": "https://chatgpt.com",
}


def open_website(name):

    name = name.lower().strip()

    if name in WEBSITES:
        webbrowser.open(WEBSITES[name])
        return True

    return False


def google_search(query):

    url = f"https://www.google.com/search?q={quote(query)}"

    webbrowser.open(url)

    return True


def youtube_search(query):

    url = f"https://www.youtube.com/results?search_query={quote(query)}"

    webbrowser.open(url)

    return True