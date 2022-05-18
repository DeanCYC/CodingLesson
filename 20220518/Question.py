#HW30-2 Building a multiple choice quiz
#question class: able to store question prompts and answers
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
