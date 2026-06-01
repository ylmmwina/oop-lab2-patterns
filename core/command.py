from abc import ABC, abstractmethod

class Command(ABC):
    """Базова команда"""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class AnswerCommand(Command):
    """Команда для збереження відповіді користувача з можливістю скасування"""
    def __init__(self, question_text, answer_text, answers_list):
        self.question = question_text
        self.answer = answer_text
        self.answers_list = answers_list

    def execute(self):
        self.answers_list.append(self.answer)
        print(f"Action: Answered '{self.answer}' to '{self.question}'")

    def undo(self):
        if self.answers_list:
            removed = self.answers_list.pop()
            print(f"Action: Undo answer '{removed}'")