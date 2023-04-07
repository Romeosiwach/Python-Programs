# Classification of data types ->
# Numeric data types -> These include the three types of numeric data such as Intiger, Float, Complex numbers

x=2
print(type(x))
y=2.56
print(type(y))
z=2+3j
print(type(z))

# Dictionary data types ->
# These data types are in the form of keys and values. i..e x={key:value, key: value}

numbers={0:0,1:1,2:4,3:9,4:16}
print(type(numbers))

# Boolan data types ->
# These are the data types which renders the output as whether it is true or false.

a=3<2
print(a)
b=3>2
print(b)

# Set data types ->
# The set data types contains the pairs of numbers but prints the single numbers amongst the pairs

sets={1,1,2,2,3,3,4,4,5,5,6,6}
print(sets)
print(type(sets))

# Sequence data types -> These are of three types Strings, Lists, Tuple.
# Strings -> It is an ordered list of characters

myString='Python'
print(type(myString))

# Lists -> It is an ordered sequence of objects. i.e [1,2,3]
myList=[1,1,2,2,3,3,4,4]
print(myList)
print(type(myList))

# Tuple -> It is an immutable sequence of objects. i.e (1,2,3), and these tupples are immutable
myTuple=(1,1,2,2,3,3,4,4)
print(myTuple)
print(type(myTuple))

myTuple=(1,) # For tuples use coma ,
print(type(myTuple))
myTuple=(1)  # For intigers do not use comma
print(type(myTuple))

