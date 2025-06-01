"""
Anagram Checker
Write a function that checks whether two strings are anagrams (case-insensitive).
Two strings are anagrams if they contain the same characters in any order.
"""

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return 'False'

    lower_s1 = list(s1.lower())
    lower_s2 = list(s2.lower())
    sorted_s1 = sorted(lower_s1)
    sorted_s2 = sorted(lower_s2)

    if sorted_s1 == sorted_s2:
        return 'True'
    else:
        return 'False'

"""
OR:
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return 'False'
    
    return 'True' if sorted(s1.lower()) == sorted(s2.lower()) else 'False'
"""

print(is_anagram("Listen", "Silent"))
