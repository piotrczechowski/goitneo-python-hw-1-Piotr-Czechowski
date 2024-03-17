from functions import parse_input, add_contact, change_contact, show_all, show_phone

def main():
    contacts = {}
    
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
        except ValueError:
            print ("Empty spaces is not allowed.")
            print ("Please chose action: hello, add, change, phone, all.")
        
        try:
            if command in ["close", "exit"]:
                print("Goodbye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except UnboundLocalError:
            print("Please provide command.")

if __name__ == "__main__":
    main()
