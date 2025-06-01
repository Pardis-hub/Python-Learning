"""
calculator
Write a function calculator() that takes two numbers and an operator (+, -, *, /) as arguments and performs
the corresponding operation. Use if-elif-else statements.
"""

def calculator(num1, num2, operator):
    # Your code here
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        assert num2 != 0, 'num2 must not be zero'
        return num1 / num2
    else:
        return 'Operation undefined!'   # raise ValueError('Operation undefined!')

i = calculator(2,0,"/")
print (i)