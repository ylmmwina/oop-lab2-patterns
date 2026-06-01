from core.memento import TestSessionOriginator, SessionCaretaker

if __name__ == "__main__":
    print("--- Pattern Memento Testing ---")
    session = TestSessionOriginator()
    caretaker = SessionCaretaker()

    # Студент починає тест
    session.answer("Python")
    session.answer("Encapsulation")

    # Студент вирішив зробити перерву і зберігає прогрес
    caretaker.backup(session.save())

    # Студент відповідає далі, але раптом вимикається світло (або він відповідає неправильно)
    session.answer("Wrong answer")
    print(f"Current answers before restore: {session.answers}")

    # Відновлюємо стан з бекапу
    last_save = caretaker.undo()
    if last_save:
        session.restore(last_save)

    print(f"Current answers after restore: {session.answers}")
    print("✅ Pattern Memento works: State successfully saved and restored!")