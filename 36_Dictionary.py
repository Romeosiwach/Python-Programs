# Dictionary -> It is unordered mutable collection of items in which items are stored in form of key and value pairs.

myDictinary = {'first_name': 'Romeo',
               'last_name': 'Siwach', 'age': '30', 'gender': "male"}
print(myDictinary)

# Length of dictionary
print(len(myDictinary))

# Calling the Values with the help of Keys
firstName = myDictinary['first_name']
lastName = myDictinary['last_name']
age = myDictinary['age']
gender = myDictinary['gender']

print('Candidates first name is :',firstName)
print('Candidates last name is :',lastName)
print('Candidates age is :', age)
print('Candidates gender is :',gender)

# Delete Statement ->
del myDictinary['gender']
print(myDictinary)

# If Else Statements ->
if 'place' in myDictinary:
    print('the key name present in the dictionary')
else:
    print('The key name is not pressent in the dictionary')

# Nested Dictionary ->
myFamily={'child1':{'name':'Saksham','dob':'2018'},'child2':{'name':'Sagun','dob':'2024'},'child3':{'name':'abc','year':'2030'}}
print(myFamily)
    
    


