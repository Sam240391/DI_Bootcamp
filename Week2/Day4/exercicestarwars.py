
# import random


# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]



# def ask_questions(questions):
#     correct_answers = 0
#     incorrect_answers = 0
#     wrong_answers = []

#     # random.shuffle(questions)  # Shuffle the questions for variety

#     for question_data in questions:
#         question = question_data["question"]
#         correct_answer = question_data["answer"]

#         user_answer = input(question + " ").strip()

#         if user_answer.lower() == correct_answer.lower():
#             print("Correct!")
#             correct_answers += 1
#         else:
#             print(f"Wrong! The correct answer is: {correct_answer}")
#             incorrect_answers += 1
#             wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

#     return correct_answers, incorrect_answers, wrong_answers

# def display_results(correct, incorrect, wrong_answers):
#     print("\nQuiz Results:")
#     print(f"Correct Answers: {correct}")
#     print(f"Incorrect Answers: {incorrect}")

#     if incorrect > 3:
#         print("\nYou answered more than 3 questions incorrectly. Please play again.")
        

#     if wrong_answers:
#         print("\nQuestions you answered incorrectly:")
#         for i, data in enumerate(wrong_answers, 1):
#             print(f"{i}. Question: {data['question']}")
#             print(f"   Your Answer: {data['user_answer']}")
#             print(f"   Correct Answer: {data['correct_answer']}")

# def star_wars_quiz():
#     print("Welcome to the Star Wars Quiz!")
#     correct, incorrect, wrong_answers = ask_questions(data)
#     display_results(correct, incorrect, wrong_answers)

# if __name__ == "__main__":
#     star_wars_quiz()




data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

# Functiun that it will ask questions to the user and check the answers
def check_answers () :
    # first variable which count the number of correct answer
    number_correct_answers = 0
    # second variable which count the number of incorrect answer
    number_incorrect_answers = 0
    # we create list for wrong answer of the user that we will fill with the Data and the wrong answer 
    list_wrong_answers = []


    print("\n ---- The quizz starts ----")

    # we create a loop that will compare the user answer with the answer of each question 
    for quizz in data :
        # For all answers user same that the correct answer 
        user_answer = input(quizz["question"])
        # if the answer of the user is the same that the answer of the relevant question s
        if user_answer.lower() == quizz["answer"].lower():
            #  so add 1 to the variable number_correct_answer
            number_correct_answers += 1
        else :
            # if the asnwer of the user is no equal to the correct answer so add 1 to the number_incorrect_answers
            number_incorrect_answers += 1
            new_quizz = quizz.copy() #make a copy of the dictionary
            # we add inside the dictionnary new element that it will be the user answer
            new_quizz["user_answer"] = user_answer
            # we add in the list of dictionnary (list_wring_answers) the question, correct answer and user wronganswer 
            list_wrong_answers.append(new_quizz)
    
    #After ask all the questions and create all variable and liste we need we will call the second function in order to display the information regarding the answer to the user 
    inform_user(number_correct_answers, number_incorrect_answers, list_wrong_answers)


# we create the new function who will display and inform user
def inform_user (correct, incorrect, wrong_answers) :
    #  we inform the user regarding the number of correct and inccorect answwers
    print("\n ----------------------------")
    print(f"You have {correct} correct answers")
    print(f"You have {incorrect} incorrect answers")
    # we make a loop  that will show to the user all question that he has wrong answer 
    for global_answer in wrong_answers :
        print(f'The question was {global_answer["question"]}')
        print(f'Your answer was {global_answer["user_answer"]}')
        print(f'Your got it wrong, the correct answer is {global_answer["answer"]}')

    
    print("\n --------------------")
    # we create a condition if the user has more thatn 3 wrong aswer the play start again
    if incorrect > 3 :
        print(" YOU GOT MORE 3 ANSWERS WRONG Play Again")
        check_answers()
    else :
        print("Good Job - YOU DONT NEED TO REDO THE GAME")

#  we call the function 
check_answers()


















