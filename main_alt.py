"""
This is just an alternate main script made by ryder, since the OG main script isnt mine and I wanted to write one.
"""
#imports
from content import questions
import functions
import random
#variables
done_ids = []

print("This script tests a multi choice and written question.") #remove this when this is finished, just here for now.

#grab a random multi choice that hasnt been done, just does nothing tho if it is a done one, gonna need to make it keep trying until it finds unfinished one.
valid = [k for k,v in questions.multi_choice.normal_questions.__dict__.items()
         if isinstance(v, dict) and not k.startswith("__")]

while True:
    question = random.choice(valid)
    if question not in done_ids:
        functions.ask_multi_choice(questions.multi_choice.normal_questions.__dict__[question])
        done_ids.append(question)
        break
