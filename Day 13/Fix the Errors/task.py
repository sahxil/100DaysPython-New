try:
    age = int(input("How old are you?"))
    if age > 18:
        print(f"You can drive at age {age}.")

except ValueError:
    print("You can't mix integers and string in a comparison")
