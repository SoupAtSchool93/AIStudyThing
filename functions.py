import random
def test():
    """testing function, """
    print("This is a test function, functions.py is imported!")
def ask_multi_choice(question_class):
    """
    ask a multi choice question from content.py
    input question class should be like "normal_questions.question1"
    returns if user got question right, and answer they picked in list: [right=bool, answer=str]
    """
    zequestion = question_class
    print(zequestion["question"])
    counter = 1
    choices = []
    for i in zequestion["wrong_answers"]:
        choices.append(i)
    choices.append(zequestion["correct_answer"])
    random.shuffle(choices)
    for i in range(len(choices)):
        print(f"{counter}. {choices[i]}")
    counter = 1
    answered = False
    while not answered:
        answer = int(input("Answer (number as shown):"))-1
    if answer == choices.index(zequestion["correct_answer"]):
        print("Correct!")
        return [True, choices[answer]]
    elif not answer == choices.index(zequestion["correct_answer"]):
        print("Wrong!")
        return [False, choices[answer]]
def ask_written(question_class):
    """
    ask a written question from content.py
    input question class should be like "normal_questions.question1"
    returns if user got question right, and answer they picked in list: [right=bool, answer=str]
    """
    