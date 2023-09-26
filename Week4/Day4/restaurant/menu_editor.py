from menu_item import MenuItem
from menu_manager import MenuManager


HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Sam159753'
DATABASE = 'my_restaurant'
PORT = '5432'

def show_user_menu():
    while True:
        print("\nProgram Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("X - Exit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'V':
            # View an Item
            item_name = input("Enter the name of the item to view: ")
            item = MenuManager.get_by_name(item_name)
            if item:
                print(f"Item: {item.item_name}, Price: {item.item_price}")
            else:
                print("Item not found.")

        elif choice == 'A':
            # Add an Item
            add_item_to_menu()

        elif choice == 'D':
            # Delete an Item
            remove_item_from_menu()

        elif choice == 'U':
            # Update an Item
            update_item_from_menu()

        elif choice == 'S':
            # Show the Menu
            show_restaurant_menu()

        elif choice == 'X':
            # Exit
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    item_name = input("Enter the name of the item: ")
    item_price = input("Enter the price of the item: ")
    try:
        item_price = int(item_price)
        item = MenuItem(item_name, item_price)
        item.save()
        print("Item was added successfully.")
    except ValueError:
        print("Invalid price. Please enter a valid number.")

def remove_item_from_menu():
    item_name = input("Enter the name of the item to remove: ")
    item = MenuItem(item_name, 0)  # Price doesn't matter for deletion
    if item.delete():
        print("Item was deleted successfully.")
    else:
        print("Item not found or error occurred during deletion.")

def update_item_from_menu():
    item_name = input("Enter the name of the item to update: ")
    new_item_name = input("Enter the new name of the item: ")
    new_item_price = input("Enter the new price of the item: ")
    try:
        new_item_price = int(new_item_price)
        item = MenuItem(item_name, 0)  # Price doesn't matter for update
        if item.update(new_item_name, new_item_price):
            print("Item was updated successfully.")
        else:
            print("Item not found or error occurred during update.")
    except ValueError:
        print("Invalid price. Please enter a valid number.")

def show_restaurant_menu():
    print("\nRestaurant Menu:")
    items = MenuManager.all_items()
    for item in items:
        print(f"Item: {item.item_name}, Price: {item.item_price}")




if __name__ == "__main__":
    show_user_menu()


