"""
Most Frequent Word in a String
Write a function that returns the most frequent word in a given string. Ignore case and punctuation.
"""
import string

def most_frequent_word(s):
    # Your code here
    word_count = {}
    most_frequent = []

    s_no_punctuation = ''.join(char for char in s if char not in string.punctuation)
    final_string = s_no_punctuation.lower().split()

    for word in final_string:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    frequency = sorted(word_count.values(), reverse = True)

    for key, value in word_count.items():
        if value == frequency[0]:
            most_frequent.append(key)

    return most_frequent


print(most_frequent_word("Hello hello hello? Bye Bye!"))

"""
import string

def most_frequent_word(s):
    word_count = {}
    most_frequent = []

    # Remove punctuation, make lowercase, and split into words
    s_no_punctuation = ''.join(char for char in s if char not in string.punctuation)
    final_string = s_no_punctuation.lower().split()

    # Count each word's frequency
    for word in final_string:
        word_count[word] = word_count.get(word, 0) + 1

    # Find the maximum frequency
    max_frequency = max(word_count.values())

    # Collect words with the maximum frequency
    for word, count in word_count.items():
        if count == max_frequency:
            most_frequent.append(word)

    return most_frequent
    """
