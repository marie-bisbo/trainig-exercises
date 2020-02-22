def sort_list(chars: list) -> list:
    chars.sort(key=get_second_letter)
    return chars


def get_second_letter(letters: str) -> str:
    return letters[1]


print(sort_list(["kagergerg", "ocergergerg", "qboergoierjgeoirjg"]))
