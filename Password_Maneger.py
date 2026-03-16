import pyperclip
import os

FILE_NAME = "passwords.txt"
def save_password():
    website = input("Enter the website: ").strip()
    password = input("Enter the password: ").strip()
    with open(FILE_NAME, 'a') as f:
        f.write(f"{website} | {password}\n")
    print("Password saved successfully!")


def get_password():
    website = input("Enter website : ")
    with open(FILE_NAME, 'r') as f:
        for line in f:
            if website in line:
                password = line.split('|')[1].strip()
                pyperclip.copy(password)
                print("Password copied to clipboard!")
                break
        else:
            print("Website not found.")
            

def main():
    while True:
        print("\nPassword Manager")
        print("1) Save a new password")
        print("2) Get a password")
        print("3) Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == '3':
            print("Exiting...!")
            break
        elif choice == '1':
            save_password()
        elif choice == '2':
            get_password()
        else:
            print("Invalid choice. Please choose 1-3.")
main()