from abc import ABC, abstractmethod

class Observer(ABC):
    """Базовий клас для підписників"""
    @abstractmethod
    def update(self, message):
        pass

class Subject:
    """Об'єкт, за яким спостерігають (наприклад, сесія тесту)"""
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class ProgressTracker(Observer):
    """Конкретний спостерігач, який слідкує за прогресом"""
    def update(self, message):
        print(f"[Tracker] Update received: {message}")