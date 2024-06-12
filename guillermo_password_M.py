import hashlib
import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init()

# Dictionary to store username and hashed passwords
user_data = {}

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def register_user():
    username = input("Enter a username: ")
    choice = input("Would you like to generate a strong password? (yes/no): ").strip().lower()

    if choice == 'yes':
        password = generate_password()
        print(f"Generated password: {password}")
    else:
        password = input("Enter a password: ")

    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    user_data[username] = hashed_pass
    print("User registered successfully!")

def authenticate_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    if username in user_data and user_data[username] == hashed_pass:
        print(Fore.GREEN + "Login successful!, you are in!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid username or password." + Style.RESET_ALL)

def main():
    while True:
        print("1. Register\n2. Login\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            authenticate_user()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
