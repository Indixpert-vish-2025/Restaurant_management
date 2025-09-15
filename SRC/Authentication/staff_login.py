import os
import json
import re
import msvcrt

class StaffManager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    staff_file = os.path.join(base_dir, '..', 'Database', 'staff_data.json')

    @classmethod
    def ensure_folder_exists(cls):
        folder = os.path.dirname(cls.staff_file)
        if not os.path.exists(folder):
            os.makedirs(folder)

    @classmethod
    def write_json(cls, filename, data):
        cls.ensure_folder_exists()
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_json(cls, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return []

    @classmethod
    def input_password(cls, prompt="Password: "):
        print(prompt, end="", flush=True)
        password = ""
        while True:
            char = msvcrt.getch()
            if char in {b"\r", b"\n"}:
                print()
                break
            elif char == b"\x08":
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            else:
                password += char.decode("utf-8")
                print("*", end="", flush=True)
        return password

    @classmethod
    def is_valid_password(cls, password):
        if len(password) < 6:
            return False
        if not re.search(r"[A-Za-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

    @classmethod
    def register_staff(cls):
        name = input("Staff Name: ")
        email = input("Email: ")

        while True:
            password = cls.input_password("Password: ")
            if cls.is_valid_password(password):
                break
            else:
                print(" Weak password. Use at least 6 characters including letter, number & special character.")

        staff_list = cls.load_json(cls.staff_file)
        staff_list.append({"name": name, "email": email, "password": password})
        cls.write_json(cls.staff_file, staff_list)
        print(f"\nStaff '{name}' registered successfully!\n")

    @classmethod
    def staff_login(cls):
        email = input("Email: ")
        password = cls.input_password("Password: ")

        staff_list = cls.load_json(cls.staff_file)
        for staff in staff_list:
            if staff["email"] == email and staff["password"] == password:
                print(f"\nWelcome, {staff['name']} (Staff)!\n")
                return True

        print("\nInvalid email or password. Please try again.\n")
        return False
