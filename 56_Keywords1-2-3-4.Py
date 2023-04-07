import keyword
'Python Keywords -> Kewords are the pre defined words in any programming languge which have predefined meaning and functionality. It can not be used as a variable.'
'The Python keywords are :- true,false,calss,def,return,if,elif,else,try,except,raise,finally,for,in,is,not,from,import,global,non-local,lambda,pass,while,break,continue,and,with,as,yield,del.or,assert,none.'

# Example 1:-
print(len(keyword.kwlist))
print(keyword.kwlist)

###########################################################################################################################################

'1---> TRUE and FALSE Keywords:- These are used by boolean datatypes, comparison operators returns True or False'
# Example 2:-
print(10 >= 11)  # False
print(2 > 6)  # False
print(10 > 9)  # True
print(5 >= 5)  # True

###########################################################################################################################################

'2---> CLASS, DEF, RETURN Keywords:- '
# Example 3:-


class areaSqur:
    def calArea(self, side):
        return (side*side)

    def displaySelf(self):
        return (self)

    @classmethod
    def classMethod(cls):
        return (cls)

    @staticmethod
    def staticMethod():
        return ()


object_class = areaSqur()
print('0> *************************The area of square is***************************')
print(object_class.calArea(8))
print('\n')

print('1> The self parameter is a reference to current instance of the class where we are calling instance method here')
print(object_class.displaySelf())
print('\n')

print('2> The first parameter in the class method is cls parameter where we are calling class method here')
print(object_class.classMethod())
print('\n')

print('3> If you dont specify any parameter in the method then static mathod is called here')
print(object_class.staticMethod())
print('\n')


# Example 4:-
class myClass:
    def method(self):
        return self

    @classmethod
    def classMethod(cls):
        return cls

    @staticmethod
    def static():
        return

obj = myClass()
print(myClass.method(obj))
print(obj.method())
print(obj.classMethod())
print(obj.static())

############################################################################################################################################

'3---> IF, ELIF, ELSE Keywords --> These keyeords are used for conditional branching or decision making'
'First the "If" condition is checked iit is found false then it checks the "Elif" statement and if it is also found false then finally else condition is printed'
# Example 5:-

# x = print(int(input('Enter the number')))
x = 20
if x > 10:
    print('The value of x is greater then 10 so if condition is true and printed : ', x)
elif x < 10:
    print('The value of x is less then 10 so the elif condition is true and printed : ', x)
else:
    print('The value of x is equal to 10 so else is true and printed ; ', x)

###########################################################################################################################################

'4---> TRY,EXCEPT,RAISE,FINALLY Keywords --> These keywords are use to handle diff exceptions in python. '
'In "Try" block we can write some code which may raise dome exceptions'
'Using the "Except" block we can handel them'
'The "Finally" block is exexuted even if there is unhandles exception'
'In python the " _init_() " function is called as constructor and is always called when an object is created'
'The task of "Constructor" is to assign values to the data members of the class when an object of the class is created'


class BalException(Exception):
    def _init_(self, msg):
        self.msg = msg


customerId = 124001
custimerName = 'Romeo Siwach'
Currentbal = 100000

amount = int(input('Enter the amount you want to withdraw : '))
if amount > Currentbal:
    print('Insufficient balance in your account')
else:
    try:
        if Currentbal < 5000:
            balance = Currentbal-amount
            raise BalException('Minimum balance maintained should be 5000')
    except BalException as be:
        print(be)

    finally:
        balance = Currentbal-amount
        print('The remaining balance is : ',balance)