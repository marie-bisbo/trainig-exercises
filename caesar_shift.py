import string

LOWERCASE_ALPHABET = list(string.ascii_lowercase)
UPPERCASE_ALPHABET = list(string.ascii_uppercase)


def encode(message: str, shift: int) -> str:
    encoded_message = "".join((shift_letter(letter, shift) for letter in message))
    return encoded_message


def decode(encoded_message: str, shift: int) -> str:
    return encode(encoded_message, -shift)


def shift_letter(letter: str, shift: int) -> str:
    letter = (
        check_case(letter, shift, LOWERCASE_ALPHABET)
        if letter in LOWERCASE_ALPHABET
        else check_case(letter, shift, UPPERCASE_ALPHABET)
        if letter in UPPERCASE_ALPHABET
        else letter
    )
    return letter


def check_case(letter: str, shift: int, alphabet: list) -> str:
    return alphabet[(alphabet.index(letter) + shift) % 26]


print(encode("This is a message!", 1))
