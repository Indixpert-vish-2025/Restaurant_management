import json
import os

class OrderManager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    order_file = os.path.join(base_dir, '..', 'Database', 'orders.json')

    @classmethod
    def ensure_order_file(cls):
        folder = os.path.dirname(cls.order_file)
        if not os.path.exists(folder):
            os.makedirs(folder)
        if not os.path.exists(cls.order_file):
            with open(cls.order_file, 'w') as f:
                json.dump([], f)

    @classmethod
    def load_orders(cls):
        cls.ensure_order_file()
        with open(cls.order_file, 'r') as file:
            return json.load(file)

    @classmethod
    def save_orders(cls, orders):
        with open(cls.order_file, 'w') as file:
            json.dump(orders, file, indent=4)

    @classmethod
    def place_order(cls):
        customer_name = input("Customer Name: ")
        item = input("Item Ordered: ")
        quantity = input("Quantity: ")

        order = {
            "customer_name": customer_name,
            "item": item,
            "quantity": quantity,
            "status": "Processing"
        }

        orders = cls.load_orders()
        orders.append(order)
        cls.save_orders(orders)
        print("\nOrder placed and is now in 'Processing' status.\n")

    @classmethod
    def update_order_status(cls):
        orders = cls.load_orders()
        if not orders:
            print("\nNo orders found.\n")
            return

        print("\nCurrent Orders:")
        for idx, order in enumerate(orders, 1):
            print(f"{idx}. {order['customer_name']} - {order['item']} ({order['status']})")

        choice = int(input("Enter order number to mark as 'Completed': "))
        if 1 <= choice <= len(orders):
            orders[choice - 1]['status'] = "Completed"
            cls.save_orders(orders)
            print("Order status updated to Completed.")

    @classmethod
    def show_ready_orders(cls):
        orders = cls.load_orders()
        print("\nReady to Serve Orders:")
        for order in orders:
            if order['status'] == "Completed":
                print(f"{order['customer_name']} - {order['item']} x{order['quantity']} ")
