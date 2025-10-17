# Contact Book using Python
# Features: Add, View, Search, Delete Contacts

contacts = []  # List to store all contacts


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"\n Contact '{name}' added successfully!\n")


def view_contacts():
    if not contacts:
        print("\n📭 No contacts found!\n")
        return
    print("\n All Contacts:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()


def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print(f"\n Found: {contact['name']} - {contact['phone']} - {contact['email']}\n")
            found = True
            break
    if not found:
        print("\n No contact found with that name.\n")


def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == delete_name:
            contacts.remove(contact)
            print(f"\n Contact '{contact['name']}' deleted successfully!\n")
            return
    print("\n No contact found with that name.\n")


def main():
    while True:
        print("=====  CONTACT BOOK MENU =====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\n Exiting Contact Book. Goodbye!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
