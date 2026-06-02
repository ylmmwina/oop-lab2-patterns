from abc import ABC, abstractmethod


class ScoringStrategy(ABC):
    """
    @brief Базова стратегія оцінювання відповідей.

    Дозволяє змінювати алгоритм оцінювання без зміни клієнтського коду.

    Патерн: Strategy.
    """

    @abstractmethod
    def calculate_score(
        self,
        correct_answers: list[str],
        user_answers: list[str],
        max_score: int,
    ) -> int:
        """
        @brief Обчислює результат тесту.
        @param correct_answers Список правильних відповідей.
        @param user_answers Список відповідей користувача.
        @param max_score Максимальний бал.
        @return Набраний бал.
        """
        pass


class StrictScoring(ScoringStrategy):
    """
    @brief Строге оцінювання.

    Дає повний бал тільки тоді, коли всі відповіді правильні.
    """

    def calculate_score(
        self,
        correct_answers: list[str],
        user_answers: list[str],
        max_score: int,
    ) -> int:
        """
        @brief Обчислює результат за строгим правилом.
        @param correct_answers Список правильних відповідей.
        @param user_answers Список відповідей користувача.
        @param max_score Максимальний бал.
        @return max_score або 0.
        """
        if correct_answers == user_answers:
            return max_score
        return 0


class LoyalScoring(ScoringStrategy):
    """
    @brief Лояльне оцінювання.

    Дає частковий бал за кожну правильну відповідь.
    """

    def calculate_score(
        self,
        correct_answers: list[str],
        user_answers: list[str],
        max_score: int,
    ) -> int:
        """
        @brief Обчислює частковий результат.
        @param correct_answers Список правильних відповідей.
        @param user_answers Список відповідей користувача.
        @param max_score Максимальний бал.
        @return Частковий бал.
        """
        if not correct_answers:
            return 0

        correct_count = sum(
            1
            for correct_answer, user_answer in zip(correct_answers, user_answers)
            if correct_answer == user_answer
        )

        return int((correct_count / len(correct_answers)) * max_score)