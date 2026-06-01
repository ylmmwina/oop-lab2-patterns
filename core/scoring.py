from abc import ABC, abstractmethod

class ScoringStrategy(ABC):
    """Базова стратегія для підрахунку балів"""
    @abstractmethod
    def calculate_score(self, correct_answers, user_answers, max_score):
        pass

class StrictScoring(ScoringStrategy):
    """Суворе оцінювання: бал дається лише якщо всі відповіді 100% правильні"""
    def calculate_score(self, correct_answers, user_answers, max_score):
        if correct_answers == user_answers:
            return max_score
        return 0

class LoyalScoring(ScoringStrategy):
    """Лояльне оцінювання: дає часткові бали за кожну правильну відповідь"""
    def calculate_score(self, correct_answers, user_answers, max_score):
        if not correct_answers:
            return 0
        correct_count = sum(1 for a, b in zip(correct_answers, user_answers) if a == b)
        return int((correct_count / len(correct_answers)) * max_score)