n = int(input('Enter number of words: '))
dictionary = {}

for i in range(n):
    word, meaning = input('Enter word and meaning of dictionary: ').split()
    dictionary[word] = meaning

sentence = input('Enter the sentence: ')
translation = sentence

for key, value in dictionary.items():
    if word in sentence:
        translation = translation.replace(key, value)

print(translation)