from core.db_manager import DBManager
from core.questions import QuestionFactory, QuestionSection, TimedQuestion

if __name__ == "__main__":
    db = DBManager()

    # Створюємо окремі питання через Factory
    q1 = QuestionFactory.create_question("choice", "What is polymorphism?", options=["Many forms", "One form"])
    q2 = QuestionFactory.create_question("text", "Explain encapsulation.")

    # Використовуємо Decorator, щоб додати таймер до другого питання
    timed_q2 = TimedQuestion(q2, time_limit=60)

    # Використовуємо Composite, щоб згрупувати їх у секцію
    section = QuestionSection("OOP Principles")
    section.add(q1)
    section.add(timed_q2)

    print("✅ Patterns Composite & Decorator work:\n")
    section.display()