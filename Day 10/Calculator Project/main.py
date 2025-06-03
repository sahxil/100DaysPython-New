import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return round((n1/n2), 2)

cont_calc = "y"
count = 0

while cont_calc == "y":
    if count == 0:
        first_no = int(input("Whats the first number?: "))
    print("+\n"+"-\n"+"*\n"+"/")
    operation_input = input("Pick an operation: ")
    second_no = int(input("What the next number?: "))

    #first_no here is out of bounds because it is initialized inside an if condition, however
    #that if condition always is true the first time because count was initialized as 0
    #outside the while loop

    operations = {
        "+": add(first_no, second_no),
        "-": subtract(first_no, second_no),
        "*": multiply(first_no, second_no),
        "/": divide(first_no, second_no)
    }

    print(f"{first_no} {operation_input} {second_no} = {operations[operation_input]}")
    cont_calc = input(f"Type 'y' to continue calculating with {operations[operation_input]}, or type 'n' to "
                      f"start a new calculation:")

    if cont_calc == "y":
        count += 1

    if count > 0:
        first_no = operations[operation_input]