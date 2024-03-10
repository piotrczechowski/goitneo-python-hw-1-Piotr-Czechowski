Function: add_contact
# Adds a contact (name, phone) to contacts dict.
# Parameters: args (list), contacts (dict)
# Returns: "Invalid command." or "Contact added."

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide name and phone number."    
    name, phone = args
    contacts[name] = phone
    return ("Contact added.")
