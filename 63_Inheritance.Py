'Python Inheritance :-'
'It is a feature that allows us to create a child class that allows us to inherit the properties and methods of another/parent class'

# Example :-
# Parent Class #
class Animal:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
# Method #        
    def walk(self):
        print(self.Name+' walk fastly')  
        
# Child Class #   
class Puppy(Animal):        
    def __init__(self,Name,Age):
        super().__init__(Name,Age)
# Method #        
    def sound(self):
        print(self.Name+' walk slowly') 
        print('The age of puppy is ' +str(self.Age)+' Years ')
 
# Calling Functions #       
obj_Puppy=Puppy('Tomy',2)
obj_Puppy.walk()
obj_Puppy.sound()