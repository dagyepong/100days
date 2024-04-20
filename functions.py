#  functions with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

# doc strings 

""" This is an example of a docstring"""