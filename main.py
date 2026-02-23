import time
from content import questions
from functions import *
name = ""
score = 0
mode = 1
win = """
 |||        |||   |||||||||||   ||          ||           |||          |||  ||||||||||   ||||||         |||
 |||        |||   ||       ||   ||          ||           |||          |||     |||       ||||||         |||
  |||      |||    ||       ||   ||          ||           |||          |||     |||       ||| |||        |||
   |||    |||     ||       ||   ||          ||           |||          |||     |||       |||  |||       |||
    |||  |||      ||       ||   ||          ||           |||          |||     |||       |||   |||      |||
     ||||||       ||       ||   ||          ||           |||          |||     |||       |||    |||     |||
      ||||        ||       ||   ||          ||           |||  ||||||  |||     |||       |||     |||    |||
      ||||        ||       ||   ||          ||           ||| |||  ||| |||     |||       |||      |||   |||
      ||||        ||       ||    ||        ||             |||||    |||||      |||       |||       ||||||||
      ||||        |||||||||||     ||||||||||               |||      |||    ||||||||||   |||        |||||||"""

def start():
    global score, name, mode
    print("Hello and welcome to the AI study thing...")
    time.sleep(1)
    print("If you answer a question wrong, you fail an restart. This is on Section 1.1 - AI Fundamentals")
    time.sleep(3)
    name = input("What is your name, Studying person?")
    if name == "Professor":
        print("Hard mode activated... good luck!")
        mode = 2
        level1_1()
    else:
        print(f"Hello, {name}! Let's start studying!")

def level1_1():
    if mode == 2:
        print(content.multi_choice.trick_question.question1)
    else:
        print(content.multi_choice.normal_questions.question1)
