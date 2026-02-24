from content import questions
import functions
import random
done_ids = []
print("This script tests a multi choice and written question.")
#grab a random multi choice that hasnt been done
# only consider attributes that actually contain question dictionaries
valid = [k for k,v in questions.multi_choice.normal_questions.__dict__.items()
         if isinstance(v, dict) and not k.startswith("__")]
while True:
    question = random.choice(valid)
    if question not in done_ids:
        functions.ask_multi_choice(questions.multi_choice.normal_questions.__dict__[question])
        done_ids.append(question)
        break
