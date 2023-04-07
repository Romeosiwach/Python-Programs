# Python tuple -> Python tuple is a type of list but unlike a list items can not be modified in the tupple.

myTuple=(2,2.25,True,'Romeo',(2+3j))
print(myTuple)  
print(type(myTuple))
print(len(myTuple))

# Tuple indexing ->
print(myTuple[2])
print(myTuple[-2])
print(myTuple[2:5])
print(myTuple[-2:-4])

# In and not in ->
print('Romeo'in myTuple)
print('Siwach'in myTuple)
print('Saksham'not in myTuple)


# Touple looping ->
for items in myTuple:
    print("Items in mytuple are",items)
    
print(myTuple.count(5))    
    