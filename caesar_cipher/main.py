ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(message, shift_n):
    message_letters = list(message)
    encoded_line = ""
    for letter in message_letters:
        if letter in ALPHABET:
            encoded_line += ALPHABET[ALPHABET.index(letter) - shift_n]
        else:
            encoded_line += letter
    return encoded_line


def decode(message, shift_n):
    message_letters = list(message)
    encoded_line = ""
    for letter in message_letters:
        if letter in ALPHABET:
            new_ind = ALPHABET.index(letter) + shift_n
            if new_ind > len(ALPHABET)-1:
                new_ind -= len(ALPHABET)
            encoded_line += ALPHABET[new_ind]
        else:
            encoded_line += letter
    return encoded_line


go_on = True
while go_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    if direction not in ['encode', 'decode']:
        print("Incorrect input.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 30:
            shift = shift%30

        if direction == "encode":
            print(f"Result: {encode(text, shift)}")
        elif direction == "decode":
            print(f"Result: {decode(text, shift)}")

    try_again = input("Type 'Y' to return to the main menu: ").upper()
    if try_again != "Y":
        go_on = False