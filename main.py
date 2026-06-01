from core.facade import EduSystemFacade
from core.scoring import StrictScoring, LoyalScoring

if __name__ == "__main__":
    # --- Перевірка Фасаду ---
    facade = EduSystemFacade()

    questions = [
        {"type": "choice", "text": "Is Python compiled?", "options": ["Yes", "No"]},
        {"type": "text", "text": "What is Facade?"}
    ]

    # Створюємо і зберігаємо тест одним зручним викликом!
    new_test = facade.create_and_save_test("Advanced Python", questions, 100)
    print("✅ Pattern Facade works: Test created and saved seamlessly!")
    print(new_test)

    # --- Перевірка Стратегії ---
    correct = ["No", "Pattern"]
    user_strict = ["Yes", "Pattern"]
    user_loyal = ["No", "Wrong"]

    strict = StrictScoring()
    loyal = LoyalScoring()

    print("\n✅ Pattern Strategy works:")
    print(f"Strict score (1 mistake): {strict.calculate_score(correct, user_strict, 100)}")
    print(f"Loyal score (1 correct out of 2): {loyal.calculate_score(correct, user_loyal, 100)}")