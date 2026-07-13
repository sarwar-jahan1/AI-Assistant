AUTOMATION_COMMANDS = [
    "open",
    "close",
    "shutdown",
    "restart",
    "search",
    "play",
    "create",
    "delete",
    "move",
    "copy"
]


class Router:

    def is_automation(self, command):

        command = command.lower()

        for keyword in AUTOMATION_COMMANDS:

            if command.startswith(keyword):
                return True

        return False