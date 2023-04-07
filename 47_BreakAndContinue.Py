'Break and Continue Statements -> The "Break" statement stops the execution of loop and "Continue" statement stops the current iteration of loop and continues the another loop iteration.'

"Break Statements:-"
# Example 1:-
myFamily = ["Surender", "Romeo", "Vinay", "Saksham", "Kamlesh", "Deepika"]

for member in myFamily:
    if member == "Saksham":
        break
    print('The member of family is ', member)

# Example 2:-
i = 0
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1

"Continue Statements :-"
# Example 1:
food = ['Dal', 'Mushroom', 'Paneer', 'Chaap', 'Rice', 'Fish', 'Chicken']
for veg in food:
    if veg == 'Fish':
        continue
    if veg == 'Chicken':
        continue
    print('Vegetarian types of food are ', veg)

# Example 2:
i = 0
while i <= 10:
    i += 1
    if i == 6:
        continue
    print(i)
   
