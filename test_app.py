from core.command import AnswerCommand
from core.db_manager import DBManager
from core.memento import ExamSession, SessionCaretaker
from core.observer import ProgressTracker, Subject
from core.questions import QuestionFactory, QuestionSection, TimedQuestion
from core.scoring import LoyalScoring, StrictScoring
from core.tests import EducationalTestBuilder


def test_singleton_db():
    """
    @brief Перевіряє, що DBManager повертає один і той самий екземпляр.
    """
    db1 = DBManager("test.db")
    db2 = DBManager("test.db")

    assert id(db1) == id(db2)


def test_factory_method():
    """
    @brief Перевіряє створення різних типів питань через фабрику.
    """
    choice_question = QuestionFactory.create_question(
        "choice",
        "2 + 2?",
        options=["3", "4"],
    )
    text_question = QuestionFactory.create_question("text", "What is OOP?")

    assert choice_question.get_question_type() == "choice"
    assert text_question.get_question_type() == "text"
    assert text_question.text == "What is OOP?"


def test_builder_creates_test():
    """
    @brief Перевіряє покрокове створення тесту через Builder.
    """
    test = (
        EducationalTestBuilder()
        .set_title("OOP Basics")
        .add_choice_question("What is Python?", ["Language", "Database"])
        .add_text_question("Explain encapsulation.")
        .set_max_score(100)
        .build()
    )

    assert test.title == "OOP Basics"
    assert len(test.questions) == 2
    assert test.max_score == 100


def test_scoring_strategies():
    """
    @brief Перевіряє строгий і лояльний алгоритми оцінювання.
    """
    strict = StrictScoring()
    loyal = LoyalScoring()

    correct_answers = ["A", "B", "C"]
    user_answers = ["A", "B", "Wrong"]

    assert strict.calculate_score(correct_answers, user_answers, 100) == 0
    assert loyal.calculate_score(correct_answers, user_answers, 100) == 66


def test_composite_question_section():
    """
    @brief Перевіряє, що секція може містити кілька питань.
    """
    section = QuestionSection("Basics")
    section.add(QuestionFactory.create_question("text", "What is OOP?"))
    section.add(QuestionFactory.create_question("choice", "2 + 2?", options=["3", "4"]))

    assert len(section.children) == 2


def test_decorator_timed_question():
    """
    @brief Перевіряє, що декоратор додає часовий ліміт до питання.
    """
    question = QuestionFactory.create_question("text", "Explain inheritance.")
    timed_question = TimedQuestion(question, 60)

    assert timed_question.time_limit == 60
    assert timed_question.wrapped == question


def test_command_answer_and_undo():
    """
    @brief Перевіряє виконання і скасування команди відповіді.
    """
    answers = []
    command = AnswerCommand("What is OOP?", "Object-oriented programming", answers)

    command.execute()
    assert answers == ["Object-oriented programming"]

    command.undo()
    assert answers == []


def test_memento_save_and_restore():
    """
    @brief Перевіряє збереження і відновлення стану тестової сесії.
    """
    session = ExamSession()
    caretaker = SessionCaretaker()

    session.answer("A")
    caretaker.backup(session.save())

    session.answer("B")
    restored_state = caretaker.undo()
    session.restore(restored_state)

    assert session.current_index == 1
    assert session.answers == ["A"]


def test_observer_progress_tracker():
    """
    @brief Перевіряє, що Observer отримує повідомлення від Subject.
    """
    subject = Subject()
    tracker = ProgressTracker()

    subject.attach(tracker)
    subject.notify("Question 1 answered")

    assert tracker.messages == ["Question 1 answered"]