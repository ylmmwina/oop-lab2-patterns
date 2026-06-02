from core.questions import QuestionFactory


class EducationalTest:
    """
    @brief Модель навчального тесту.

    Об'єкт містить назву тесту, список питань та максимальний бал.
    """

    def __init__(self):
        """
        @brief Ініціалізує порожній тест.
        """
        self.title = ""
        self.questions = []
        self.max_score = 0

    def __str__(self) -> str:
        """
        @brief Повертає текстовий опис тесту.
        @return Рядок з основною інформацією про тест.
        """
        return (
            f"Test: '{self.title}' | "
            f"Questions: {len(self.questions)} | "
            f"Max Score: {self.max_score}"
        )


class EducationalTestBuilder:
    """
    @brief Будівельник навчального тесту.

    Дозволяє створювати складний об'єкт EducationalTest покроково.

    Патерн: Builder.
    """

    def __init__(self):
        """
        @brief Ініціалізує будівельник і створює новий порожній тест.
        """
        self.reset()

    def reset(self):
        """
        @brief Скидає поточний тест до порожнього стану.
        @return Поточний будівельник для ланцюжкового виклику.
        """
        self._test = EducationalTest()
        return self

    def set_title(self, title: str):
        """
        @brief Встановлює назву тесту.
        @param title Назва тесту.
        @return Поточний будівельник.
        """
        self._test.title = title
        return self

    def add_choice_question(self, text: str, options: list[str]):
        """
        @brief Додає питання з варіантами відповіді.
        @param text Текст питання.
        @param options Варіанти відповіді.
        @return Поточний будівельник.
        """
        question = QuestionFactory.create_question("choice", text, options=options)
        self._test.questions.append(question)
        return self

    def add_text_question(self, text: str):
        """
        @brief Додає текстове питання.
        @param text Текст питання.
        @return Поточний будівельник.
        """
        question = QuestionFactory.create_question("text", text)
        self._test.questions.append(question)
        return self

    def set_max_score(self, score: int):
        """
        @brief Встановлює максимальний бал за тест.
        @param score Максимальний бал.
        @return Поточний будівельник.
        """
        self._test.max_score = score
        return self

    def build(self) -> EducationalTest:
        """
        @brief Завершує створення тесту.
        @return Готовий об'єкт EducationalTest.
        """
        built_test = self._test
        self.reset()
        return built_test