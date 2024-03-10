# Function: change_contact
# Updates phone number of a contact.
# Parameters: args (list), contacts (dict)
# Returns: "Invalid command." or "Contact not found." or "Contact updated."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide name and new phone number."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."