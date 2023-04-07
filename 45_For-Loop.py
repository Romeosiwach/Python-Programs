# Python loops ->
# There are two types of loops in Python --->For Loop and --->While Loop
# For Loops :- For loops are used to loop through or iterate over a sequence or iterable objects. A "For" Loop is used to repeat a specific block of code a known number of times. Iterable objects are strings, lists,sets etc

# For loop through a list :- The for loop is commonly used with a list.

myList = [2, 2.25, True, False, 'Romeo', 'Siwach']

for items in myList:
    print('Items of list are', items)


# For loop through Strings :- A string is also an iterable object because it is a sequence of characters.

myString = ['Surender', 'Romeo', 'Vinay', 'Saksham', 'Deepika']

for family in myString:
    print('One of the member of Siwach family is ', family)

# For loop through range() function :- When you are programming something you need to repetetively use the block of code but you dont have something to loop over. This is where the range function comes into picture.
# The range function creates the sequence opf numbers starting with 0 and ending with n-1
# For example in range(5) the sequence of five numbers is created from 0 to 4.
# from collections import Counter
myString = ('Python Programming')

for items in myString:
    print('The sequence of characters in my string are ', (items))

for numbers in range(20):
    print('Numbers in range 0 to 20 are ', numbers)

# Nested For Loops :-
# For placing a 'for' loop in another 'for' loop.
# Example 1: Tables of Mathematics 
for i in range(1, 11):
    for j in range(1, 11):
      print(i * j, end='') # Here end=" ", is used to print # in same line and not in new line.
    print()  
    
# Example 2: Printing Patterns
rows=10
for i in range(1,rows+1):
    for j in range(1,i+1):
        print('*',end='')
    print('')    
# Example 3:
for numbers in range(4):
    print('I am in for loop because loop has not ended')    
else:
    print('I am not in loop because loop has ended')