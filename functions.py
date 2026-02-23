def ask_multi_choice(question_class):
    """
    ask a multi choice question from content.py
    input question class should be like "content.questions.multi_choice.normal_questions.question1"
    returns if user got question right, and answer they picked in list: [right=bool, answer=str]
    """
    question = question_class()
    print(question.question)
    counter = 1
    for i in question.choices:
        print(f"{i}")