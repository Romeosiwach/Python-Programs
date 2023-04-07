# Enumrate Function :-
# By using this enumrate function we can provide the serial numbers to the items of the list
# It is a build in Python function it loops over alist of items to provide it numbering

# Example 1 :- Providing normal serial numbers to a list
fruits=['apple','mango','banana','guavava','pineapple','grapes']
for counter,value in enumerate(fruits):
    print(counter,value)

# Example 2 :- Providing numbering to a list starting from 1
fruits=['apple','mango','banana','pineapple','grapes','guavava']
for counter, value in enumerate(fruits,1):
    print(counter,value)
    
# Example 3 :- Providing numbering to a list by converting it into a tuple
fruits=['apple','mango','banana','pineapple','grapes','guavava']   
tuples=list(enumerate(fruits,1))
print(tuples)
    