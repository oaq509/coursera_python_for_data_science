# Tuples can store diffrent data types
# tuple is immutable, we can't change them

from cgitb import reset


Ratings = (10,9,8,7,6,5,4,3,2,1)
Ratings.index(1) # find index contain value (1) | last index = 9
print(sorted(Ratings))

Ratings2 = Ratings[0:3] # Slicing 
print('Ratings2 = ', Ratings2) # (10, 9, 8)

# Same as Tuples, But they are mutable (can change)
# lists are part of the core Python programming language; 
# arrays are a part of the numerical computing package NumPy.
L = ['owais ali', 10.1, 1999]

result = [1,2,3] + [1,1,1] # concatenate | [1, 2, 3, 1, 1, 1]

result.extend('5')
result.append(['6',7]) # add list in last index [1, 2, 3, 1, 1, 1, 5, ['6',7]]
del(result[0]) # delete first element
del(result[-1]) # delete last element

'owais algarni'.split() # ['owais','algarni']
'A,B,C,D'.split(",") # split using delimiter comma ,

print(result)
