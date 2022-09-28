import numpy as np

# Create a list
a = [[11,12,13],[21,22,23],[31,32,33]]

## Convert list to Numpy Array
# Every element is the same type
A = np.array(a)

# A=[11 12 13]
#   [21 22 23]
#   [31 32 33]

# A[2][1] = 32

# Access the element on the first and second rows and third column
A[0:2, 2]

# Access the element on the first row and first and second columns
A[0][0:2]

A.ndim # = 2 | Show the numpy array dimensions
A.shape # (3,3) | 3x3 return tuple 
A.size # 9

B = A[0:2,2] 
# print(B) # [13 23]

# Adding 2 Arrays
x = np.array([[1,0],[0,1]])
y = np.array([[2,1],[1,2]])
z = x+y
# [3 1]
# [1 3]

# Multiply in a constant
d = 2*z
# [6 2]
# [2 6]

# Dot product 2 arrays
X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)

print(z)
