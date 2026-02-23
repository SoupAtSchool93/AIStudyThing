if __name__ == "__main__":
    print("""Why are you running this?
          This is the content script.
          dummy""")
    input("Press [Enter] to exit.")

class questions():
    class multi_choice():
        class test_question():
            question = "Test Qestion"
            wrong_answers = ["Wrong Answer 1", "Wrong Answer 2", "Wrong Answer 3"]
            correct_answer = "Correct Answer"
        class normal_questions():
            class question1():
                question = "What is an example of Unsupervised learning? Filtering Emails, Diagnosing conditions, Video Game Recommendation, or Loan Approval prediction?"
                wrong_answers = ["Filtering emails","Diagnosing conditions","Loan Approval prediction"]
                correct_answer = "Video Game Recommendation"
        class trick_questions():
            class question1():
                question = "What year was the first turing test? 1961, 1965, 1969, or 1963?"
                wrong_answers = ["1961","1965","1969","1963"]
                correct_answer = "1950"
    class written_answer():
        class test_question():
            question = ""
            answers = ["","",""]