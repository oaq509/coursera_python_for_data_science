# Dictionaries are a type of collection in Python.
# List is integer indexes. These are like addresses. |  [0,1,2,3,4,5] indexes | Element 1 , Element 2 ...
# Dictionary has keys and values.                    |  [key1,key2,key3] keys | Value 1 , Value 2 ...
# Each key must be immutable and unique

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}  

print('F' in Dict) # True

print(Dict.keys()) # dict_keys(['A', 'B', 'C', 'D', 'E', 'F'])
print(Dict.values()) # dict_values([1, '2', [3, 3, 3], (4, 4, 4), 5, 6])

print(Dict) # print all keys & values