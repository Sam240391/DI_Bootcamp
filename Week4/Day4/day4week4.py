import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Sam159753'
DATABASE = 'dvdrental'
PORT = '5432'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE, port=PORT)


cursor = connection.cursor()

# query = "SELECT last_name, first_name FROM customer LIMIT 20;"

# cursor.execute(query)

# results = cursor.fetchall()

# connection.close()

# for item in results:
#         print(item)


import sqlite3
from tabulate import tabulate

def order():
    choice = None
    while choice != "X":
        print("Moti's Fruit Shake Stand with questionable hygiene")
        inv = get_inv()
        print(tabulate(inv, headers=['Fruit', 'Amount']))
        choice = input("What do you want to add to your shake?")
        update_inv(choice)
    else:
        print("Bye")

def update_inv(choice):
    query = f"UPDATE fruit SET quantity=quantity-1 WHERE name = '{choice}';"
    return run_query(query)

def get_inv():
    query = "SELECT name, quantity FROM fruit ORDER BY name ASC;"
    return run_query(query)

def run_query(query):
    connection = sqlite3.connect("shakes.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

order()
