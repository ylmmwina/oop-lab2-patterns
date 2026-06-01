from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def get_question_type(self):
        pass

class ChoiceQuestion(Question):
    def __init__(self, text, options):
        super().__init__(text)
        self.options = options

    def get_question_type(self):
        return "choice"

class TextQuestion(Question):
    def get_question_type(self):
        return "text"

class QuestionFactory:
    """Factory Method pattern for creating different types of questions."""
    @staticmethod
    def create_question(q_type, text, **kwargs):
        if q_type == "choice":
            return ChoiceQuestion(text, kwargs.get("options", []))
        elif q_type == "text":
            return TextQuestion(text)
        else:
            raise ValueError(f"Unknown question type: {q_type}")