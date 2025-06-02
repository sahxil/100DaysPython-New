# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction_type, original_text, shift_amount):
    ciphered_text = ""
    if direction_type == "decode":
        shift_amount *= -1
    for i in original_text:
        index_value = alphabet.index(i)
        step = (index_value + shift_amount) % 26
        ciphered_text += alphabet[step]

    print(ciphered_text)

caesar(direction, text, shift)




