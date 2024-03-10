# Function: parse_input
# Parses user input into a command and its arguments.
# Parameters: user_input (str)
# Returns: cmd (str), args (list)

def parse_input(user_input):

    cmd, *args = user_input.split()
   
    #command lower case
    cmd = cmd.strip().lower()
    return cmd, args

