# import os
# import json
# import re
# import msvcrt

# class AdminManager:
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     admin_file = os.path.join(base_dir, '..', 'Database', 'admin_data.json')

#     @classmethod
#     def ensure_folder_exists(cls):
#         folder = os.path.dirname(cls.admin_file)
#         if not os.path.exists(folder):
#             os.makedirs(folder)

#     @classmethod
#     def write_json(cls, filename, data):
#         cls.ensure_folder_exists()
#         with open(filename, 'w') as file:
#             json.dump(data, file, indent=4)

#     @classmethod
#     def load_json(cls, filename):
#         if os.path.exists(filename):
#             with open(filename, 'r') as file:
#                 return json.load(file)
#         return []

#     @classmethod
#     def input_password(cls, prompt="Password: "):
#         print(prompt, end="", flush=True)
#         password = ""
#         while True:
#             char = msvcrt.getch()
#             if char in {b"\r", b"\n"}:
#                 print()
#                 break
#             elif char == b"\x08":  # backspace
#                 if password:
#                     password = password[:-1]
#                     print("\b \b", end="", flush=True)
#             else:
#                 password += char.decode("utf-8")
#                 print("*", end="", flush=True)
#         return password

#     @classmethod
#     def is_valid_password(cls, password):
#         if len(password) < 6:
#             return False
#         if not re.search(r"[A-Za-z]", password):
#             return False
#         if not re.search(r"\d", password):
#             return False
#         if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#             return False
#         return True

#     @classmethod
#     def register_admin(cls):
#         admin_list = cls.load_json(cls.admin_file)

#         if admin_list:
#             print("\n Admin already exists. Signup is allowed only once.\n")
#             return

#         name = input("Admin Name: ")
#         email = input("Email: ")

#         while True:
#             password = cls.input_password("Password: ")
#             if cls.is_valid_password(password):
#                 break
#             else:
#                 print(" Weak password. Use at least 6 characters including letter, number & special character.")

#         admin_list.append({"name": name, "email": email, "password": password})
#         cls.write_json(cls.admin_file, admin_list)
#         print("\n Admin registered successfully!\n")

#     @classmethod
#     def admin_login(cls):
#         email = input("Email: ")
#         password = cls.input_password("Password: ")

#         admin_list = cls.load_json(cls.admin_file)

#         for admin in admin_list:
#             if admin["email"] == email and admin["password"] == password:
#                 print(f"\n Welcome, {admin['name']}!\n")
#                 return True

#         print("\n Invalid email or password. Please try again.\n")
#         return False

# @classmethod
# def show_all_admins(cls):
#     admins = cls.load_json(cls.admin_file)
#     if not admins:
#         print("\nNo admin found.\n")
#         return
#     print("\nRegistered Admins:")
#     for i, admin in enumerate(admins, 1):
#         print(f"{i}. Name: {admin['name']}, Email: {admin['email']}")



import os
import json
import re
import msvcrt

class AdminManager:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    admin_file = os.path.join(base_dir, '..', 'Database', 'admin_data.json')

    @classmethod
    def ensure_folder_exists(cls):
        folder = os.path.dirname(cls.admin_file)
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
            elif char == b"\x08":  # backspace
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
    def register_admin(cls):
        admin_list = cls.load_json(cls.admin_file)

        if admin_list:
            print("\n Admin already exists. Signup is allowed only once.\n")
            return

        name = input("Admin Name: ")
        email = input("Email: ")

        while True:
            password = cls.input_password("Password: ")
            if cls.is_valid_password(password):
                break
            else:
                print(" Weak password. Use at least 6 characters including letter, number & special character.")

        admin_list.append({"name": name, "email": email, "password": password})
        cls.write_json(cls.admin_file, admin_list)
        print("\n Admin registered successfully!\n")

    @classmethod
    def admin_login(cls):
        email = input("Email: ")
        password = cls.input_password("Password: ")

        admin_list = cls.load_json(cls.admin_file)

        for admin in admin_list:
            if admin["email"] == email and admin["password"] == password:
                print(f"\n Welcome, {admin['name']}!\n")
                return True

        print("\n Invalid email or password. Please try again.\n")
        return False

    @classmethod
    def show_all_admins(cls):
        admins = cls.load_json(cls.admin_file)
        if not admins:
            print("\nNo admin found.\n")
            return
        print("\n--- Registered Admins ---")
        for i, admin in enumerate(admins, 1):
            print(f"{i}. Name: {admin['name']}, Email: {admin['email']}")
