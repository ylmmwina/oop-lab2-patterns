from abc import ABC, abstractmethod


class Command(ABC):
    """
    @brief Базовий інтерфейс команди.

    Дозволяє інкапсулювати дію користувача як окремий об'єкт.

    Патерн: Command.
    """

    @abstractmethod
    def execute(self) -> None:
        """
        @brief Виконує команду.
        """
        pass

    @abstractmethod
    def undo(self) -> None:
        """
        @brief Скасовує команду.
        """
        pass


class AnswerCommand(Command):
    """
    @brief Команда відповіді на питання.

    Зберігає відповідь користувача та підтримує скасування.
    """

    def __init__(self, question_text: str, answer_text: str, answers_list: list[str]):
        """
        @brief Ініціалізує команду відповіді.
        @param question_text Текст питання.
        @param answer_text Текст відповіді.
        @param answers_list Список відповідей, який змінює команда.
        """
        self.question = question_text
        self.answer = answer_text
        self.answers_list = answers_list

    def execute(self) -> None:
        """
        @brief Додає відповідь до списку.
        """
        self.answers_list.append(self.answer)

    def undo(self) -> None:
        """
        @brief Видаляє останню додану відповідь.
        """
        if self.answers_list:
            self.answers_list.pop()