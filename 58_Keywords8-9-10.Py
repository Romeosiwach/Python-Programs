'[8]--> NONE Keyword :- The none keyword in python is no value associated, non is also an object in Python'
'i.e x=10 and x=None'
'x=10 in this the x is refering to a data type int and x=None is refering to a data type called "None-type"'

# Example:-
variable1 = None
variable2 = 10

if variable1 == None:
    print('The first variable "variable1" is a None')
else:
    print('The first variable "variable1" is not a None')

if variable2 == None:
    print('The second variable "variable2" is a None')
else:
    print('The second variable "variable2" is non a None')

print(type(variable1))
print(type(variable2))

'[9]-->ASSERT Keyword :-'
'The assert keyword is used when we are debugging code, teh assert keyword is useful to ensure that the given condition is true, If it is not true then it raises an error'
'Syntax of assertion ---> [ assertion condition, error_message ]'

# Example 1:-
number = 20

assert number <= 21, 'The number should be greater or equal to 20'
# Example 2:-
myName = 'Romeo Siwach'

assert (myName ==
        'Romeo Siwach'), f'Provided name is {myName}, it should be Romeo Siwach'
print(f'Yes,My name is {myName}')

'[10]--> YIELD Keyword:-'
'The yiled keyword to make a output and continue the program unlike return where the output is printed and program stops'
'The yield keyword gives back a generator object'
'It is used inside a function'
'It destroyes the state of a local variable and also it exits the function'

# Example:- Programn for making a list of numbers


def makeList(num):
    for lists in range(num):
        print('Local variable number is ', lists)
        yield lists


print(makeList(10))
print(list(makeList(10)))

valueList = makeList(11)

firstValue=next(valueList)
print('The first value is : ',firstValue)

secondValue=next(valueList)
print('The second value is : ',secondValue)

thirdValue=next(valueList)
print('The third value is : ',thirdValue)

fourthValue=next(valueList)
print('The fourth value is : ',fourthValue)

fifthValue=next(valueList)
print('The fifth value is : ',fifthValue)

sixthValue=next(valueList)
print('The sixth value is : ',sixthValue)

seventhValue=next(valueList)
print('The seventh value is : ',seventhValue)

eighthValue=next(valueList)
print('The eighth value is : ',eighthValue)

ninthValue=next(valueList)
print('The ninth value is : ',ninthValue)

tenthValue=next(valueList)
print('The tenth value is : ',tenthValue)

eleventhValue=next(valueList)
print('The eleventh value is : ',eleventhValue)