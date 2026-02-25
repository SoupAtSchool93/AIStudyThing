"""
This is just an alternate main script made by ryder, since the OG main script isnt mine and I wanted to write one.
"""
#imports
from content import questions; import functions; import random; import os; import time
# variables
# `done_ids` will store actual question ids (from content dictionaries)
done_ids = []
failed_grab_counter = 0
score = 0
done_questions = 0
curr_question = 1
# toggle debugging output for skipped questions
debug = False  # set to True during development to see why questions are skipped

#get some initial stuff, and welcome message
os.system("cls" if os.name == "nt" else "clear")
print("Welcome to the very much complete AI study thing (section 1.1, version v0.1-alpha)")
ammt_to_do = int(input("Ammount of questions to do: "))

#ze main loop
while done_questions < ammt_to_do:
    os.system("cls" if os.name == "nt" else "clear")
    valid = [k for k,v in questions.multi_choice.normal_questions.__dict__.items()
             if isinstance(v, dict) and not k.startswith("__")]

    while True:
        question_key = random.choice(valid)
        qdict = questions.multi_choice.normal_questions.__dict__[question_key]
        qid = qdict.get("id")

        if qid in done_ids:
            # already asked this specific question
            if debug:
                print(f"skipping {qid}: already in done_ids")
            failed_grab_counter += 1
            # if we've tried too many times give the user options
            if failed_grab_counter > 100:
                print(
                    f"The question grabber has failed to find a new unfinished question in {failed_grab_counter} attempts, exit or reset done question?"
                )
                ans = input("(reset/exit/results)>").lower()
                if ans == "reset":
                    failed_grab_counter = 0
                    done_ids = []
                    print("Done questions reset, continuing")
                    continue
                elif ans == "results":
                    break
                else:
                    exit()
            continue  # pick another question

        # found a new question
        failed_grab_counter = 0
        print(f"Current question: {curr_question}/{ammt_to_do}")
        if functions.ask_multi_choice(qdict)[0]:
            score += 1
        done_ids.append(qid)
        done_questions += 1
        curr_question += 1
        time.sleep(0.5)
        break
print("Results")
percentage = round(score/ammt_to_do*100, 2)
if percentage >= 90:
    letter = "A"
elif percentage >= 80:
    letter = "B"
elif percentage >= 70:
    letter = "C"
elif percentage >= 60:
    letter = "D"
else:
    letter = "F"
print(f"Score: {score}/{ammt_to_do}: {percentage}% ({letter})")
input("Press [Enter] to exit.")
os.system("cls" if os.name == "nt" else "clear")
exit()