import sqlite3


class Memory:

    def __init__(self):
        self.connection = sqlite3.connect("nexa.db")
        self.cursor = self.connection.cursor()

    def save(self, key, value):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO memory(key,value)
            VALUES(?,?)
            """,
            (key, value)
        )

        self.connection.commit()

    def get(self, key):

        self.cursor.execute(
            "SELECT value FROM memory WHERE key=?",
            (key,)
        )

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None