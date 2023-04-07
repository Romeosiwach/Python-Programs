# Keywords argumets and parameters -> Keywords arguments or named arguments are the values that when passed into a function are identifiable by a specific parameter name. A keyword argument is proceded by a parameter and the assignment operator(=). The arguments passed are assigned according to their position. But when we use keyword agruments the positions does not matter.

def keywordFunc(fruit1,fruit2,fruit3,fruit4,fruit5,fruit6):
    print('Romeo likes the',fruit1)
    print('Vinay likes the',fruit2)
    print('Saksham likes the',fruit3)
    print('Surender likes the',fruit4)
    print('Kamlesh likes the',fruit5)
    print('Deepika likes the',fruit6)
    
keywordFunc(fruit1='Apple',fruit2='Mango',fruit3='Guava',fruit4='Grapes',fruit5='Watermelon',fruit6='Muskmelon')    

print()
keywordFunc('Apple','Mango','Guava','Grapes','Watermelon','Muskmelon')