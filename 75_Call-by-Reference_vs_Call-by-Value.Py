# Call by Reference vs Call by Value :-
# Call by Reference :-
# When we calls a function then instead of copying values of variables in call by reference we use to call the address of the varible.
# If there is any change in the variable in that function then the original variable also changes
# Python acts as call by reference if passed data is mutable data types like list, sets and dictionaries,

# Example 1:-

def marks(mylist):
    mylist.append([12,13,14,15,16])
    print('List of values inside the function : ',mylist)
    print("Address of the list variables inside the function is : ",id(mylist))
    return

mylist=[19,20]
marks(mylist)
print('list of values outside the function : ',mylist)
print('Address of the variables outside the function : ',id(mylist))

# Call by Value :-
# In call by value when a function is called then the copy of the variable is passed to the function 
# If there is any change in the variable in that function then the original variable is not changed
# Python acts as call by value if passed data is immutable data types like tuples, strings and numbers

# Example 2 :-

string='Romeo'
def display(string):
    string='Romeo Siwach'
    print('The string inside the function is : ',string)
    print('Address of the string inside the function : ',id(string))
    return

display(string)
print('Value of string outside the function : ',string)
print('Address of the string outside the function is : ',id(string))