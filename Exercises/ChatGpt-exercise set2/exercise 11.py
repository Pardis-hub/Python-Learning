"""
 Find Intersection of Two Lists
Write a function that returns the common elements between two lists.
"""

def intersection(list1, list2):
    mutual = []
    if list1 == [] or list2 == []:
        return 'List can not be empty!'

    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                mutual.append(item2)
                break
    if mutual == []:
        return 'No intersection!'
    return mutual


"""
Improved version:
def intersection(list1, list2):
    # Check for empty lists
    if not list1 or not list2:
        return 'List can not be empty!'
    
    # Convert list2 to a set for faster lookups
    set2 = set(list2)
    mutual = [item for item in list1 if item in set2]
    
    return mutual if mutual else 'No intersection!'
"""




print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))