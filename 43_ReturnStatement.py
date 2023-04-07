# Return Statement -> The return statement is used to return the value to the function caller.In this the print function after adding return will not be executed. The return statement stops the execution of the function.

def average(num1, num2, num3, num4, num5):

    return (num1+num2+num3+num4+num5)/5


print('This statement is not going to execute because we use return statement in the function')
print('Print thr average of the numbers')

avg1 = average(2, 3, 4, 5, 6)
print(avg1)

avg2 = average(11, 1, 23, 45, 66)
print(avg2)
