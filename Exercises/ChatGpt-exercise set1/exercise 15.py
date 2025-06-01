"""
File Search
Write a Python function that takes a word as input and searches for the word in a given text file.
The function should return the line numbers where the word appears.
"""

import os

def search_word_in_file(word, file_name):
    # Your code here
    with open(file_name, 'r') as file:
        lines = file.readlines()
        i = 0
    number_of_lines = len(lines)
    for line in lines:
        i += 1
        if word in line:
            return i

"""
Correct Answer:

import os

def search_word_in_file(word, file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            lines = file.readlines()  # Read all lines into a list

        # Enumerate over lines to get both line number and line content
        for i, line in enumerate(lines, start=1):  # Start counting from 1
            # Check if the word is in the current line (case-insensitive)
            if word.lower() in line.lower():  # Convert both to lowercase for case-insensitive search
                return f"Word '{word}' found on line {i}."  # Return line number

        return f"Word '{word}' not found in the file."  # If the word is not found

    except FileNotFoundError:
        return f"The file '{file_name}' does not exist."  # Handle case where file does not exist
    except IOError:
        return "An error occurred while reading the file."  # Handle I/O errors
"""