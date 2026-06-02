from abc import ABC, abstractmethod


class Observer(ABC):
    """
    @brief Базовий інтерфейс спостерігача.

    Патерн: Observer.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        @brief Отримує повідомлення від суб'єкта.
        @param message Текст повідомлення.
        """
        pass


class Subject:
    """
    @brief Суб'єкт, за яким можуть спостерігати інші об'єкти.
    """

    def __init__(self):
        """
        @brief Ініціалізує список спостерігачів.
        """
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        @brief Додає спостерігача.
        @param observer Об'єкт-спостерігач.
        """
        self._observers.append(observer)

    def notify(self, message: str) -> None:
        """
        @brief Повідомляє всіх спостерігачів.
        @param message Текст повідомлення.
        """
        for observer in self._observers:
            observer.update(message)


class ProgressTracker(Observer):
    """
    @brief Спостерігач, який зберігає повідомлення про прогрес.
    """

    def __init__(self):
        """
        @brief Ініціалізує порожній список повідомлень.
        """
        self.messages: list[str] = []

    def update(self, message: str) -> None:
        """
        @brief Зберігає отримане повідомлення.
        @param message Текст повідомлення.
        """
        self.messages.append(message)