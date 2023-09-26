import requests
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Sam159753'
DATABASE = 'dailychallengeday4'
PORT = '5432'

API_URL = "https://restcountries.com/v3.1/all"


NUmber_random = 10
def fetch_random_countries():
    try:
        # Fetch data from the REST Countries API
        response = requests.get(API_URL)
        data = response.json()

        # Randomly select 10 countries from the API data
        import random
        random_countries = random.sample(data, NUmber_random)

        return random_countries
    except Exception as e:
        print("Error fetching data from the API:", e)
        return []
    



def insert_countries_into_db(countries):
    try:
        # Establish a database connection
        conn = psycopg2.connect(
            host=HOSTNAME,
            user=USERNAME,
            password=PASSWORD,
            dbname=DATABASE,
            port=PORT
        )
        cursor = conn.cursor()

        # Insert each country into the database
        for country in countries:
            name = country.get('name', {}).get('common', '')
            capital = country.get('capital', [''])[0]  # Extract the first capital
            flag = country.get('flags', {}).get('png', '')
            subregion = country.get('subregion', '')
            population = country.get('population', 0)

            # Insert the country data into the database
            cursor.execute(
                "INSERT INTO Countries (name, capital, flag, subregion, population) "
                "VALUES (%s, %s, %s, %s, %s)",
                (name, capital, flag, subregion, population)
            )

        # Commit the changes and close the database connection
        conn.commit()
        cursor.close()
        conn.close()

        print("Countries inserted into the database successfully.")
    except Exception as e:
        print("Error inserting data into the database:", e)

if __name__ == "__main__":
    random_countries = fetch_random_countries()
    if random_countries:
        insert_countries_into_db(random_countries)