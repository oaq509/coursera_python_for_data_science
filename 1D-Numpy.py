# NumPy is a Python library used for working with arrays, 
# linear algebra, fourier transform, and matrices.
# A numpy array is similar to a list. 
# NumPy stands for Numerical Python and it is an open source project.
# The array object in NumPy is called ndarray, 
# it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np

# Create a python list
a = ["0", 1, "two", "3", 4]

# Create a numpay array
a = np.array([0,1,2,3,4])
type(a) # numpay.ndarray
a.dtype # int64
a.size # 5
a.ndim # 1 | Number of array dimensions (Rank of the array)
a.shape # Get the shape/size of numpy array

b = np.array([3.1,11.02,6.2,213.2,5.2])
type(b)
b.dtype # float64

print(b[0]) # first element

print(b[1:4]) # Slicing | Select from index 1 - 3



# Vector Addition and Subtraction
u = np.array([1,0])
v = np.array([0,1])

z = u+v # [1,1]


# Array multiplication with a Scalar
y = np.array([1,2])
s = 2 * y # [2,4]


# Product of two numpay arrays
k = np.array([1,2])
j = np.array([3,2])
z = k * j # [3,4]


# Dot Product
q = np.array([1,2])
w = np.array([3,1])
result = np.dot(q,w) # = 5 | (1*3)+(2*1)

# Adding Constant to an numpy Array
p = np.array[1,2,3,-1]
g = p + 1 # [2,3,4,0]

# Universal Functions
xx = np.array([1,-1,1,-1])
mean = xx.mean() # = 0 | adding all number and dividing them on thier count which is 4.

# Get the standard deviation of numpy array
standard_deviation = xx.std()

# Max value
zz = np.array([1,-2,3,4,5])
zz.max() # 5

# Linspace
np.linspace(-2,2,num=5) # (starting point, ending point,num = number of samples to generate)
# [-2,-1,0,1,2]

np.linspace(-2,2,num=9)
#[-2,-1.5,-1,-0.5,0,0.5,1,1.5,2]
#[ 1, 2,   3, 4,  5, 6, 7, 8, 9]

# The value of pi
np.pi

# Calculate the sin of each elements

yy = np.sin(zz)
print(yy)


# Iterating 1-D Arrays
arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
  print(x)


