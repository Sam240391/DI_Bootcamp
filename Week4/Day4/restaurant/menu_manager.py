import psycopg2
from menu_item import MenuItem

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Sam159753'
DATABASE = 'my_restaurant'
PORT = '5432'


class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            conn = psycopg2.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
                dbname=DATABASE,
                port=PORT
            )
            cursor = conn.cursor()
            cursor.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (item_name,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            if result:
                return MenuItem(result[0], result[1])
            else:
                return None
        except Exception as e:
            print("Error:", e)
            return None

    @classmethod
    def all_items(cls):
        try:
            conn = psycopg2.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
                dbname=DATABASE,
                port=PORT
            )
            cursor = conn.cursor()
            cursor.execute("SELECT item_name, item_price FROM Menu_Items")
            results = cursor.fetchall()
            cursor.close()
            conn.close()

            menu_items = [MenuItem(result[0], result[1]) for result in results]
            return menu_items
        except Exception as e:
            print("Error:", e)
            return []
        




# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuManager.get_by_name('Beef Stew')
# items = MenuManager.all_items() 


