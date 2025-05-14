from Authentication.admin_login import AdminManager
from Authentication.staff_login import StaffManager
from Authentication.customer_login import CustomerManager
from menu_management.menu_management import MenuManager

def main_menu():
    while True:
        print("\n====== Vishal Restaurant Management System veg only ======")
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
        print("\n--- Admin Access ---")
        print("1. Login")
        print("2. Signup")
        print("3. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            if AdminManager.admin_login():
                admin_panel()
        elif choice == '2':
            AdminManager.register_admin()
        elif choice == '3':
            break
        else:
            print("Invalid input. Try again.")

def admin_panel():  
    while True:
        print("\n--- Admin Dashboard ---")
        print("1. View All Admins")
        print("2. Assign Role to Staff")
        print("3. Manage Menu")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            AdminManager.show_all_admins()
        elif choice == '2':
            if hasattr(AdminManager, 'assign_staff_role'):
                AdminManager.assign_staff_role()
            else:
                print("Assign Role feature not implemented yet.")
        elif choice == '3':
            while True:
                print("\n--- Vishal Restaurant Menu Management ---")
                print("1. Add Menu Item")
                print("2. View Menu")
                print("3. Back")

                opt = input("Choose an option: ")

                if opt == '1':
                    MenuManager.add_menu_item()
                elif opt == '2':
                    MenuManager.view_menu()
                elif opt == '3':
                    break
                else:
                    print("Invalid choice.")
        elif choice == '4':
            break
        else:
            print("Invalid input. Try again.")

def staff_dashboard():
    while True:
        print("\n--- Staff Access ---")
        print("1. Login")
        print("2. Signup")
        print("3. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            if StaffManager.staff_login():
                print("Staff options coming soon!")  
        elif choice == '2':
            StaffManager.register_staff()
        elif choice == '3':
            break
        else:
            print("Invalid input. Try again.")

def customer_dashboard():
    while True:
        print("\n--- Customer Access ---")
        print("1. Login")
        print("2. Signup")
        print("3. Back")
        choice = input("Choose an option: ")

        if choice == '1':
            if CustomerManager.customer_login():
                print("Customer options coming soon!")  
        elif choice == '2':
            CustomerManager.register_customer()
        elif choice == '3':
            break
        else:
            print("Invalid input. Try again.")

main_menu()
