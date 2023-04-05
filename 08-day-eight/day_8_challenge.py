# A caesar cipher function that takes in a string and a shift amount and then outputs the modified string.

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(input_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        else:
            output_text += char
    print(f"The {cipher_direction}d text is {output_text}")


print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar_cipher(input_text=text, shift_amount=shift,
                  cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
