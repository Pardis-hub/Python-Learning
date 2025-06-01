"""
String Manipulation
Write a Python function that takes a string and returns a dictionary
containing the frequency of each character in the string.
"""

def char_frequency(s):
    # Your code here
    length = len(s)
    string = s.lower()
    frequency_dict = {}

    for i in range(length):
       if string[i] in frequency_dict.key():
           frequency_dict[string[i]] += 1
       else:
           frequency_dict[string[i]] = 1

    return frequency_dict

"""
def char_frequency(s):
    string = s.lower()
    frequency_dict = {}

    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict
"""