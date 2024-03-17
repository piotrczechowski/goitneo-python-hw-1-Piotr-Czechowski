def parse_input(user_input):

    cmd, *args = user_input.split()
   
    #command lower case
    cmd = cmd.strip().lower()
    return cmd, args

