"""
Find the Second Largest Number in a List
Write a function that returns the second-largest number in a list.
Handle cases where the list is too short to have a second-largest number.
"""

def second_largest(numbers):
    # Your code here
    length = len(numbers)
    if length == 1:
        return 'List is too short!'
    else:
        sorted_list = sorted(numbers, reverse = True)
        for i in range(0, length):
            if sorted_list[i] > sorted_list[i+1]:
                return (sorted_list[i+1])
                break


"""
def second_largest(numbers):
    if len(numbers) < 2:
        return 'List is too short!'

    # Sort the list in reverse order (largest first)
    sorted_list = sorted(numbers, reverse=True)

    # Find the first element that is smaller than the largest element
    for num in sorted_list:
        if num < sorted_list[0]:
            return num

    return 'No second largest element found!'  # If all elements are the same
"""