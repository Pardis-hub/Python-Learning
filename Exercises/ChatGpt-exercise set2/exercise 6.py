"""
Custom Exception Handling
Write a function that divides two numbers and raises a custom exception when division by zero occurs.
Catch the exception and display a meaningful error message.
"""

class DivisionByZeroError(Exception):
    def __init__(self, message="Cannot divide by zero"):
        super().__init__(message)

def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise DivisionByZeroError()  # Raise the custom exception if denominator is zero
    return numerator / denominator  # Perform division if safe

try:
    result = divide_numbers(10, 0)  # Example where denominator is zero
    print("Result:", result)
except DivisionByZeroError as e:
    print("Error:", e)  # Handle the error and print the custom message

"""
The line raise DivisionByZeroError() is responsible for intentionally triggering the DivisionByZeroError exception 
you defined earlier. Here’s what it does in detail:

1.raise Keyword: This keyword in Python is used to signal that an exception (error) should be triggered. 
When raise is used, the program stops its normal flow at that line and looks for an exception handler 
(try-except block) to manage the error.

2.DivisionByZeroError(): This is an instance of the custom exception class DivisionByZeroError. 
When called without any arguments, it uses the default message we set: "Cannot divide by zero".

So, in this context, raise DivisionByZeroError() does the following:

1.Stops the function’s execution at that line because it encounters an error.
2.Causes Python to search for any except DivisionByZeroError block to handle this specific exception.
3.If it’s handled, the program continues running (in the except block); otherwise, 
it stops and shows the error traceback.
"""
