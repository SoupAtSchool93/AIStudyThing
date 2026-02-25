if __name__ == "__main__": #make sure this is not run directly
    print("""   Why are you running this?
   This is the content script.
   dummy""")
    input("Press [Enter] to exit.")

class questions(): #the actual content
    class multi_choice(): #multiple choice stuff
        test_question = {
            "question":"Test Question",
            "wrong_answers":["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"],
            "correct_answer":"Correct Answer"
        }
        class normal_questions():
            question1 = {
                "question": "What is an example of Unsupervised learning?",
                "wrong_answers": ["Filtering emails","Diagnosing conditions","Loan Approval prediction"],
                "correct_answer": "Video Game Recommendation"
            }
            question2 = {
                "question": "What is the difference between supervised and unsupervised learning?",
                "wrong_answers": ["Unsupervised uses labeled data to predict", "Both are the same", "Supervised clusters data"],
                "correct_answer":"Supervised uses labeled data"
            }
        class trick_questions():
            question1 = {
                "question": "What year was the first turing test?",
                "wrong_answers": ["1961","1965","1969","1963"],
                "correct_answer": "1950"
            }
    class written_answer(): #written answer stuff
        test_question = {
            "question":"Test Question, answer is test",
            "correct_answer":"test",
        }
        class normal_questions():
            question1 = {
            "question":"question 1, to be implemented",
            "correct_answer":"answer",
            }