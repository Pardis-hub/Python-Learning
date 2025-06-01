"""
 Remove Punctuation from a String
Write a function that removes all punctuation from a given string.
"""

import string

def remove_punctuation(s):
    # Your code here
    no_punctuation_s = ''.join(char for char in s if char not in string.punctuation)
    return no_punctuation_s

