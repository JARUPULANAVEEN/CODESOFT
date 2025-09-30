contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['phone']}")

def search_contact():
    keyword = input("Search by name or phone: ")
    found = False
    for c in contacts:
        if keyword.lower() in c['name'].lower() or keyword in c['phone']:
            print(c)
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input(f"Enter new phone [{c['phone']}]: ") or c['phone']
            c['email'] = input(f"Enter new email [{c['email']}]: ") or c['email']
            c['address'] = input(f"Enter new address [{c['address']}]: ") or c['address']
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted.")
            return
    print("Contact not found.")

while True:
    print("\nContact Manager Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Try again.")

     