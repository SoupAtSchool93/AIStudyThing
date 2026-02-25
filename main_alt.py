"""
This is just an alternate main script made by ryder, since the OG main script isnt mine and I wanted to write one.
"""
#imports
from content import questions; import functions; import random; import os; import time
#variables
done_ids = []; failed_grab_counter = 0; done = False; score = 0; done_questions = 0; curr_question = 1

#get some initial stuff, and welcome message
os.system("cls" if os.name == "nt" else "clear")
print("Welcome to the very much complete AI study thing (1.1)")
ammt_to_do = int(input("Ammount of questions to do: "))

#ze main loop
while done_questions < ammt_to_do:
    os.system("cls" if os.name == "nt" else "clear")
    valid = [k for k,v in questions.multi_choice.normal_questions.__dict__.items() #i swear to god if someone touches this I will remove their permissions to the repo and they can use windows notepad to finish anything they can still access.
             if isinstance(v, dict) and not k.startswith("__")]
    while True: 
        question = random.choice(valid)
        if question not in done_ids:
            failed_grab_counter = 0
            print(f"Current question: {curr_question}/{ammt_to_do}")
            if functions.ask_multi_choice(questions.multi_choice.normal_questions.__dict__[question])[0]:
                score += 1
            done_ids.append(question)
            done_questions += 1
            curr_question += 1
            time.sleep(0.5)
        else:
            failed_grab_counter += 1
            if failed_grab_counter > 100:
                print(f"The question grabber has failed to find a new unifnished question in {failed_grab_counter} attempts, exit or reset done question?")
                ans =input("(reset/exit/results)>").lower()
                if ans == "reset":
                    failed_grab_counter = 0
                    done_ids = []
                    print("Done question reset, continuing")
                    continue
                elif ans == "results":
                    break
                else:
                    exit()
        break
print("Results")
print(f"Score: {score}/{ammt_to_do}: {round(score/ammt_to_do*100, 2)}%")
