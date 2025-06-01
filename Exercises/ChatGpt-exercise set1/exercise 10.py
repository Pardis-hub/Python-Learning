"""
List Operations
Write a program that takes a list of numbers and:

  Returns the sum of the numbers
  Returns the largest and smallest number in the list
  Returns a sorted version of the list
"""

def list_operations(numbers):
    # Your code here
    length = len(numbers)
    min = max = numbers[0]
    sum = 0
    for i in numbers:
        sum += i
        if i > max:
            max = i
        if i < min:
            min = i
    sorted_numbers = sorted(numbers)
    #WRONG: return 'SUM =' , sum , 'MAX = ', max, 'MIN =', min, 'Sorted Numbers =' , sorted_numbers
    return f'SUM = {sum}, MAX = {max}, MIN = {min}, Sorted Numbers = {sorted_numbers}'