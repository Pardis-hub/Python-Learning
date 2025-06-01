"""
Tuple and Dictionary Exercise
Write a Python program that creates a dictionary where keys are tuples of coordinates (x, y),
and the values are the result of some function (like multiplication of x and y).
"""

def create_coord_dict(x_range , y_range):
    # Your code here
    coord_dict = {}

    for x in x_range:
        for y in y_range:
            coordinate = (x , y)
            value = x * y
            coord_dict[(x , y)] = value

    return coord_dict
