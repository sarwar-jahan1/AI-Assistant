class Planner:

    def split_tasks(self, command):

        command = command.lower()

        separators = [
            " and ",
            " then ",
            ","
        ]

        tasks = [command]

        for separator in separators:

            new_tasks = []

            for task in tasks:

                if separator in task:

                    new_tasks.extend(task.split(separator))

                else:

                    new_tasks.append(task)

            tasks = new_tasks

        return [task.strip() for task in tasks if task.strip()]