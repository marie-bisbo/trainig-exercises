# ** * Write a function `sortList()` which takes a list of strings as input
#  * and outputs the same list sorted into alphabetical order by their second
#  * letter. It should be case-insensitive.
#  * It should remove words from the list that are only one letter long or empty.
#  *
#  * Examples:
#  *  sortList(['formalise', 'automate', 'share', 'test']) ===
#  *     ['test', 'share', 'formalise', 'automate'];
#  *  sortList(['i', 'love', 'php']) === ['php', 'love'];
#  */
#
# function sortList(array $list): array
# {
#     return [];
# }


def sort_list(chars: list):
    chars.sort(key=get_second_letter)
    return chars


def get_second_letter(letters: str) -> str:
    return letters[1]


print(sort_list(["kagergerg", "ocergergerg", "qboergoierjgeoirjg"]))
