# Lambda functions -> Lambda funcctions are also cvalled Anonymous functions.
# These functions does not have names.
# The body of lambda functions have only one expressions but can have multiple arguments.
# The result of expressioin is atomatically returned.

def add(a, b):
    c = a+b
    return c


print("The addition of 2 and 3 is :", add(2, 3))


def sub(a, b):
    c = a-b
    return c


print('The substraction of 20 and 10 is :', sub(20, 10))


def multi(a, b):
    c = a*b
    return c


print('The product of 55 and 65 is :', multi(55, 65))


def div(a, b):
    c = a/b
    return c


print("The division of 20 by 5 :", div(22, 5))


def pow(a, b):
    c = a**b
    return c


print('The power of 3 to 6 is :', pow(3, 6))


# Understanding the Lambda function keyword :-

add=lambda a,b:a+b
print("The sum of 5,6 is :",add(5,6))

sub=lambda a,b:a-b
print('The sub of two a,b is :',sub(5,6))

multi=lambda a,b:a*b
print("The product of a,b :", multi(5,6))

div=lambda a,b:a/b
print('Division of a,b is :', div(5,6))
pow=lambda a,b:a**b
print('Power of a to b is :', pow(5,6))