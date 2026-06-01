from core.db_manager import DBManager
from core.tests import TestBuilder


class EduSystemFacade:
    """Facade pattern: єдина точка входу для роботи з усією складною системою."""

    def __init__(self):
        self.db = DBManager()
        self.builder = TestBuilder()

    def create_and_save_test(self, title, questions_data, max_score):
        """Спрощує створення тесту та його збереження в БД до одного методу"""
        self.builder.reset().set_title(title).set_max_score(max_score)

        for q in questions_data:
            if q['type'] == 'choice':
                self.builder.add_choice_question(q['text'], q['options'])
            elif q['type'] == 'text':
                self.builder.add_text_question(q['text'])

        test = self.builder.build()

        # Зберігаємо в базу
        self.db.execute_query(
            "INSERT INTO tests (title, max_score) VALUES (?, ?)",
            (test.title, test.max_score)
        )
        return test