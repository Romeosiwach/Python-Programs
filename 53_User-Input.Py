'User Input -> The input function takes the input from the user the python script stops until the user provides the value.'
'By default the value entered by the user is always considered as String type'
'To change the type to other types we have to provide some instructions called Type Casting such as'

# Examples:-
num1 = input('Enter the first number : ')
num2 = input('Enter the second number : ')
sum = num1+num2
print(sum)  # Output is 1020 this means the Python script is concidering the input type as a string value


num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))
sum = num1+num2
print(sum) # Output is now 30 it means type is converted into intiger type

'In this way we can convert the types into different types such as : float(), string(), bool(), complex()'
