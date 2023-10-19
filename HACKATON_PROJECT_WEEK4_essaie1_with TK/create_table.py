import psycopg2
from psycopg2 import sql

db_config = {
    "host": "localhost",      
    "database": "quizz_student",    
    "user": "postgres",      
    "password": "Sam159753",   
    "port" : "5432"
}

def create_database_tables():
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(300) UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(300) UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quizzes (
            quiz_id SERIAL PRIMARY KEY,
            quiz_name TEXT,
            quiz_category TEXT,
            quiz_difficulty TEXT,
            teacher_id INT REFERENCES teachers(teacher_id)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            result_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES students(student_id),
            quiz_id INT REFERENCES quizzes(quiz_id),
            score INT,
            date_taken TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database_tables()





