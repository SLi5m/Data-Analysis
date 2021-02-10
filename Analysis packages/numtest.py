import numpy as np # Import numpy

data = [[2, 6, 1, 3, 7], [5, 10, 4, 9, 8]]
data = np.array(data)
print (data)
print (data.shape)
print (np.zeros((2, 3))) # produce an array of all 0's
print (np.ones((2, 3))) # produce an array of all 1's

array = np.arange(10) # produce and array from 0 to 9
print(array)
print(array[5:8]) # slice the array by the index, the last index is not included

array[5: 8] = 0 # replace the slice with zero's
print(array)


# Array operations
# Arithmetic operations

data = np.array([[5, 6, 7],
                [8, 9, 10]])
print(data + 5)
print(data * data)

# Transposing and swapping axis
data = np.arange(16).reshape((4,4))
print (data)
# Transposing of an array
print(data.T)

x = np.random.randn(2, 3)
print(x)


# Statistical methods
# Random data
data = np.random.randn(3, 2)
print (data.mean())
print (data.min())
print (data.max())
print (data.sum())

# Matrix Class
X = np.random.randn(3, 2)
X = np.matrix(X)
print(X)
Y = np.random.randn(2, 2)
Y = np.matrix(Y)
print(Y)
# Multiply the matrix
print (X * Y)
