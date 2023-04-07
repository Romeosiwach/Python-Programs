# Program for printing Calender for any given month and year :-

import calendar
month = int(input('Enter the month you want to print : '))
year = int(input('Enter the year you want to print : '))

print('\n', calendar.month(year, month))

# Calculator in a singe line of code

while True: print(eval(input('Enter the equation you want to solve i.e 2+3 : ')))


# Calculator in which user is asked to input numbers for calculation and which type of calculation is required

firstNum = int(input('Enter first number : '))
secondNum = int(input('Enter second number : '))
calculation = input(
    'Enter the calculation type of your choice, \nadd, \nsubs,\nmulti, \ndiv,\nmode : ')

if calculation == 'add':
    print('The sum of the numbers is : ', firstNum + secondNum)
elif calculation == 'sub':
    print('The substraction of the numbers is : ', firstNum-secondNum)
elif calculation == 'multi':
    print('The multiplication of the numbers is : ', firstNum*secondNum)
elif calculation == 'div':
    print('The division of the numbers is : ', firstNum/secondNum)
elif calculation == 'mode':
    print('The mode of the numbers is : ', firstNum%secondNum)
else:
    print('Error! enter valid calculation keyword')

# Program to display countdown timer :-
import time

def countdown(time_sec):
    while time_sec:
        mins, secs=divmod(time_sec,60) 
        timeformat='{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_sec-=1
    print('countdown timer ends!!!') 
# countdown(15)       
countdown(int(input('Enter the time in seconds : '))) 

# Program for Making Fake Profile :-
from faker import Faker
fake = Faker()
for i in fake.profile():
    print(i.upper(),':', fake.profile()[i])

# Program for implementing the game for two players with a delay of 2 seconds
from time import sleep
from threading import *
def display1():
    for i in range(5):
        print('Hi I am the Player - 1 playing the Game')
        sleep(2)
def display2():
    for i in range(5):
        print('Hi I am the Player - 2 playing the Game') 
        sleep(2)
thread1=Thread(target=display1) 
thread2=Thread(target=display2)       
thread1.start()
sleep(1)
thread2.start()
thread1.join()
thread2.join()
print('Bye,The Game is Ended for both the Players!!!')
