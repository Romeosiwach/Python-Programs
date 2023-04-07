'Python Iterators -> Python iterators are used to iterate or repeat through, Iter() function is used to do so.'
# Examp)le 1:- Without using Iterators
family = ['Romeo', 'Vinay', 'Saksham', 'Surender', 'Kamlesh', 'Deepika']
for members in family:
    print('The member of family is : ', members)


# Example 2:- With Iterators
family = ['Romeo', 'Vinay', 'Surender', 'Saksham', 'Kamlesh', 'Deepika']
members = iter(family)

print('First member of family is : ', next(members))
print('Second member of family is : ', next(members))
print('Third member of family is : ', next(members))
print('Fourth member of family is : ', next(members))
print('Fifth member of family is : ', next(members))
print('Sixth member of family is : ', next(members))
