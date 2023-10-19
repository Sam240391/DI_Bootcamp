import psycopg2
from psycopg2 import sql

db_config = {
    "host": "localhost",      
    "database": "quizz_student",    
    "user": "postgres",      
    "password": "Sam159753",   
    "port" : "5432"
}

def register_student():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last_name: ")
    email = input("Enter your email: ")
    username = input("Enter a username for the student: ")
    password = input("Enter a password: ")

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        ("INSERT INTO students (first_name, last_name, email, username, password) VALUES (%s, %s,%s, %s, %s) RETURNING student_id;"),
        (first_name, last_name, email, username, password)  
    )
    student_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    print(f"Student registered with ID: {student_id}")

def login_student():
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
        login_student()

login_student()