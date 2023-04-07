'Fibonacci Series -> It is a type of series in which add all the previous numbers in a sequence upto th last number.'
'i.e : "1, 2, 1+2=3, 3+2+1=6, 6+3+2+1=12, 12+6+3+2+1=24 ............n" '


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(int(input('Enter any number of your choice : '))))

