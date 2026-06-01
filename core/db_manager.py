import sqlite3
import os

class DBManager:
    _instance = None

    def __new__(cls, db_name="edu_system.db"):
        if cls._instance is None:
            cls._instance = super(DBManager, cls).__new__(cls)
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', db_name)
            cls._instance.connection = sqlite3.connect(db_path)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance._initialize_db()
        return cls._instance

    def _initialize_db(self):
        # Базова таблиця для зберігання тестів
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                max_score INTEGER
            )
        ''')
        self.connection.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()