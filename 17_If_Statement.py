# If Statement -> The 'IF' statement checks the codition first, If the condition evaluates to true then it executes the statement otherwise ignore it or moves to next condition. #

age=input("Enter your age : ")
if int(age) >= 18:
    print("You are eligible to vote, let's go for voting.")
if int(age)<18:
    print("You are not eligible for voting")
    
    