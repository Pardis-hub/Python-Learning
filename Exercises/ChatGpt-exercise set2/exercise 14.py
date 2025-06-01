"""
File Line Counter
Write a function that counts the number of lines in a file.
"""

def count_lines(file_name):
    with open(file_name, 'r') as file:
        return len(file.readlines())

"""
def count_lines(file_name):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            count += 1
    return count
"""


