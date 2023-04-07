# Multiple Parameters Functions -> In this we use to apply more value and pairs for use more calculations.
def myFunc(num1=1, num2=2):
    x = num1+num2
    print(x)
myFunc(250,350) #Calling function



# Exampple 2:-
def myFunction(str1='romeo', str2='siwach'):
    x = str1+str2
    print(x)
myFunction('Alexandra', 'Dadario') #Calling function



# Default Parameters -> These are the parameters which uses the default values provided to he functions.
def addNum(num1=10, num2=20):
    x = num1+num2
    print('The sum of two numbers is', x)
addNum()  #Calling function
