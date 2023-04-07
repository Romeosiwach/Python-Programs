'There are three types of inheritance :-'
'Single Inheritance :-'
'Single inheritance enables a child class to inherit properties from a single parent class'
'Thus enabling code re-usablity and addition of new features to existing code. A---->B'
# Example:-
class Animal:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
    def walk(self):
        print(self.Name+' walk fastly')    
class Puppy(Animal):
    def __init__(self,Name,Age):
        super().__init__(Name,Age)
        
    def sound(self):
        print(self.Name+' walk slowly')        
        print('The age of puppy is '+str(self.Age)+' Years')

obj_Puppy=Puppy('Tomy',2)
obj_Puppy.walk()
obj_Puppy.sound()

                    

'Multiple Inheritance :-'
'When a class can be derived from more than one parents(father,mother) class then this ic called multiple inheritance'
'In this all the features of parent class are inherited into child class. A--->C, B--->C '
#Example :-
# Parent1
class Father:
    fathername=' '
    def father(self):
        print(self.fathername)
# Parent2 
class Mother:
    mothername=''        
    def mother(self):
        print(self.mothername)

# Derived/Child Class        
class Son(Father,Mother):
    def parentsofson(self):
        print('My father name is :'+self.fathername)
        print('My mother name is :'+self.mothername)

# Calling functions        
obj_Son=Son()     
obj_Son.fathername='Rama'
obj_Son.mothername='Sita'
obj_Son.parentsofson()

        
'Multi Level Inheritance :-'
'In this inheritace the child class is derived from a class(parent) which is already derived from another class(grand-parents)'
'In this class we inherit a classes from multiple separate levels'
'A-->B-->C'

# Example :-
class Animals:
    def speak(self):
        print('Animals is speaking') 
class Dog(Animals):
    def bark(self):
        print('Dog is barking') 
class Pupy(Dog):
    def eat(self):
        print('Puppy is eating bread')

object1=Pupy()
object1.speak()       
object1.bark()
object1.eat()
