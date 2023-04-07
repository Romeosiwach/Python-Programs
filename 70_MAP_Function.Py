# Map Function in Python :-
# A Map function in Python that applies on all items in an input list
# Syntax : map(Function_to_apply,List_of_inputs)

# Example without using map function -
num=[1,2,3,4,5]
square=[]
for i in num:
    square.append(i**2)
print('The square of num is : ',square)    

# Example using map function -
num=[1,2,3,4,5]
square=list(map(lambda x:x**2,num))
print('Square of num is : ',square)
    
# Example for using map function using list of function :-
def multiply(x):
    return x*x
def add(x):
    return x+x
result = [multiply,add] 
for i in range(5):   
    value=list(map(lambda x: x(i),result))
    print('The final result is : ',value)    