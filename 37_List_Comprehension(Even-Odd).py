# List_Comprehension -> 
# A list comprehension is a concise way of creatng a new list from a existing list.
# it consist of a expression and a 'for' loop enclosed in a square brackets.

# Calculating powers upto a range :-
power=[]
for x in range (15):
    power.append(2**x)
print(power)

# Calculating even numbers upto a specific range :-
even=[x for x in range(20) if x%2==0]
print(even)

# Calculating Odd numbers upto a specific range :-
odd=[x for x in range(20) if x%2!=0]
print(odd)