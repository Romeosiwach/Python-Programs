# class Student:
#     def __init__(self,Roll_number,Name,Age):
#         self.Roll_number=Roll_number
#         self.Name=Name
#         self.Age=Age
#     def introduction(self):
#         print("My roll number is : ",self.Roll_number)
#         print("My name is : ",self.Name)
#         print("My age is : ",self.Age)
#     def ask(self):
#         print('Hello! '+self.Name +' how are you ?')
#     def greet(self,greeting):
#         print('Thankyou! '+self.Name+','+greeting)

# Student1=Student(1201,'Romeo Siwach',32)
# Student2=Student(1202,'Vinay Siwach',28)
# Student3=Student(1203,'Saksham Siwach',5)

# # ************************Method**************************** #
# Student1.introduction()
# Student1.ask()
# Student1.greet(' welcome to the world of coding.')

# Student2.introduction()
# Student2.ask()
# Student2.greet(' welcome to the world of coding')

# Student3.introduction()
# Student3.ask()
# Student3.greet(' welcome to the world of coding')


################################## Type 2 ##################################
# print('**********Details of student-1**************')
# StudentFirst=Student1.Roll_number
# NameFirst=Student1.Name
# AgeFirst=Student1.Age

# StudentSecond=Student2.Roll_number
# NameSecond=Student2.Name
# AgeSecond=Student2.Age


# StudentThird=Student3.Roll_number
# NameThird=Student3.Name
# AgeThird=Student3.Age


# print(StudentFirst)
# print(NameFirst)
# print(AgeFirst)

# print(StudentSecond)
# print(NameSecond)
# print(AgeSecond)

# print(StudentThird)
# print(NameThird)
# print(AgeThird)
#############################################################################################################################

# import calendar
# month=int(input('Enter the month you want to print : ', ))
# year=int(input('Enter the year you want to print : '))
# print('\n',calendar.month(year,month))

############################################################################################################
# import calendar
# month=(int(input('Enter month : ')))
# year=(int(input('Enter year : ')))
# print('\n',calendar.month(year,month))

#######################################################
# while True: print(eval(input('Enter the equation for evaluation : ')))

#############################################################
# while True: print(int(eval(input('Value : '))))

# import calendar
# month=int(input('Enter month : '))
# year=int(input('Enter Year : '))
# print("\n",calendar.month(year,month)

# print('Hello world')

# a=int(input('Enter the first number'))
# b=int(input('Enter the second number'))
# c=a+b
# print(c)
# print(a+b)
# a=int(input('Enter the first number : '))
# b=int(input('Enter the second number : '))
# print('Result is : ',a+b)

# import csv
# opened_file = open('AppleStore.csv')
# read_file = opened_file.read()
# new_line_split = read_file.split("\n")
# print(new_line_split[:2])

# rating = [10, 5, 6, 8, 9, 11]
# index = 0

# for elements in rating:
#     print(index,elements)
#     index +=             1

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(i, end='none')