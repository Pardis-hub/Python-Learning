"""
Factorial Using Recursion
Write a recursive function to calculate the factorial of a number.
"""

def factorial(n):
    # Your code here
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

"""
OR

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
"""