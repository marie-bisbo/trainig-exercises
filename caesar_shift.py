import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)


def encode(message: str, shift: int) -> str:
    shifted_message = ""
    for letter in message:
        shifted_message += (
            shift_letter(letter, shift, lowercase_alphabet)
            if letter in lowercase_alphabet
            else shift_letter(letter, shift, uppercase_alphabet)
            if letter in uppercase_alphabet
            else letter
        )
    return shifted_message


def shift_letter(letter: str, shift: int, alphabet: list):
    return alphabet[(alphabet.index(letter) + shift) % 26]


def decode(encoded_message: str, shift: int) -> str:
    return encode(encoded_message, -shift)


print(encode("This is a message!", 1))
