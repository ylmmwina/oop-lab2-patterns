from core.observer import Subject, ProgressTracker
from core.command import AnswerCommand

if __name__ == "__main__":
    # --- Перевірка Observer ---
    test_session = Subject()
    tracker = ProgressTracker()
    test_session.attach(tracker)  # Підписуємо трекер на події сесії

    print("✅ Pattern Observer works:")
    test_session.notify("Test Session Started.")

    # --- Перевірка Command ---
    print("\n✅ Pattern Command works:")
    user_answers = []

    # Створюємо команду відповіді
    cmd1 = AnswerCommand("What is 2+2?", "4", user_answers)

    # Виконуємо і сповіщаємо спостерігачів
    cmd1.execute()
    test_session.notify(f"Answers submitted: {len(user_answers)}")

    # Скасовуємо (Undo) і сповіщаємо спостерігачів
    cmd1.undo()
    test_session.notify(f"Answers submitted after undo: {len(user_answers)}")