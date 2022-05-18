#HW30-2 Building a multiple choice quiz
#question class: able to store question prompts and answers
#question a question data type
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
