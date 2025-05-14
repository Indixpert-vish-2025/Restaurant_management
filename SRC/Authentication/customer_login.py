import json
import os
import uuid

class CustomerManager:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, 'Database', 'customers.json')


    @staticmethod
    def read_customers():
        if not os.path.exists(CustomerManager.file_path) or os.path.getsize(CustomerManager.file_path) == 0:
            return []
        with open(CustomerManager.file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_customers(data):
        with open(CustomerManager.file_path, 'w') as f:
            json.dump(data, f, indent=4)

@classmethod
def register_customer(cls):
    name = input("Customer Name: ")
    email = input("Email: ")
    password = input("Password: ")
    customer_id = str(uuid.uuid4())[:8]

    new_customer = {
        "customer_id": customer_id,
        "name": name,
        "email": email,
        "password": password
    }

    data = cls.read_customers()
    data.append(new_customer)
    cls.write_customers(data)
    print(f"Customer '{name}' registered successfully!")

@classmethod
def customer_login(cls):
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    data = cls.read_customers()
    for customer in data:
        if customer["email"] == email and customer["password"] == password:
            print(f"Welcome {customer['name']}, login successful!")
            return True
    print("Login failed! Incorrect credentials.")
    return False

    @classmethod
    def show_customers(cls):
        customers = cls.read_customers()
        if not customers:
            print("No customers found.")
        else:
            print("Customer List:")
            for cust in customers:
                print(f"ID: {cust['customer_id']}, Name: {cust['name']}, Phone: {cust['phone']}")