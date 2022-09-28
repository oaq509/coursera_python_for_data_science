# Sets are a type of collection. Like lists and tuples.
# you can input different Python types. Unlike lists and tuples, they are unordered. 
# This means sets do not record element position. Sets only have unique elements.

sets = {"a","a","b","c"}; 
print(sets) # {'c', 'a', 'b'}

# we can convert list to set
album_list = ["Michael Jackson", "Thriller", "Thriller", 1982]
album_list = set(album_list)
print(album_list) # {'Michael Jackson', 'Thriller', 1982}

A = {"Thriller","Back in Black", "AC/DC"}
A.add("NSYNC") # {'Back in Black', 'AC/DC', 'NSYNC', 'Thriller'}
print(A)


A.remove("NSYNC") # delete element from a set
"Who" in A        # False


# find intersection of two sets. | we use and &
album1 = {"AC/DC", "Thriller","Back in Black"}
album2 = {"AC/DC", "Thriller","The Dark Side of the Moon"}
intersection = album1 & album2
print(intersection) # {'AC/DC', 'Thriller'}


album4 = album1.union(album2) # The result is a new set that has all the elements of album set one and album set two
print(album4) # {'AC/DC', 'Thriller', 'Back in Black', 'The Dark Side of the Moon'}

print(album1.issubset(album4)) # True
