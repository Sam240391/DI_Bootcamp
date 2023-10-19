import psycopg2
from psycopg2 import sql

db_config = {
    "host": "localhost",      
    "database": "quizz_student",    
    "user": "postgres",      
    "password": "Sam159753",   
    "port" : "5432"
}

def register_teacher():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    username = input("Enter a username for the teacher: ")
    password = input("Enter a password: ")

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        ("INSERT INTO teachers (first_name, last_name, email, username, password) VALUES (%s, %s,%s, %s, %s) RETURNING teacher_id;"),
        (first_name, last_name, email, username, password)  
    )
    teacher_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f"teacher registered with ID: {teacher_id}")
    user_choice = input(f'Do you want to add another teacher ? Yes or No')
    if user_choice.lower() == 'yes':
        register_teacher()
    else:
        quit

def login_teacher():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        ("SELECT * FROM students WHERE username = %s AND password = %s"),
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful. Welcome, student!")
    else:
        print("Login failed. Please check your username and password.")
        login_teacher()


register_teacher()