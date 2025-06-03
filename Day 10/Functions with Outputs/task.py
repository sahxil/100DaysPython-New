def format_name(f_name, l_name):
        first = f_name.title()
        last = l_name.title()
        name = first + last
        return name

format_name(input("Enter first name:\n"), input("Enter last name:\n"))
