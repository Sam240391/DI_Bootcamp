import psycopg2


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Sam159753'
DATABASE = 'my_restaurant'
PORT = '5432'


class MenuItem():
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        try:
            conn = psycopg2.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
                dbname=DATABASE,
                port=PORT
            )
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                (self.item_name, self.item_price)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False
        
    def delete(self):
        try:
            conn = psycopg2.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
                dbname=DATABASE,
                port=PORT
            )
            cursor = conn.cursor()
            query = "DELETE FROM Menu_Items WHERE item_name = '%s'" % self.item_name
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False
        
    def update(self, new_name, new_price):
        try:
            conn = psycopg2.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
                dbname=DATABASE,
                port=PORT
            )
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                (new_name, new_price, self.item_name)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False
        

