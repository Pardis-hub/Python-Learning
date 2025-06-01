"""
Swap Variables Without Using a Temporary Variable
Write a Python program that swaps two variables without using a temporary variable
"""

a = 5
b = 3
print('a =', a)
print('b =', b)
numbers = (a, b)
a, b = b, a
print('a =', a)
print('b =', b)