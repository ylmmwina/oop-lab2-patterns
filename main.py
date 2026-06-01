from core.db_manager import DBManager

if __name__ == "__main__":
    db1 = DBManager()
    db2 = DBManager()

    # Перевірка роботи Singleton
    if id(db1) == id(db2):
        print("✅ Singleton pattern works: single database connection established!")