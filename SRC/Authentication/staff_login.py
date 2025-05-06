import json
import os
import uuid

class StaffManager:
    file_path = 'Database/staff_data.json'

    @staticmethod
    def read_staff():
        if not os.path.exists(StaffManager.file_path) or os.path.getsize(StaffManager.file_path) == 0:
            return []
        with open(StaffManager.file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def write_staff(data):
        with open(StaffManager.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def register_staff(cls):
        sname = input("Staff Name: ")
        saddress = input("Address: ")
        scontact = input("Contact Number: ")
        sid = str(uuid.uuid4())[:8]

        new_staff = {
            "staff_id": sid,
            "name": sname,
            "address": saddress,
            "contact": scontact,
            "role": None
        }

        staff_list = cls.read_staff()
        staff_list.append(new_staff)
        cls.write_staff(staff_list)
        print(f"Staff '{sname}' registered successfully!")

    @classmethod
    def staff_login(cls):
        sname = input("Enter Name: ")
        scontact = input("Enter Contact Number: ")

        staff_list = cls.read_staff()
        for staff in staff_list:
            if staff["name"] == sname and staff["contact"] == scontact:
                print(f"Welcome {sname}, login successful!")
                print("Role:", staff.get("role", "Not assigned"))
                return True
        print("Login failed. Incorrect details.")
        return False

    @classmethod
    def list_staff(cls):
        staff_list = cls.read_staff()
        if not staff_list:
            print("No staff records found.")
            return

        print("Staff Members:")
        for s in staff_list:
            print(f"ID: {s['staff_id']}, Name: {s['name']}, Contact: {s['contact']}, Role: {s.get('role', 'N/A')}")