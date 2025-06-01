"""
Palindrome Checker
Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).
"""

def is_palindrome(s):
    # Your code here
    i = -1
    string = s.lower()
    for char in string:
        backwards[i] = char
        i -= 1
    if string == backwards:
        return 'True'
    else:
        return 'False'

"""
Correct answer:

def is_palindrome(s):
    string = s.lower()  # Convert to lowercase for case-insensitive comparison
    backwards = string[::-1]  # Reverse the string using slicing
    
    if string == backwards:
        return True  # Return True for a palindrome
    else:
        return False  # Return False otherwise

Optional Improvement:
 
def is_palindrome(s):
    string = ''.join(char.lower() for char in s if char.isalnum())  # Filter non-alphabetic chars and lowercase
    return string == string[::-1]  # Check if the string is equal to its reverse        
"""