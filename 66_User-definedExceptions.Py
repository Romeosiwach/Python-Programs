'User-defined Exceptions --->'
'Sometimes we have to define or raise our own exceptions explicitly to indicate that something went wrong '

'TRY BLOCK :- In try block we can make some program which may raise some exceptions'
'RAISE KEYWORD :- The raise keyword is going to raise some exception which is already handled'
'EXCEPT BLOCK :- This block is used o handle exceptions'
'FINALLY BLOCK :- The finally block is used when ther is even a exception which is pending to be handled'

# # Example 1 :- Whithout using try and except block for handling exceptions.
# class Age(Exception):
#     def __init__(self,msg):
#         self.msg=msg

#     age=int(input('Eneter your age : '))
#     if age>60:
#         print('Your age is greater than eligiblity criteria for voting')
#     elif age<18:
#         print('Sorry your age is less than eligible criteria for voting')
#     else:
#         print('Congrats! you are eligible for voting')

# Example 2:- Using try and except block for handling exceptions.


class Age(Exception):
    def __init__(self, msg):
        self.msg = msg


age = int(input('Enter your age : '))

try:
    if age >= 60:
        raise Age('You are to old for voting')

    elif age < 18:
        raise Age('You are to young to vote')

    else:
        print('Congrats! you are eligible for voting')

except Age as error:
    print(error)

'UNCHECKED EXCEPTIONS :-'
'The exceptions which are not checked on the compile time, these can be handled on run time only'
'CHECKED EXCEPTIONS :- '
'The exceptions which are checked at compile time, if some code within the method throws a checked exception'