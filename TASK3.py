import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def add_contact(name, phone_number, email):
    contacts[name] = {'phone_number': phone_number, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("Contact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone Number: {info['phone_number']}, Email: {info['email']}")

def edit_contact(name):
    if name in contacts:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {'phone_number': phone_number, 'email': email}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

contacts = load_contacts()

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone_number, email)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter name of the contact to edit: ")
            edit_contact(name)
        elif choice == '4':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
