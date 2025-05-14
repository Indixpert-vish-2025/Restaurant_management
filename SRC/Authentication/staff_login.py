import json
import uuid
import os

class StaffManager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    staff_file_path = os.path.join(base_dir, '..', 'database', 'staff_data.json')

    @classmethod
    def read_json(cls, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    @classmethod
    def write_json(cls, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def register_staff(cls):
        name = input("Staff Name: ")
        email = input("Email: ")
        password = input("Password: ")
        staff_id = str(uuid.uuid4())[:8]

        new_staff = {
            "staff_id": staff_id,
            "name": name,
            "email": email,
            "password": password
        }

        staff_list = cls.read_json(cls.staff_file_path)
        staff_list.append(new_staff)
        cls.write_json(cls.staff_file_path, staff_list)
        print(f"Staff '{name}' registered successfully!")

    @classmethod
    def login_staff(cls):
        email = input("Email: ")
        password = input("Password: ")

        staff_list = cls.read_json(cls.staff_file_path)
        for staff in staff_list:
            if staff["email"] == email and staff["password"] == password:
                print(f"\nWelcome Staff: {staff['name']}")
                return True
        print("Invalid credentials. Try again.")
        return False
