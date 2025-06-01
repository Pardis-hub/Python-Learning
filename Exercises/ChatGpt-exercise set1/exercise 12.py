"""
Write and Read from a File
Create a Python function that writes user input to a file and then reads it back.
"""
import os

def write_and_read_file(input):
    # Your code here
    with open('file_name.txt' , '+') as file:
        file.write(input)
        content = file.read()
    return content

"""
Corrected Answer:

import os 

def write_and_read_file(data):  # Use 'data' instead of 'input'
    # Open the file in write and read mode
    with open('file_name.txt', 'w+') as file:  # Use 'w+' to create/overwrite and read
        file.write(data)  # Write data to the file
        file.seek(0)  # Move the pointer to the beginning of the file to read the content
        content = file.read()  # Read the content of the file
    return content  # Return the content read from the file
"""