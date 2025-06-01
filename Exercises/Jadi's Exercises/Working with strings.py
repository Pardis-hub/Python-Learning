
string_input = input('Enter your string: ').lower()
vowel_characters = 'aeiou'
for character in string_input:
    for vowel in vowel_characters:
        if character == vowel:
            string_input = string_input.replace(vowel, '')

output = ''
for character in string_input:
    output += '.' + character
print(output)
