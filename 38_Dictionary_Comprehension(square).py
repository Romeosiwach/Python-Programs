# Dictionary comprehension ->
# This is the concise way of creating a new dictionary from a Python loops(iterables).

# Squaring the items upto a range :-
square = {number: number**2 for number in range(20)}
print(square)
print(type(square))

# Square of Odd numbers upto a specified range :-
odd = {number: number**2 for number in range(20) if number%2!= 0}
print(odd)

# Square of even numbers upto specified range :-
even={number: number**2 for number in range(20) if number%2==0}
print(even)
