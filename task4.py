def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
  
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
  
def change_contact(name, new_phone, contacts):
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' updated to {new_phone}."
    else:
        return f"Contact '{name}' not found."
      
def delete_contact(name, contacts):
    if name in contacts:
        del contacts[name]
        return f"Contact '{name}' deleted."
    else:
        return f"Contact '{name}' not found."
      
def show_contact(name, contacts):
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "No contacts found."
      
def show_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            name, new_phone = args
            print(change_contact(name, new_phone, contacts))
        elif command == "delete":
            name = args[0]
            print(delete_contact(name, contacts))
        elif command == "phone":
            name = args[0]
            print(show_contact(name, contacts))
        elif command == "all":
            print(show_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
