"""
Count Words in a String with Recursion
Write a recursive function to count the number of words in a string.
"""
"""
#My answer:
def count_words_recursive(s):
    for index, char in enumerate(s):
        if char == ' ':
            return 1 + count_words_recursive(s[index + 1:])
    return 1
"""


def count_words_recursive(s):
    # Base case: if the string is empty, no words are left
    if not s:
        return 0

    # Recursive case: count one word when the first space is found
    for index, char in enumerate(s):
        if char == ' ':
            # Avoid counting multiple spaces
            return 1 + count_words_recursive(s[index + 1:].lstrip())

    # If no spaces are left, count the remaining segment as one word
    return 1

print(count_words_recursive("I am learning Python"))