if __name__ == "__main__": #make sure this is not run directly
    print("""   Why are you running this?
   This is the content script.
   dummy""")
    input("Press [Enter] to exit.")

"""
ID system works as follows:
first digit is 1 if multi choice, 2 if written answer
2nd digit is 0 for test, 1 for normal, 2 for trick
3rd is number of question;
so 1.0.1 would be multi choice test question,
2.1.3 would be written answer normal question 3, etc.
"""


class questions(): #the actual content
    class multi_choice(): #multiple choice stuff, formatting is not the same as written answer, john.
        test_question = {
            "id":"1.0.1",
            "question":"Test Question",
            "wrong_answers":["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"],
            "correct_answer":"Correct Answer"
        }
        class normal_questions():
            question1 = {
                "id":"1.1.1",
                "question": "What is an example of Unsupervised learning?",
                "wrong_answers": ["Filtering emails","Diagnosing conditions","Loan Approval prediction"],
                "correct_answer": "Video Game Recommendation"
            }
            question2 = {
                "id":"1.1.2",
                "question": "What is the difference between supervised and unsupervised learning?",
                "wrong_answers": ["Unsupervised uses labeled data to predict", "Both are the same", "Supervised clusters data"],
                "correct_answer":"Supervised uses labeled data"
            }
            question3 = {
                "id":"1.1.3",
                "question":"True or False: A Rational agent is a agent that makes continuous steps to get from point A to point B.",
                "wrong_answers":["True"],
                "correct_answer":"False"
            }
            question3part2 = {
                "id":"1.1.3",
                "question":"True or False: Part-of-Speech (POS) tagging is a Natural Language Processing (NLP) process that assigns grammatical categories—such as nouns, verbs, adjectives, and adverbs—to each word (token) in a text based on its definition and context.",
                "wrong_answers":["False"],
                "correct_answer":"True"
            }
            question4 = {
                "id":"1.1.4",
                "question":"What is the purpose of AI? To serve us in every concieveable way",
                "wrong_answers":["To serve us in every concieveable way", "Take our jobs", "Hack the government"],
                "correct_answer":"Mimic human-like intelligence"
            }
            question5 = {
                "id":"1.1.5",
                "question":"What mistake did google make in 2018?",
                "wrong_answers":["Have syntax errors", "Promote racism", "Using wrong interpolation laws"],
                "correct_answer":"non-representative sampling"
            }
        class trick_questions():
            question1 = {
                "id":"1.2.1",
                "question": "What year was the first turing test?",
                "wrong_answers": ["1961","1965","1969","1963"],
                "correct_answer": "1950" 
            }
    class written_answer(): #written answer stuff, formatting is not the same as multiple choice, john.
        test_question = {
            "id":"2.0.1",
            "question":"What is the machine that was the first implementation of an artificial neural network designed to learn from experience, rather than being explicitly programmed for every task called?",
            "correct_answer":["perceptron"] 
        }    
        class normal_questions():
            question1 = {
            "id":"2.1.1",
            "question":" Which thing is not a subdomain of AI? Natural Language Processing, Machine Learning (ML), Computer Vision, or Data Science?",
            "correct_answer":["Data Science"]
            }
            question2 = {
                "id":"2.1.2",
                "question":"",
                "correct_answer":["answer"],
            }
            question3 = {
                "id":"2.1.3",
                "question":"What is AGI?",
                "correct_answer":["Artificial General Intelligence"]
            }
            question = {
                "id":"2.1.",
                "question":"",
                "correct_answer":[""]
            }
            question = {
                "id":"2.1.",
                "question":"",
                "wrong_answers":"",
                "correct_answer":[""]
            }