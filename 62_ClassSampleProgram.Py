'Python Class Sample Program :-'


class Student:

#****************************** Initializing Functions ************************ #
    def __init__(self, Roll_number, Name, Age):
        self.Roll_number = Roll_number
        self.Name = Name
        self.Age = Age

    def introduction(self):
        print('My roll number is : ', self.Roll_number)
        print('My name is : ', self.Name)
        print('My age is : ', self.Age)

    def ask_student(self):
        print('Hello' + self.Name + ',how are you?')

    def greet(self, greetings):
        print('Thankyou ' + self.Name + ',' + greetings)

#****************************** Initializing Variables ************************#
Student1 = Student(1201, " Romeo Siwach", 32)
Student2 = Student(1202, " Saksham Siwach", 26)
Student3 = Student(1203, " Vinay Siwach", 28)

# ******************************* Calling Functions/Methods ************************** #
print('**********Details of student-1***********')

Student1.introduction()
Student1.ask_student()
Student1.greet("Welcome to the world of coding")

print('**********Details of student-2***********')

Student2.introduction()
Student2.ask_student()
Student2.greet(" Welcome to the world of coding")

print('**********Details of student-3***********')

Student3.introduction()
Student3.ask_student()
Student3.greet("Welcome to the world of coding")


#############################################################SECOND METHOD#####################################################

#***************************** Initializing Variables ***************************#
Firststudent = Student1.Roll_number
Namefirst = Student1.Name
Agefirst = Student1.Age

Secondstudent = Student2.Roll_number
Namesecond = Student2.Name
Agesecond = Student2.Age

Thirdstudent = Student3.Roll_number
Namethird = Student3.Name
Agethird = Student3.Age


# ***************************Printing Variables ********************************#
print('**************Details of first student*********A***')
print('Roll number of first student is : ', Firststudent)
print('Name of first student is : ', Namefirst)
print('Roll number of first student is : ', Agefirst)

print('**************Details of second student************')
print('Roll number of second student is : ', Secondstudent)
print('Name of second student is : ', Namesecond)
print('Roll number of second student is : ', Agesecond)

print('**************Details of third student************')
print('Roll number of third student is : ', Thirdstudent)
print('Name of third student is : ', Namethird)
print('Roll number of third student is : ', Agethird)
