import customtkinter as ctk

from core.facade import EduSystemFacade


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class EduApp(ctk.CTk):
    """
    @brief Графічний інтерфейс системи навчальних завдань.

    GUI використовує EduSystemFacade, щоб не працювати напряму
    з базою даних, будівельником тестів та іншими внутрішніми класами.
    """

    def __init__(self):
        """
        @brief Створює головне вікно програми.
        """
        super().__init__()

        self.title("Система навчальних завдань — OOP Lab 2")
        self.geometry("620x460")

        self.facade = EduSystemFacade()

        self.label = ctk.CTkLabel(
            self,
            text="Система підтримки навчальних завдань",
            font=("Arial", 20, "bold"),
        )
        self.label.pack(pady=20)

        self.btn_create = ctk.CTkButton(
            self,
            text="Створити та зберегти тест",
            command=self.create_test,
            height=40,
        )
        self.btn_create.pack(pady=8)

        self.btn_show = ctk.CTkButton(
            self,
            text="Показати збережені тести",
            command=self.show_saved_tests,
            height=40,
        )
        self.btn_show.pack(pady=8)

        self.text_box = ctk.CTkTextbox(self, width=520, height=250)
        self.text_box.pack(pady=20)

    def create_test(self) -> None:
        """
        @brief Створює демонстраційний тест і зберігає його в SQLite.
        """
        questions = [
            {
                "type": "choice",
                "text": "Is Python compiled?",
                "options": ["Yes", "No"],
            },
            {
                "type": "text",
                "text": "Explain the Observer pattern.",
            },
        ]

        test = self.facade.create_and_save_test(
            "Advanced OOP",
            questions,
            100,
        )

        self.text_box.delete("0.0", "end")
        self.text_box.insert("0.0", "Тест успішно створено і збережено.\n\n")
        self.text_box.insert("end", f"Назва: {test.title}\n")
        self.text_box.insert("end", f"Максимальний бал: {test.max_score}\n")
        self.text_box.insert("end", f"Кількість питань: {len(test.questions)}\n")

    def show_saved_tests(self) -> None:
        """
        @brief Показує тести, які вже збережені у базі даних.
        """
        saved_tests = self.facade.get_saved_tests()

        self.text_box.delete("0.0", "end")

        if not saved_tests:
            self.text_box.insert("0.0", "Збережених тестів поки немає.\n")
            return

        self.text_box.insert("0.0", "Збережені тести:\n\n")

        for test_id, title, max_score in saved_tests:
            self.text_box.insert(
                "end",
                f"#{test_id}: {title} — {max_score} балів\n",
            )


if __name__ == "__main__":
    app = EduApp()
    app.mainloop()