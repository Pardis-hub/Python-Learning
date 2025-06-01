"""
Convert List of Tuples to Dictionary
Write a function that converts a list of tuples into a dictionary, where the first element of each tuple is the key and the second is the value.
"""

def list_to_dict(tuples):
    # Your code here
    result_dict = {}
    for tuple in tuples:
        result_dict[tuple[0]] = tuple[1]
    return result_dict

print(list_to_dict([("apple", 1), ("banana", 2)]))