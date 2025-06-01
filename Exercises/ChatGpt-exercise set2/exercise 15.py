"""
Group Elements of a List by Length
Write a function that groups the elements of a list of strings by their lengths into a dictionary,
where the keys are the lengths and the values are lists of strings of that length.
"""


def group_by_length(strings):
    length_dict = {}

    for string in strings:
        length = len(string)
        if length not in length_dict:
            length_dict[length] = []  # Initialize the list if the length key doesn't exist
        length_dict[length].append(string)  # Append the string to the corresponding length key

    return length_dict


print(group_by_length(["apple", "banana", "cherry", "dog", "cat"]))
# Output: {5: ["apple"], 6: ["banana", "cherry"], 3: ["dog", "cat"]}