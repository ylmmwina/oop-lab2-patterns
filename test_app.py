import pytest
from core.db_manager import DBManager
from core.questions import QuestionFactory
from core.scoring import StrictScoring, LoyalScoring


def test_singleton_db():
    """Перевіряємо, що БД завжди повертає один і той самий об'єкт"""
    db1 = DBManager("test.db")
    db2 = DBManager("test.db")
    assert id(db1) == id(db2)


def test_factory_method():
    """Перевіряємо створення питань через Фабрику"""
    q_choice = QuestionFactory.create_question("choice", "2+2?", options=["3", "4"])
    q_text = QuestionFactory.create_question("text", "What is OOP?")

    assert q_choice.get_question_type() == "choice"
    assert q_text.get_question_type() == "text"
    assert q_text.text == "What is OOP?"


def test_scoring_strategies():
    """Перевіряємо алгоритми підрахунку балів (Strategy)"""
    strict = StrictScoring()
    loyal = LoyalScoring()

    correct_answers = ["A", "B", "C"]
    user_answers = ["A", "B", "Wrong"]  # 2 з 3 правильні

    # Суворе оцінювання дає 0, бо є одна помилка
    assert strict.calculate_score(correct_answers, user_answers, 100) == 0

    # Лояльне оцінювання дає частковий бал (2/3 від 100 = 66)
    assert loyal.calculate_score(correct_answers, user_answers, 100) == 66