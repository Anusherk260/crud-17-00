import sqlite3


def connect(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor # (connection, cursor)


class Connection:
    def __init__(self, db_name):
        self.connection, self.cursor = connect(db_name)
