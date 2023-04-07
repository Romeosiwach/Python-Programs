# Zip and Unzip Functions :- 
# Zip Function :-
# A Zip function is used to combining two or more lists easily
# After calling a zip function an iterator is return to check content wraped inside and we need to convert it into a list first

# # Example :-
# firstName=['Romeo','Saksham','Surender','Vinay']
# lastName=['Siwach','Singh','Kumar','Siw']
# age=[32,5,54,28]
# print(list(zip(firstName,lastName,age)))

# # Example 2:-
# firstName=['Romeo','Saksham','Surender','Vinay']
# lastName=['Siwach','Singh','Kumar','Siw']
# age=[32,5,54,28]
# for firstName,lastName,age in zip(firstName,lastName,age):
#     print(f"{firstName} {lastName}  is {age} years old")
    
# Unzip Function :- This function is used to separate a single list into two or more lists
 
# Example 3:-
fullName=[('Romeo', 'Siwach', 32), ('Saksham', 'Singh', 5), ('Surender', 'Kumar', 54), ('Vinay', 'Siw', 28)] 
firstName,lastName,age=list(zip(*fullName))
print(f"{firstName}\n{lastName}\n{age}")