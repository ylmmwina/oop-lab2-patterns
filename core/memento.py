class TestMemento:
    """Зберігач: незмінний об'єкт, що містить стан сесії"""
    def __init__(self, current_index, answers):
        self.current_index = current_index
        self.answers = list(answers)  # Робимо копію списку

class TestSessionOriginator:
    """Творець: об'єкт, стан якого ми зберігаємо і відновлюємо"""
    def __init__(self):
        self.current_index = 0
        self.answers = []

    def answer(self, ans):
        self.answers.append(ans)
        self.current_index += 1
        print(f"-> Question {self.current_index} answered: {ans}")

    def save(self) -> TestMemento:
        print("💾 Progress saved.")
        return TestMemento(self.current_index, self.answers)

    def restore(self, memento: TestMemento):
        self.current_index = memento.current_index
        self.answers = list(memento.answers)
        print("🔄 Progress restored.")

class SessionCaretaker:
    """Опікун: керує збереженими станами (наприклад, зберігає їх у список)"""
    def __init__(self):
        self.history = []

    def backup(self, memento: TestMemento):
        self.history.append(memento)

    def undo(self) -> TestMemento:
        if not self.history:
            return None
        return self.history.pop()