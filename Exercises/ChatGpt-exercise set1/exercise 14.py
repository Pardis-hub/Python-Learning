"""
Count Words in a File
Write a Python function that reads a file and counts the total number of words in it.
"""

import os


def count_words_in_file(file_path):
    try:
        # Step 1: Open the file in read mode
        with open(file_path, 'r') as file:
            # Step 2: Read the content
             content = file.read()

        # Step 3: Split the content into words
        words = content.split()  # This splits the content by whitespace

        # Step 4: Count the words
        word_count = len(words)  # Get the number of words

        return word_count  # Return the word count

    except FileNotFoundError:
            print(f"The file {file_path} does not exist.")  # Handle case where file does not exist
    except IOError:
            print("An error occurred while reading the file.")  # Handle I/O errors