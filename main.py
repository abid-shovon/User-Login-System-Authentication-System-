import time
import os

def animated_welcome_message():
    message = "Welcome to Login System"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def new_account():
    name = input("Enter your name: ").lower()
    age = int(input("Enter your age: "))
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    file_name = f"{username}.txt"
    with open(file_name, "w") as save:
        save.write(f"{name}\n")
        save.write(f"{age}\n")
        save.write(f"{username}\n")
        save.write(f"{password}\n")

    print("✅ Successfully created a new account.")

def login_account():
    username = input("Enter your username: ")
    password = input(f"Account name: {username}.\nPlease enter the password: ")

    file_name = f"{username}.txt"
    if not os.path.exists(file_name):
        print(" No account found with that username.")
        return

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            saved_password = lines[3].strip()

            if password == saved_password:
                print(" Successfully logged in.")
            else:
                print(" Incorrect password.")
    except Exception as e:
        print(" Something went wrong during login:", e)

def delete_account():
    username = input("Enter your username which you want to delete: ")
    password = input(f"Account name is {username}.\nPlease enter the password: ")

    file_name = f"{username}.txt"
    if not os.path.exists(file_name):
        print("No account found with that username.")
        return

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            saved_password = lines[3].strip()

        if password == saved_password:
            confirm = input(f"Are you sure you want to delete '{username}'? (Y/N): ").lower()
            if confirm == "y":
                os.remove(file_name)
                print(f" '{username}' deleted successfully.")
            else:
                print(" Deletion cancelled.")
        else:
            print(" Incorrect password.")
    except Exception as e:
        print(" Error while deleting account:", e)

def main():
    animated_welcome_message()
    while True:
        print('''
        1. Create a new account.
        2. Login your account.
        3. Delete your account.
        4. Exit.
        ''')
        try:
            selected = int(input("Which option do you want to select: "))
            if selected == 1:
                new_account()
            elif selected == 2:
                login_account()
            elif selected == 3:
                delete_account()
            elif selected == 4:
                print("👋 Exiting program...")
                break
            else:
                print(" Invalid option. Please choose 1 to 4.")
        except ValueError:
            print(" Please enter a number.")
        except Exception as e:
            print(" Something went wrong:", e)

        choice = input("Do you want to restart (Y/N)? ").lower()
        if choice != "y":
            break

main()
