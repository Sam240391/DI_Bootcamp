import requests
import json
from pprint import pprint
import psycopg2


db_config = {
    "host": "localhost",      
    "database": "quizz_student",    
    "user": "postgres",      
    "password": "Sam159753",   
    "port" : "5432"
}

def create_database_tables_categories():
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
    """)
    conn.commit()
    conn.close()

categories_url = 'https://opentdb.com/api_category.php'

response = requests.get(categories_url)
print(response)
data = response.json()

pprint(data['trivia_categories'])

data_categories = data['trivia_categories']
pprint(data_categories)


for category in data_categories:
    print(f"{category['id']} : {category['name']}")


# if __name__ == "__main__":
#     create_database_tables_categories()


def add_category():
    for category in data_categories:
        category_id = category['id']
        name = category['name']

        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO categories (category_id, name) VALUES (%s, %s)",
                (category_id, name))

        conn.commit()
        conn.close()


if __name__ == "__main__":
    add_category()




