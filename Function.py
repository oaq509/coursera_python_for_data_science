# There are many built in python functions | sorted,len
ratings = [3,5,5.2,2,4,6.6,6,9,7.5,10]
ratings_sorted = sorted(ratings) # sorted return new list
print(ratings_sorted)

# sort change the list itself
ratings.sort()
print(ratings)

# Making Functions
def add(x,y):
    return x+y

print(add(1,2))

#########
help(add)


def NoWork():
    pass # do nothing like empty function



# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)


