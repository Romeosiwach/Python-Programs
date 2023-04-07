# If_Elif_Else Statement -> The 'IF' statement checks the codition first, If the condition evaluates to true then it executes the statement otherwise or moves to Elif condition and if it is found true then exexutes or rather moves to Else condition. #

age=input("Enter your age : ")
if int(age) <= 5:
    ticket_price=5
elif (5 < int(age) <= 18):
    ticket_price = 10
else:
    ticket_price = 20

print("You ticket price is : ",ticket_price)