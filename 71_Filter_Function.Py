# Filter Function :-
# A Filter function creates a list of elements for which a function returns true.
# The filter resembles a for loop but it is a built in function and faster.

# Example :-
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)