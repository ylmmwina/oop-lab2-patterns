from core.db_manager import DBManager
from core.tests import TestBuilder

if __name__ == "__main__":
    db = DBManager()

    # Будуємо тест за допомогою Builder та Factory
    builder = TestBuilder()
    my_test = (builder.set_title("OOP Basics")
               .add_choice_question("What is encapsulation?", ["Hiding data", "Polymorphism"])
               .add_text_question("Describe the Singleton pattern.")
               .set_max_score(10)
               .build())

    print("✅ Patterns Factory Method & Builder work:\n")
    print(my_test)
    for i, q in enumerate(my_test.questions, 1):
        print(f" {i}. [{q.get_question_type()}] {q.text}")