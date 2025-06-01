def input_string():
    string_inp = input('Enter the string: ').upper()
    return string_inp

def check_substring(s):
    print(s)
    for index, char in enumerate(s, start=0):
        if len(s) < 2:
            if char == 'A' or char == 'B':
                return 'NO'
            else:
                return 'YES'
        if char == 'A':
            if s[index+1] == 'B':
                if len(s) > 2:
                    return check_substring(s[index+2:])
                else:
                    return 'YES'
            else:
                return 'NO'

        elif char == 'B':
            if s[index + 1] == 'A':
                if len(s) > 2:
                    return check_substring(s[index + 2:])
                else:
                    return 'YES'
            else:
                return 'NO'
    return 'YES'

s = input_string()
print(check_substring(s))

