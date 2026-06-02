import os
import sqlite3


class DBManager:
    """
    @brief Singleton для роботи з SQLite-базою даних.

    Клас відповідає за створення єдиного підключення до бази даних
    та виконання SQL-запитів.

    Патерн: Singleton.
    """

    _instance = None

    def __new__(cls, db_name: str = "edu_system.db"):
        """
        @brief Створює або повертає єдиний екземпляр DBManager.
        @param db_name Назва SQLite-файлу бази даних.
        @return Єдиний екземпляр DBManager.
        """
        if cls._instance is None:
            cls._instance = super(DBManager, cls).__new__(cls)

            db_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "..",
                db_name,
            )

            cls._instance.connection = sqlite3.connect(db_path)
            cls._instance.cursor = cls._instance.connection.cursor()
            cls._instance._initialize_db()

        return cls._instance

    def _initialize_db(self) -> None:
        """
        @brief Створює таблиці бази даних, якщо вони ще не існують.
        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                max_score INTEGER NOT NULL
            )
            """
        )
        self.connection.commit()

    def execute_query(self, query: str, params: tuple = ()):
        """
        @brief Виконує SQL-запит, який змінює дані.
        @param query SQL-запит.
        @param params Параметри SQL-запиту.
        @return SQLite cursor після виконання запиту.
        """
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetch_all(self, query: str, params: tuple = ()):
        """
        @brief Виконує SELECT-запит і повертає всі результати.
        @param query SQL SELECT-запит.
        @param params Параметри SQL-запиту.
        @return Список рядків результату.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()