# Python has many different kinds of data types: integers, 
# floats, strings, lists, dictionaries, booleans. 
# In Python, each is an object.

# Example for a list method | reverse()
Ratings = [7, 2, 5, 6, 6, 8, 9, 9, 10, 10]
# Ratings.reverse()
Ratings.sort()
print(Ratings)

class Circle(object):
# The function init is a constructor. It's a special function that tells Python you are making a new class. 
  def __init__(self, radius, color): 
    self.radius = radius
    self.color = color
    
  def add_radius(self,r):
    self.radius = self.radius + r
    
redCircle = Circle(10,'red')

dir(redCircle) # The return value is a list of the objects data attributes.

print(redCircle.color)

# There is method to check the type
type(1+2.5) # <class 'float'>
type([1,2,3]) # <class 'list'>