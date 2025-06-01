name = input('Enter your name: ')
lowercase_chars = 0
uppercase_chars = 0
for char in name:
    if char.islower():
        lowercase_chars += 1
    elif char.isupper():
        uppercase_chars += 1

if lowercase_chars < uppercase_chars:
    print(name.upper())
else:
    print(name.lower())
