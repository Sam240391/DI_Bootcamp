
import random


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



def ask_questions(questions):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    # random.shuffle(questions)  # Shuffle the questions for variety

    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(question + " ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            incorrect_answers += 1
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    return correct_answers, incorrect_answers, wrong_answers

def display_results(correct, incorrect, wrong_answers):
    print("\nQuiz Results:")
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}")

    if incorrect > 3:
        print("\nYou answered more than 3 questions incorrectly. Please play again.")

    if wrong_answers:
        print("\nQuestions you answered incorrectly:")
        for i, data in enumerate(wrong_answers, 1):
            print(f"{i}. Question: {data['question']}")
            print(f"   Your Answer: {data['user_answer']}")
            print(f"   Correct Answer: {data['correct_answer']}")

def star_wars_quiz():
    print("Welcome to the Star Wars Quiz!")
    correct, incorrect, wrong_answers = ask_questions(data)
    display_results(correct, incorrect, wrong_answers)

if __name__ == "__main__":
    star_wars_quiz()
