from database.db import connect


class DBTableCreator:
    def __init__(self):
        self.connection, self.cursor = connect('../todos.db')

    def create_users_table(self):
        sql = """
        DROP TABLE IF EXISTS user;
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE
        );
        """

        self.cursor.executescript(sql)
        self.connection.commit()

    def create_todos_table(self):
        sql = """
            DROP TABLE IF EXISTS todos;
            CREATE TABLE IF NOT EXISTS TODOS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE,
                description TEXT,
                user_id INTEGER REFERENCES users(id),
                created_at TEXT,
                is_finished BOOLEAN
            
            
            );
        """
        self.cursor.executescript(sql)
        self.connection.commit()


creator = DBTableCreator()
creator.create_users_table()
creator.create_todos_table()
creator.connection.close()