from abc import ABC, abstractmethod

# --- Патерн Composite ---

class QuestionComponent(ABC):
    """Базовий компонент для патерну Composite"""
    @abstractmethod
    def display(self, indent=0):
        pass

class Question(QuestionComponent):
    """Leaf (Листок) - звичайне питання"""
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def get_question_type(self):
        pass

    def display(self, indent=0):
        print(" " * indent + f"[{self.get_question_type().upper()}] {self.text}")

class ChoiceQuestion(Question):
    def __init__(self, text, options):
        super().__init__(text)
        self.options = options

    def get_question_type(self):
        return "choice"

class TextQuestion(Question):
    def get_question_type(self):
        return "text"

class QuestionSection(QuestionComponent):
    """Composite - секція, що містить інші питання або секції"""
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component: QuestionComponent):
        self.children.append(component)

    def display(self, indent=0):
        print(" " * indent + f"=== Section: {self.title} ===")
        for child in self.children:
            child.display(indent + 2)

# --- Патерн Decorator ---

class QuestionDecorator(QuestionComponent):
    """Базовий декоратор"""
    def __init__(self, wrapped: QuestionComponent):
        self.wrapped = wrapped

    def display(self, indent=0):
        self.wrapped.display(indent)

class TimedQuestion(QuestionDecorator):
    """Конкретний декоратор, що додає таймер"""
    def __init__(self, wrapped: QuestionComponent, time_limit: int):
        super().__init__(wrapped)
        self.time_limit = time_limit

    def display(self, indent=0):
        self.wrapped.display(indent)
        print(" " * (indent + 2) + f"⏱ Time limit: {self.time_limit} sec")

# --- Патерн Factory Method ---

class QuestionFactory:
    @staticmethod
    def create_question(q_type, text, **kwargs):
        if q_type == "choice":
            return ChoiceQuestion(text, kwargs.get("options", []))
        elif q_type == "text":
            return TextQuestion(text)
        else:
            raise ValueError(f"Unknown question type: {q_type}")