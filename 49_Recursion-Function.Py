'Recursion Function -> Recursion function is a type of function which calls itself to solve the smaller version of its task until a final call is made which doesnot require a call to itself.'
'Every Recursion function has two major cases:'
'--->Base Case :-In which the problrm is simple enough to be solved directly without making any further calls to the same function'
'--->Recursive Case :- In which first the problem is divided into smaller sub parts'

# Example 1:-
def fact(n):
    if (n == 0):
        return 1
    else:
        return n*fact(n-1)
n = int(input('Enter any number :'))
result = fact(n)
print('The factorial of number you entered is :', result)

# Example 2:-
def num(n):
    if (n==0):
        return 0
    else:
        return (n%10+num(n//10))
n= int(input('Enter any number :'))        
result=num(n)
print('The sum of numbers you entered :',result)


