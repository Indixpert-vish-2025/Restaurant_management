import json
import os
import uuid

class CustomerManager:
    file_path = 'Database/customers.json'

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
        cname = input("Customer Name: ")
        cphone = input("Mobile Number: ")
        caddress = input("Address: ")
        cid = str(uuid.uuid4())[:8]

        new_customer = {
            "customer_id": cid,
            "name": cname,
            "phone": cphone,
            "address": caddress
        }

        data = cls.read_customers()
        data.append(new_customer)
        cls.write_customers(data)
        print(f"Customer '{cname}' registered successfully!")

    @classmethod
    def customer_login(cls):
        cname = input("Enter Name: ")
        cphone = input("Enter Mobile Number: ")

        data = cls.read_customers()
        for customer in data:
            if customer["name"] == cname and customer["phone"] == cphone:
                print(f"Welcome {cname}, login successful!")
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