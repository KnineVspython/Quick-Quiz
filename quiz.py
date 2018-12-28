from Question import Question
# simple questions set up
question_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
# options and answers
questions =[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

# score
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
# results model
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)