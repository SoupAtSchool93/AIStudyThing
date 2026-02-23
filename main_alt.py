from content import questions
import functions
import random
done_ids = []
print("This script tests a multi choice and written question.")
#grab a random multi choice that hasnt been done
while True:
    question = random.choice(list(questions.multi_choice.normal_questions.__dict__.keys()))
    if question not in done_ids:
        break
functions.ask_multi_choice(questions.multi_choice.normal_questions.__dict__[question])
done_ids.append(question)
