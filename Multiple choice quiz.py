#building a multiple choice quiz
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompt = [
    "What is the color of a carrot?\n(a) blue\n(b) orange\n(c) green\n\n",
    "Which country is Lagos state located?\n(a) Nigeria\n(b) United States\n(c) England\n\n",
    "Which is the closest planet to the sun?\n(a) Venus\n(b) Saturn\n(c) Mercury\n\n",
    "Which is the closest planet to the sun?\n(a) 6\n(b) 7\n(c) 5\n\n"
]
questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "c"),
    Question(question_prompt[3], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)