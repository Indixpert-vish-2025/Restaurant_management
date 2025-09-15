import json
import os

class MenuManager:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    menu_file = os.path.join(base_dir, 'Database', 'menu.json')

    @staticmethod
    def read_menu():
        if not os.path.exists(MenuManager.menu_file) or os.path.getsize(MenuManager.menu_file) == 0:
            return []
        with open(MenuManager.menu_file, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_menu(data):
        with open(MenuManager.menu_file, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def add_menu_item(cls):
        item_name = input("Enter item name: ")
        try:
            half_price = float(input("Enter half plate price: "))
            full_price = float(input("Enter full plate price: "))
        except ValueError:
            print("Invalid price. Must be a number.")
            return

        new_item = {
            "name": item_name,
            "half_price": half_price,
            "full_price": full_price
        }

        menu = cls.read_menu()
        menu.append(new_item)
        cls.write_menu(menu)
        print(f"'{item_name}' added to menu successfully!")

    @classmethod
    def view_menu(cls):
        menu = cls.read_menu()
        if not menu:
            print("Menu is empty.")
        else:
            print("\n--- Current Menu ---")
            for idx, item in enumerate(menu, start=1):
                print(f"{idx}. {item['name']} - Half: ₹{item['half_price']} | Full: ₹{item['full_price']}")
 
