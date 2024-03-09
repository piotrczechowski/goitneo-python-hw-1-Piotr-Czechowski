# parser to provide command and values: cmd command and *args 
def parse_input(user_input):
    cmd, *args = user_input.split()
    #command lower case
    cmd = cmd.strip().lower()
    return cmd, args 