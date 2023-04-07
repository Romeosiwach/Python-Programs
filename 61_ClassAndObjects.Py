"Class and Objects in Python -->"
'In Python every thing is an object and a class is used to create object'

"# Creating a Class:- "
'Use the class keyword to create a class'
# Syntax - 
# class Classname:
#    statement(s)

"# Discovering an object :- "
'We can create an object by class by instatiating or discovering it.'
'To discover a class add round brackets() to its class name'
# Syntax: object = Classname()
'After instating a object we can now access the object properties'

"# Class Attributes :-"
'A class can have attributes for example a student class can have attributes like Student_name,Roll_number,age,batch'
"Now that our class is ready we can now instantiate it by providing the values to its attributes"
'This process is called creating the instance of the class'
'Instance is simply the object creted from the class, In below program the student1 is unique instance of the Student class'
'We can now access the class property of the object,self parameter allows us to access the attributes and methods of the class'
'The __init__() function provides the values for the attributes of the class'

"# Method :-"
'Method are the functions that can access the class attributes, these methods should be created inside the class'
'We must use the self parameters to access class attributes, we can pass the arguments to a method'

# Example:-
class Person1:
    first_name='Romeo'
    last_name='Siwach'
    age='30'
object=Person1() 

print(object.first_name)
print(object.last_name)
print(object.age)

class Person2:
    first_name='Saksham'
    last_name='Siwach'
    age='5'   
object=Person2()

print(object.first_name)
print(object.last_name)
print(object.age)