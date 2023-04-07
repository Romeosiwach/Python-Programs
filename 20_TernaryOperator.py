# Ternary Operator ->
# Use of ternary operator is to make the code more concise(Compact).
# Ternary operator in Python is :- "value_if_true if condition else value_if_false"

#1# Normal Code #
age=input("Enter the age : ") 
if int(age)>=18:
    ticket_price=20
else:
    ticket_price=5
    
print("You have to pay : ",ticket_price)        

#2# Concise Code #

age=input("Enter the age : ")
ticket_price = 20 if int(age)>=18 else 5
print("You have to pay : ",ticket_price)