from math import pi, factorial
'(4)---> FOR, IN, IS, NOT Keywords :- '
'The "For" keyword is basically the for looping or iterating in the Python language'
'The "IN" keyword is used to check the participation of any element in some conatiner objects'
'The "IS" keyword is used to test the identity of any object.'
'The "IS NOT" is used to invert any conditional statements'

# Example 1:- using for and in keywords
myFamily = ['Surender', 'Kamlesh', 'Romeo', 'Deepika', 'Vinay', 'Skasham']
print(myFamily)

for allMembers in myFamily:
    print('All members in my family are : ', allMembers)

# Example 2:- Using is and is not keywords
firstNum = 15
secondNum = 10

print(firstNum is secondNum)  # false
print(secondNum is firstNum)  # false

print(firstNum is not secondNum)  # true
print(secondNum is not firstNum)  # true

'(5)--> FROM and IMPORT Kewords :- '
'The "IMPORT" keyword is used to import some modules into current workspace or namespace'
'The "FROM" keywor is used to import some sp[ecial attribute from a module'

# Example :-
print(pi)  # 3.141592653589793
print(factorial(10))  # 3628800

'(6)--> Global Keyword :-'
'By using global keyword we can force a local scope variable to be a global scope variable'
'Variable Scope -In python the variable has two types of scopes '
'---> Local scope variable - A varible that is defined inside a function is called local scope variable.'
'---> Global scope variable - A variable that is defined out side the function has a global scope.'

# Example :- For local scope


def fruitName():
    fruit = 'Grapes'  # variable declared inside the function
    print(fruit)


fruitName()
'print(fruit)'  # This is not printing because this is declared outside the function

# Example :- For global scope
fruit = 'Mangoes'
print(fruit)  # Printing outside the function


def fruitNames():
    print(fruit)  # Printing inside the function


fruitNames()
print(fruit)  # Printing outside the function

# Example: Using Global keyword
frt = 'Oranges'
print(frt)


def frtName():
    global frt  # Here by using "Global keyword we have made the global keyword to local keyword"
    frt = 'Cherries'
    print(frt)


frtName()

print(frt)  # Here we are using the global keyword as per local keyword variable

'(7)--> NON-LOCAL KEYWORD :- The non local keyword is used for declaring non local scope variables which are used in nested functions means a function with in a function and whose local scope is not defined'
'This means the variable can neither be local not global scope'
'To choose the outer function from outer to innner function we use non local keyword'

# Example:-
myVariable = 'Global Variable'

def outerFunc():
    myVariable = 'Local Variable'
    print('The value of x for outer function ', myVariable)

    def innerFunction():
        nonlocal myVariable
        myVariable = 'Nonlocal Variable'
        print('The value of x for Inner function function', myVariable)
    innerFunction()

outerFunc()
print('The value of x for which is outside the inner and outer functions ',myVariable)
