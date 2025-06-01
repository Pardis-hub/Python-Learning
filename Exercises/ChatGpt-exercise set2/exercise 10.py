"""
Zip Two Lists into a Dictionary
Write a function that takes two lists (of the same length) and returns a dictionary,
where the elements of the first list are the keys, and the elements of the second list are the values.
"""

def lists_to_dict(keys, values):
    # Your code here
    result_dict = {}
    for i in range(0, len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict


"""
def lists_to_dict(keys, values):
    return dict(zip(keys, values))
"""