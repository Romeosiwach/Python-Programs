'# Exception --> An unwanted and unexpected event that disturbs normal flow of program is calledexception'

'* Exception Handling --->In any programming language there are two types of errors'
'# Syntax Errors :- The errors which occurs because of invalid syntax'
'# Runtime Errors :- While executing the program if something goes wrong because of end user input or programming logic or memory problems then this error occures'
'i.e - -Zero division error, -Type error, -Value error, -File not found error, -EOF error, -Name error'

'SYNTAX OF EXCEPTION HANDLING :-'
# try:
#     Risky Code
# except XXX:
#     Handling the code or Showing an alternative code

# Example 1:-
try:
    a=10
    b=0
    print('The division of a and b is : ',a/b)
except:
    print("No,brother you can't execute the division because it is a zero division error")   
print("Thanks for exception handling for handling exception in my program")

# Example 2:-
try:
    num=int(input('Enter the numenator : '))
    deno=int(input('Enter the denominator : '))
    print('Division is : ',num/deno)
except(ZeroDivisionError) :
    print('You can not divide by zero')   
except(ValueError):    
    print('You must enter the intiger value for division')
    
# Example 3:-
try:
    num=int(input('Enter the numenator : ')) 
    deno=int(input('Enter the denominator : '))
    print('Division is : ', num/deno)
except(ValueError,ZeroDivisionError):
    print('Please check the entered value again it should be of intiger type and greater than zero') 
    
# Example 4 :-
try:
    num=int(input("Enter the numenator : ")) 
    deno=int(input("Enter the denominator : "))
    print('Division is : ', num/deno)
except(ZeroDivisionError):
    print('Entered value can not be zero')    
except(ValueError):
    print('Input value should be of intiger type')    
finally:
    print('All the errors are handled successfully')    
    print('Thanks to exception handling')

# Example 5 :-
try:
    firstnumber=10
    secondnumber='ten'
    raise ValueError
    print('Division is : ', firstnumber/secondnumber)
except:
    print('Enter the intiger value') 

# Example 6:-
import math
num=int(input('Enter the number for factorial : '))
try:
    result=math.factorial(num)
    print('Factorial is : ', result)
except:
    print('Factorial of negative numbers is not possible') 
finally:
    print('Print the factorial or print the statement that that factorial of negative numbers is not possible')

# Example 7:-
try:
    num=int(input('Enter the number : '))
    if num<=0:
        raise ValueError('This is not a positive number') 
    else:
        print('This is positive number')
except ValueError as error:
    print(error)    