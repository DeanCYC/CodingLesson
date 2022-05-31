#HW30-1 Building a multiple choice quiz
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Geen\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"), #create question object and assign the answer
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions): #create question array
    score = 0
    for question in questions: #for each question object inside of the question array
        answer = input(question.prompt)
        if answer == question.answer: #check answer that input by user is euqal to the answer of current question
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct") #count the number of correct answer and show the number of question

run_test(questions)