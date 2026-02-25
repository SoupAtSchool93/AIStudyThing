import random
def test():
    """testing function, for making sure importing is working"""
    print("This is a test function, functions.py is imported!")
def ask_multi_choice(question_dir):
    """
    ask a multi choice question from content.py, but when finished will just pull from within main.py
    input question dir should be like "normal_questions.question1"
    returns if user got question right, and answer they picked in list: [right=bool, answer=str]
    """
    zequestion = question_dir
    print(zequestion["question"])
    counter = 1
    choices = []
    for i in zequestion["wrong_answers"]:
        choices.append(i)
    choices.append(zequestion["correct_answer"])
    random.shuffle(choices)
    for i in range(len(choices)):
        print(f"{counter}. {choices[i]}")
        counter += 1

    # loop until we get a valid numeric response
    while True:
        try:
            answer = int(input("Answer (number as shown): "))-1
            if 0 <= answer < len(choices):
                break
            else:
                print("Please enter a number corresponding to one of the choices.")
        except ValueError:
            print("Invalid input; please enter a number.")

    if answer == choices.index(zequestion["correct_answer"]):
        print("Correct!")
        return [True, choices[answer]]
    else:
        print("Wrong!")
        return [False, choices[answer], zequestion["correct_answer"]]
def ask_written(question_dir):
    """
    ask a written question from content.py, but when finished will just pull from within main.py
    input question dir should be like "normal_questions.question1"
    returns if user got question right, and answer they picked in list: [right=bool, answer=str]
    """
    zequestion = eval("questions.written_answer."+question_dir)
    print(zequestion["question"])
    answer = input("<Answer> =  ")
    if answer.lower().strip() == zequestion["correct_answer"].lower().strip():
        print("Right.")
        return [True, answer]
    else:
        print("Wrong.")
        return [False, answer, zequestion["correct_answer"]]    