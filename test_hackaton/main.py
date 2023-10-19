import requests
import html
import random
from pprint import pprint
import psycopg2


db_config = {
    "host": "localhost",      
    "database": "quizz_student",    
    "user": "postgres",      
    "password": "Sam159753",   
    "port" : "5432"
}

# Get a pool o trivia questions
def get_question_pool(amount: int, category: int) -> list:
    url = f'https://opentdb.com/api.php?amount={amount}&category={category}'
    response = requests.get(url)
    response_json = response.json()
    return response_json['results']


# Shuffle the answer choices for a question

def shuffle_choices(choices: list) -> list:
    random.shuffle(choices)
    return choices

# print the answer choices in the console
def print_choices(choices: list) -> None:
    for choice_index, choice in enumerate(choices):
        print(f'{choice_index+1}. {html.unescape(choice)}')


#Get the user(s choice in the console
def get_user_choice() -> int:
    while True:
        user_choice = int(input('Enter the number of your choice: '))
        if user_choice in range(1,5):
            return user_choice - 1 
        else:
            print('Wrong Input, Please enter the number of your choice: ')




# question_pool = get_question_pool(1, 9)
# print(question_pool[0]['category'])
# print(get_question_pool(5, 9)[0]['correct_answer'])



# play the game
def play_game (amount: int, category: int) -> None:

    name = input(f'What is your name')

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO quizzes (quiz_name, quiz_category, number_of_question ) VALUES (%s, %s, %s)",
            (name, category, amount))

    conn.commit()
    conn.close()

    index = 0
    user_correct_answers = 0
    question_pool = get_question_pool(amount, category)
    for question in question_pool:

        category = question['category'] # categorie de chaque questions

        question_text = html.unescape(question["question"])
        print (question_text)
        choices = question ["incorrect_answers"]
        choices.extend([question ["correct_answer"]])
        shuffled_choices = shuffle_choices(choices)
        print_choices (shuffled_choices)
        user_choice_index = get_user_choice()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question ["correct_answer"])


        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(f""" SELECT quiz_id FROM quizzes
                                    WHERE quiz_name = '{name}'
                                    ORDER BY quiz_id DESC LIMIT 1
                                 """)
        
        quiz_id = cursor.fetchone()
        
        cursor.execute(f""" SELECT category_id FROM categories
                                    WHERE name = '{category}'
                                 """)
        
        category_id = cursor.fetchone()

        cursor.execute("INSERT INTO questions (category_id, quiz_id, question, choice_answer, good_answer) VALUES (%s, %s,%s,%s,%s)",
                (category_id, quiz_id, question_text, shuffled_choices, correct_choice_text))

        conn.commit()
        conn.close()


        if user_choice_text == correct_choice_text:
            user_correct_answers += 1
            print (f"Correct! You answered: {correct_choice_text}\n")
        else:
            print(f"Incorrect. The correct answer is: {correct_choice_text}\n")

    print(f'you score is : {user_correct_answers} / {amount}')

    return user_correct_answers

# Call mail function 

def ask_category():
    print('Select a catégorie')
    print('1. General Knowledge | 2. History | 3. Geography | 4. Sport | 5. Science : computers ')
    user_category = int(input(f'Select a category'))
    category = 0
    if user_category == 1:
        category = 9
        return category
    elif user_category == 2:
        category = 23
        return category
    elif user_category == 3:
        category = 22
        return category
    elif user_category == 4:
        category = 21
        return category
    elif user_category == 5:
        category = 18
        return category
    else:
        print(f'Wrong input')
        ask_category()





def main():
    print()
    print(f'Welcome to our QUIZZ')
    print('-----------------------')
    
    user_amount_question = 10

    play_game (user_amount_question, ask_category())

    



main()

    
    