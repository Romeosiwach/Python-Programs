# Python Sets -> Python sets are very likely to Lists and Tuples but difference is that they are enclosed in {curly braces} and are of unordered type so it do not follow the indexing.
mySet={2,2.25,'Romeo',True,(2+3j)}
print(mySet)

mySet.add('Siwach') # Adding an item
print(mySet)

mySet.remove(2.25) # Remove an item
print(mySet)

mySet.discard(3) # Discard an item and this is effective than the remove function because it doesen't shows error while item is not present in the set. 
print(mySet)

mySet.update(['Saksham']) # Update an Item
print(mySet)

mySet.pop() # Pop the last item but it is difficult to predict which item will be poped.
print(mySet)

print('Romeo' in mySet) # In or not in my set
print('Romeo'not in mySet)

