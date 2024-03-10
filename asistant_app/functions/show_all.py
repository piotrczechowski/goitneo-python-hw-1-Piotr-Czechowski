# Function: show_all
# Generates a string of all contacts.
# Parameters: contacts (dict)
# Returns: "No contacts found." or formatted contact list (str)

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])