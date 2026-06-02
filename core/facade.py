from core.db_manager import DBManager
from core.tests import EducationalTestBuilder


class EduSystemFacade:
    """
    @brief Фасад системи навчальних завдань.

    Надає простий інтерфейс для GUI та приховує деталі створення
    тестів і роботи з базою даних.

    Патерн: Facade.
    """

    def __init__(self):
        """
        @brief Ініціалізує фасад, базу даних і будівельник тестів.
        """
        self.db = DBManager()
        self.builder = EducationalTestBuilder()

    def create_and_save_test(
        self,
        title: str,
        questions_data: list[dict],
        max_score: int,
    ):
        """
        @brief Створює тест і зберігає його короткий опис у базі.
        @param title Назва тесту.
        @param questions_data Дані питань.
        @param max_score Максимальний бал.
        @return Створений тест.
        """
        self.builder.reset().set_title(title).set_max_score(max_score)

        for question_data in questions_data:
            if question_data["type"] == "choice":
                self.builder.add_choice_question(
                    question_data["text"],
                    question_data["options"],
                )
            elif question_data["type"] == "text":
                self.builder.add_text_question(question_data["text"])
            else:
                raise ValueError(f"Unknown question type: {question_data['type']}")

        test = self.builder.build()

        self.db.execute_query(
            "INSERT INTO tests (title, max_score) VALUES (?, ?)",
            (test.title, test.max_score),
        )

        return test

    def get_saved_tests(self):
        """
        @brief Повертає список збережених тестів.
        @return Список рядків з таблиці tests.
        """
        return self.db.fetch_all("SELECT id, title, max_score FROM tests ORDER BY id")