# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue_command = "yes"

def caesar(direction_type, original_text, shift_amount):
    ciphered_text = ""
    if direction_type == "decode":
        shift_amount *= -1

    for i in original_text:
        if i not in alphabet:
            ciphered_text += i
        else:
            index_value = alphabet.index(i)
            step = (index_value + shift_amount) % 26
            ciphered_text += alphabet[step]

    print(f"Ciphered text is {ciphered_text}")


while continue_command == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    continue_command = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")



