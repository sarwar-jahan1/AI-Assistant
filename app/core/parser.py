class CommandParser:

    def parse(self, text):

        text = text.lower().strip()

        prefixes = [
            "please ",
            "can you ",
            "could you ",
            "jarvis ",
        ]

        for prefix in prefixes:
            if text.startswith(prefix):
                text = text[len(prefix):]

        return text