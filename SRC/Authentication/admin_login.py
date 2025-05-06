import json
import os
import uuid

class AdminManager:
    admin_file = os.path.join('Database', 'admins.json')
    staff_file = os.path.join('Database', 'staff_data.json')

    @staticmethod
    def read_json(file_path):
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return []
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_json(file_path, data):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def register_admin(cls):
        admin_name = input("Admin Name: ")
        admin_address = input("Address: ")
        admin_contact = input("Contact Number: ")
        admin_id = str(uuid.uuid4())[:8]

        new_admin = {
            "admin_id": admin_id,
            "name": admin_name,
            "address": admin_address,
            "contact": admin_contact
        }

        admin_list = cls.read_json(cls.admin_file)
        admin_list.append(new_admin)
        cls.write_json(cls.admin_file, admin_list)
        print(f"Admin '{admin_name}' registered successfully!")

    @classmethod
    def admin_login(cls):
        name = input("Enter Name: ")
        contact = input("Enter Contact Number: ")

        admins = cls.read_json(cls.admin_file)
        for admin in admins:
            if admin["name"] == name and admin["contact"] == contact:
                print(f"Welcome {name}, login successful!")
                return True
        print("Login failed! Invalid credentials.")
        return False

    @classmethod
    def show_all_admins(cls):
        admins = cls.read_json(cls.admin_file)
        if not admins:
            print("No admin records found.")
        else:
            print("Registered Admins:")
            for admin in admins:
                print(f"ID: {admin['admin_id']}, Name: {admin['name']}, Contact: {admin['contact']}")

    @classmethod
    def assign_staff_role(cls):
        staff_data = cls.read_json(cls.staff_file)
        if not staff_data:
            print("No staff available to assign role.")
            return

        print("Available Staff Members:")
        for idx, staff in enumerate(staff_data):
            print(f"{idx+1}. {staff['name']} (ID: {staff['staff_id']})")

        try:
            choice = int(input("Choose staff number to assign role: ")) - 1
            if 0 <= choice < len(staff_data):
                role = input("Enter Role (e.g., manager, chef): ")
                staff_data[choice]['role'] = role
                cls.write_json(cls.staff_file, staff_data)
                print("Role assigned successfully.")
            else:
                print("Invalid staff selection.")
        except ValueError:
            print("Please enter a valid number.")




