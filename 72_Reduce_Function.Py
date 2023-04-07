# Reduce Function :-
# Reduce function in Python is used for performing some computation on a list and returning a result.
# It applies a rolling computation to a sequential pair of values in a list

# Example For appliying product computation on a pair of list using 'For' Loop :-
# product=1
# lists=[1,2,3,4,5]
# for num in lists:
#     product=product*num
# print(product)
    
# Example using the Reduce function computing product of items in list :-
from functools import reduce
lists=[1,2,3,4,5]
product=reduce(lambda product,num:product*num,lists)
print(product)