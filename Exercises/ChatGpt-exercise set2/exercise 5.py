"""
 Find Unique Words in a File
Write a function that reads a file and returns a list of unique words (case-insensitive).
"""
import os

def unique_words(file_name):
    # Your code here
    word_count = {}
    unique = []

    with open(file_name, 'r') as file:
        content = file.read().split()

    for word in content:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        if count == 1:
            unique.append(word)

    return unique