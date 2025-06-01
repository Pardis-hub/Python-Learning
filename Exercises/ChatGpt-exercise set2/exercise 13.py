"""
 Rotate a List
Write a function that rotates a list by a given number of positions.
"""
"""
My Answer:
def rotate_list(lst, positions):
    if len(lst) <= positions:
        return 'Not enough items in the list!'
    elif positions == 0:
        return lst
    return lst[positions:] + lst[0:positions]
"""

def rotate_list(lst, positions):
    if not lst:  # Check for empty list
        return "List is empty!"

    positions = positions % len(lst)  # Handle cases where positions > len(lst)

    return lst[positions:] + lst[:positions]






print(rotate_list([1, 2, 3, 4, 5], 2))