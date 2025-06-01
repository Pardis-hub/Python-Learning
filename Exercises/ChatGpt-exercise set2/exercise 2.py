"""
Write a Function with Default Arguments
Create a function that calculates the area of a rectangle, and use default values for length and width.
"""

def rectangle_area(length=10, width=5):
    # Your code here
    if length <= 0 or width <= 0:
        return "Ivalid input!"
    return length * width

