from Authentication.admin_login import AdminManager
from Authentication.staff_login import StaffManager
from Authentication.customer_login import CustomerManager

def main_menu():
    while True:
        print("\n====== Restaurant Management System ======")
        print("1. Admin Panel")
        print("2. Staff Panel")
        print("3. Customer Panel")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin_dashboard()
        elif choice == '2':
            staff_dashboard()
        elif choice == '3':
            customer_dashboard()
        elif choice == '4':
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

def admin_dashboard():
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. Register Admin")
        print("2. Admin Login")
        print("3. View All Admins")
        print("4. Assign Role to Staff")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            AdminManager.register_admin()
        elif choice == '2':
            AdminManager.admin_login()
        elif choice == '3':
            AdminManager.show_all_admins()
        elif choice == '4':
            AdminManager.assign_staff_role()
        elif choice == '5':
            break
        else:
            print("Invalid input. Try again.")

def staff_dashboard():
    while True:
        print("\n--- Staff Dashboard ---")
        print("1. Register Staff")
        print("2. Staff Login")
        print("3. View All Staff")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            StaffManager.register_staff()
        elif choice == '2':
            StaffManager.staff_login()
        elif choice == '3':
            StaffManager.list_staff()
        elif choice == '4':
            break
        else:
            print("Invalid input. Try again.")

def customer_dashboard():
    while True:
        print("\n--- Customer Dashboard ---")
        print("1. Register Customer")
        print("2. Customer Login")
        print("3. View All Customers")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            CustomerManager.register_customer()
        elif choice == '2':
            CustomerManager.customer_login()
        elif choice == '3':
            CustomerManager.show_customers()
        elif choice == '4':
            break
        else:
            print("Invalid input. Try again.")

main_menu()