'Recursion Limit -> It is the limit set by the Python developers for running a iteration of loop which is by default upto 1000 and we can check it and also set user defined limit.'
import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0


def greet():
    global i
    i = i+1
    print('Hello I am testing recursion limit', i)
    greet()


greet()
