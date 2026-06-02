class SessionMemento:
    """
    @brief Знімок стану тестової сесії.

    Зберігає поточний номер питання та список відповідей.

    Патерн: Memento.
    """

    def __init__(self, current_index: int, answers: list[str]):
        """
        @brief Ініціалізує знімок стану.
        @param current_index Поточний індекс питання.
        @param answers Список відповідей.
        """
        self.current_index = current_index
        self.answers = list(answers)


class ExamSession:
    """
    @brief Об'єкт, стан якого можна зберігати та відновлювати.
    """

    def __init__(self):
        """
        @brief Ініціалізує порожню тестову сесію.
        """
        self.current_index = 0
        self.answers: list[str] = []

    def answer(self, answer_text: str) -> None:
        """
        @brief Додає відповідь і переходить до наступного питання.
        @param answer_text Текст відповіді.
        """
        self.answers.append(answer_text)
        self.current_index += 1

    def save(self) -> SessionMemento:
        """
        @brief Зберігає поточний стан сесії.
        @return Об'єкт-знімок SessionMemento.
        """
        return SessionMemento(self.current_index, self.answers)

    def restore(self, memento: SessionMemento) -> None:
        """
        @brief Відновлює стан сесії зі знімка.
        @param memento Збережений знімок стану.
        """
        self.current_index = memento.current_index
        self.answers = list(memento.answers)


class SessionCaretaker:
    """
    @brief Клас, який зберігає історію знімків сесії.
    """

    def __init__(self):
        """
        @brief Ініціалізує порожню історію знімків.
        """
        self.history: list[SessionMemento] = []

    def backup(self, memento: SessionMemento) -> None:
        """
        @brief Додає знімок до історії.
        @param memento Знімок стану.
        """
        self.history.append(memento)

    def undo(self) -> SessionMemento | None:
        """
        @brief Повертає останній знімок зі стеку історії.
        @return Останній знімок або None.
        """
        if not self.history:
            return None

        return self.history.pop()