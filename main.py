import time
name = ""
score = 0
mode = 0
win = """
|||        |||   |||||||||||   ||          ||           |||          |||  ||||||||||   ||||||         |||
|||        |||   |         |   ||          ||           |||          |||     |||       ||||||         |||
 |||      |||    |         |   ||          ||           |||          |||     |||       ||| |||        |||
  |||    |||     |         |   ||          ||           |||          |||     |||       |||  |||       |||
   |||  |||      |         |   ||          ||           |||          |||     |||       |||   |||      |||
    ||||||       |         |   ||          ||           |||          |||     |||       |||    |||     |||
      |||        |         |   ||          ||           |||  ||||||  |||     |||       |||     |||    |||
      |||        |         |   ||          ||           ||| |||  ||| |||     |||       |||      |||   |||
      |||        |         |    ||        ||             |||||    |||||      |||       |||       ||||||||
      |||        |||||||||||     ||||||||||               |||      |||    ||||||||||   |||        |||||||"""

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
        level1a()

def level1a():