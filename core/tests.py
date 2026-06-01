from core.questions import QuestionFactory

class Test:
    def __init__(self):
        self.title = ""
        self.questions = []
        self.max_score = 0

    def __str__(self):
        return f"Test: '{self.title}' | Questions: {len(self.questions)} | Max Score: {self.max_score}"

class TestBuilder:
    """Builder pattern for constructing complex test objects step by step."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._test = Test()
        return self

    def set_title(self, title):
        self._test.title = title
        return self

    def add_choice_question(self, text, options):
        q = QuestionFactory.create_question("choice", text, options=options)
        self._test.questions.append(q)
        return self

    def add_text_question(self, text):
        q = QuestionFactory.create_question("text", text)
        self._test.questions.append(q)
        return self

    def set_max_score(self, score):
        self._test.max_score = score
        return self

    def build(self):
        built_test = self._test
        self.reset()
        return built_test