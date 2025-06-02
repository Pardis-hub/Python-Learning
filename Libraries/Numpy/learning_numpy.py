import numpy as np

a = np.arange(1, 11, 1)
#print(a)

b = np.random.rand(3,3)
#print(b)

c = np.linspace(0, 5, 10)
#print(c)

d = reshaped = np.arange(12).reshape(3,4)
#print(d)

e = np.eye(5)
#print(e)

odd = a[a%2 == 1]
#print(odd)

f = np.array([1, 12, 4, 60, 8, 11])
f[f>10] = -1
#print(f)

g = np.array([[1, 2], [3,4]])
transposed_g = g.T
#print(transposed_g)

h = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
i = np.array([5, 6, 7, 8])
#print(h + i)
#print(i * 2)

# Example 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Compute column means
col_means = np.mean(arr, axis=0)

# Subtract column means from each column
result = arr - col_means

#print("Original Array:")
#print(arr)
#print("\nColumn Means:")
#print(col_means)
#print("\nArray After Subtracting Column Means:")
#print(result)

# Example array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Sum of the array
total_sum = np.sum(arr)

# Mean of the array
mean = np.mean(arr)

# Standard deviation of the array
std_dev = np.std(arr)

#print("Array:", arr)
#print("Sum:", total_sum)
#print("Mean:", mean)
#print("Standard Deviation:", std_dev)

# Example matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Dot product using np.dot
dot_product = np.dot(A, B)

# Dot product using @ operator
dot_product_alt = A @ B

#print("Matrix A:")
#print(A)
#print("\nMatrix B:")
#print(B)
#print("\nDot Product (using np.dot):")
#print(dot_product)
#print("\nDot Product (using @ operator):")
#print(dot_product_alt)

A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]])

B = np.array([1, -2, 0])

x = np.linalg.solve(A, B)
#print("Solution:", x)