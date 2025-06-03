def format_name(f_name, l_name):
    """Returns formatted name"""
    if f_name == "" or l_name == "":
        return None
    else:
        first = f_name.title()
        last = l_name.title()
        name = first + " " + last
        return name

print(format_name(input("Enter first name:\n"), input("Enter last name:\n")))
