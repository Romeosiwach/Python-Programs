# Python lists -> lists are the collection of data contained within the square braces[] and separated by commas, data may be String, Intiger, Float or Boolean values.
myList=[2,2.65,'python',True,(2+3j)]
print(myList)  #1 Printing the list

print(type(myList)) #2 Checking type of data

print(len(myList)) #3 Checking length of list

print(myList[2])   #4 Checking item on position 2

print(myList[-1])  #5 Checking item on position -1

myList.append('Romeo') #6 Adding items to list
print(myList)

myList.pop() #7 Delete last item from the list
print(myList)

myList.remove(2.65)  #8 Delete specific item from the list
print(myList)

print(myList[1:2]) #9 Print a range of items

print(myList[1:5]) #10 Print a range of items

print(myList[:]) #11 Print a range of items
print(myList)

print(2 in myList) #12 Print what is in my list

print('Siwach'in myList) #13 Print what is not in my list

myList[0]='Romeo' #14 Add an item at any specific place in list
print(myList)

del myList[2] #15 Delete an item from a specific place from a list
print(myList)
