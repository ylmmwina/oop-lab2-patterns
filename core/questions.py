from abc import ABC, abstractmethod


class QuestionComponent(ABC):
    """
    @brief Базовий компонент для патерну Composite.

    Дозволяє однаково працювати як з окремими питаннями,
    так і з групами питань.
    """

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """
        @brief Виводить компонент питання.
        @param indent Кількість пробілів для відступу.
        """
        pass


class Question(QuestionComponent):
    """
    @brief Абстрактний базовий клас питання.

    Представляє листовий елемент у патерні Composite.
    """

    def __init__(self, text: str):
        """
        @brief Ініціалізує питання.
        @param text Текст питання.
        """
        self.text = text

    @abstractmethod
    def get_question_type(self) -> str:
        """
        @brief Повертає тип питання.
        @return Рядок з типом питання.
        """
        pass

    def display(self, indent: int = 0) -> None:
        """
        @brief Виводить питання у консоль.
        @param indent Кількість пробілів для відступу.
        """
        print(" " * indent + f"[{self.get_question_type().upper()}] {self.text}")


class ChoiceQuestion(Question):
    """
    @brief Питання з варіантами відповіді.

    Використовується для тестових питань із вибором одного
    або кількох варіантів.
    """

    def __init__(self, text: str, options: list[str]):
        """
        @brief Ініціалізує питання з варіантами відповіді.
        @param text Текст питання.
        @param options Список варіантів відповіді.
        """
        super().__init__(text)
        self.options = options

    def get_question_type(self) -> str:
        """
        @brief Повертає тип питання.
        @return Тип питання choice.
        """
        return "choice"


class TextQuestion(Question):
    """
    @brief Питання з відповіддю у вільній формі.
    """

    def get_question_type(self) -> str:
        """
        @brief Повертає тип питання.
        @return Тип питання text.
        """
        return "text"


class QuestionSection(QuestionComponent):
    """
    @brief Група питань для патерну Composite.

    Секція може містити окремі питання або інші секції.
    """

    def __init__(self, title: str):
        """
        @brief Ініціалізує секцію питань.
        @param title Назва секції.
        """
        self.title = title
        self.children: list[QuestionComponent] = []

    def add(self, component: QuestionComponent) -> None:
        """
        @brief Додає питання або вкладену секцію.
        @param component Компонент, який треба додати.
        """
        self.children.append(component)

    def display(self, indent: int = 0) -> None:
        """
        @brief Виводить секцію та всі її дочірні компоненти.
        @param indent Кількість пробілів для відступу.
        """
        print(" " * indent + f"=== Section: {self.title} ===")
        for child in self.children:
            child.display(indent + 2)


class QuestionDecorator(QuestionComponent):
    """
    @brief Базовий декоратор для питань.

    Дозволяє додавати нову поведінку до питання без зміни
    його основного класу.

    Патерн: Decorator.
    """

    def __init__(self, wrapped: QuestionComponent):
        """
        @brief Ініціалізує декоратор.
        @param wrapped Компонент, який обгортається декоратором.
        """
        self.wrapped = wrapped

    def display(self, indent: int = 0) -> None:
        """
        @brief Делегує виведення обгорнутому компоненту.
        @param indent Кількість пробілів для відступу.
        """
        self.wrapped.display(indent)


class TimedQuestion(QuestionDecorator):
    """
    @brief Декоратор, який додає часове обмеження до питання.
    """

    def __init__(self, wrapped: QuestionComponent, time_limit: int):
        """
        @brief Ініціалізує питання з часовим обмеженням.
        @param wrapped Обгорнуте питання або секція.
        @param time_limit Ліміт часу в секундах.
        """
        super().__init__(wrapped)
        self.time_limit = time_limit

    def display(self, indent: int = 0) -> None:
        """
        @brief Виводить питання та його часове обмеження.
        @param indent Кількість пробілів для відступу.
        """
        self.wrapped.display(indent)
        print(" " * (indent + 2) + f"Time limit: {self.time_limit} sec")


class QuestionFactory:
    """
    @brief Фабрика для створення питань.

    Створює різні типи питань за текстовим ідентифікатором.

    Патерн: Factory Method.
    """

    @staticmethod
    def create_question(q_type: str, text: str, **kwargs) -> Question:
        """
        @brief Створює питання потрібного типу.
        @param q_type Тип питання.
        @param text Текст питання.
        @param kwargs Додаткові параметри питання.
        @return Об'єкт питання.
        @throws ValueError Якщо тип питання невідомий.
        """
        if q_type == "choice":
            return ChoiceQuestion(text, kwargs.get("options", []))

        if q_type == "text":
            return TextQuestion(text)

        raise ValueError(f"Unknown question type: {q_type}")