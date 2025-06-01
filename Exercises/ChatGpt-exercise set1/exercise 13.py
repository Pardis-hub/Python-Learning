"""
Copy Content from One File to Another
Write a Python program that reads the contents of one file and writes them to another file.
"""

import os

def copy_file_content(source_file, target_file):
    # Your code here
    with open('source_file' , 'r') as file:
        content = file.read()
    with open('target_file' , 'w') as copy:
        copy.write(content)

"""
import os

def copy_file_content(source_file, target_file):
    # Your code here
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as file:
            content = file.read()  # Read the content from the source file

        # Open the target file in write mode
        with open(target_file, 'w') as copy:
            copy.write(content)  # Write the content to the target file

        print(f"Content copied from {source_file} to {target_file}.")  # Optional success message

    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")  # Handle case where source file does not exist
    except IOError:
        print("An error occurred while writing to the target file.")  # Handle I/O errors
"""