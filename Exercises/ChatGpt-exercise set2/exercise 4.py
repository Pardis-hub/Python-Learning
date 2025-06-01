"""
Matrix Transposition
Write a function that takes a matrix (a list of lists) and returns its transpose.
"""

def transpose_matrix(matrix):
    # Your code here
    for item in matrix:
        for index,element in enumerate(item):
            trans_matrix[index].append(element)
    return trans_matrix

"""
def transpose_matrix(matrix):
    # Initialize an empty transposed matrix with dimensions swapped
    trans_matrix = [[] for _ in range(len(matrix[0]))]  # Number of rows becomes number of columns
    
    # Iterate over the original matrix and append elements to the transposed matrix
    for item in matrix:
        for index, element in enumerate(item):
            trans_matrix[index].append(element)
    
    return trans_matrix
    """

