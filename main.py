import customtkinter as ctk
from core.facade import EduSystemFacade

# Налаштування вигляду CustomTkinter
ctk.set_appearance_mode("dark")  # Темна тема
ctk.set_default_color_theme("blue")  # Сині акценти


class EduApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Система навчальних завдань (OOP Lab 2)")
        self.geometry("500x400")

        # Ініціалізуємо наш Фасад (який під капотом тягне всі 10 патернів)
        self.facade = EduSystemFacade()

        # Заголовок
        self.label = ctk.CTkLabel(self, text="Система підтримки завдань", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Кнопка генерації тесту
        self.btn_create = ctk.CTkButton(
            self,
            text="Створити та зберегти тест (Facade)",
            command=self.create_test,
            height=40
        )
        self.btn_create.pack(pady=10)

        # Текстове поле для виводу логів/результатів
        self.text_box = ctk.CTkTextbox(self, width=400, height=200)
        self.text_box.pack(pady=20)

    def create_test(self):
        # Дані для створення тесту
        questions = [
            {"type": "choice", "text": "Is Python compiled?", "options": ["Yes", "No"]},
            {"type": "text", "text": "Explain the Observer pattern."}
        ]

        # Використовуємо Facade для створення і збереження
        test = self.facade.create_and_save_test("Advanced OOP", questions, 100)

        # Виводимо красивий звіт у текстове поле
        self.text_box.delete("0.0", "end")
        self.text_box.insert("0.0", "✅ Тест успішно створено та збережено в БД!\n\n")
        self.text_box.insert("end", f"📌 Назва: {test.title}\n")
        self.text_box.insert("end", f"🏆 Макс. бал: {test.max_score}\n")
        self.text_box.insert("end", f"📝 Кількість питань: {len(test.questions)}\n")


if __name__ == "__main__":
    app = EduApp()
    app.mainloop()