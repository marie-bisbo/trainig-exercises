import string

lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)


def encode(message: str, shift: int) -> str:
    shifted_message = ""
    for letter in message:
        if letter in lowercase_alphabet:
            shifted_message += shift_letter(letter, shift, lowercase_alphabet)
        elif letter in uppercase_alphabet:
            shifted_message += shift_letter(letter, shift, uppercase_alphabet)
        else:
            shifted_message += letter
    return shifted_message


def shift_letter(letter: str, shift: int, alphabet: list):
    return alphabet[(alphabet.index(letter) + shift) % 26]


def decode(encoded_message: str, shift: int) -> str:
    return encode(encoded_message, -shift)


print(encode("This is a message!", 1))
