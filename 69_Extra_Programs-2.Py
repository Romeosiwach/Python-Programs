# # Program for printing multiplication tables from 1 to 10 :-
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()        
    
# # Program for multiplying two numbers without applying multiplication operations :-
# def multiply(x,y):
#     if (y==0):
#         return 0
#     if (y>0):
#         return(x+multiply(x,y-1))
#     if (y<0):
#         return(-multiply(x,-y))    
# num1=int(input('Enter the first number : '))    
# num2=int(input('Enter the second number : '))
# print(num1,'X',num2,'=',multiply(num1,num2))

# # Program for Making QR-Code :-
# import pyqrcode
# from pyqrcode import QRCode
# string='romeosiwach@gmail.com' 
# url=pyqrcode.create(string)
# url.svg('qr.svg', scale=8)

# # Program for making IronMan Image:-
# from sketchpy import library as lib
# obj=lib.rdj()
# obj.draw()

# # Program for printing the image of South Indian actor Vijay :-
# from sketchpy import library as lib
# obj=lib.vijay()
# obj.draw()

# Program for Printing String in three different ways :-
mystring='Python Programming'
print(mystring)
print('I am learning {}'.format(mystring))
print('I am learning '+mystring)
print(f'I am learning {mystring}')