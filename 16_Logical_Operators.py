### Logic Operators -> Python lang has three type of operators and,or & not ###
#1# And Operator -> If both the conditions are true then it will show true either it will show false #
price=9.5
print(price>9 and price<10)
print(price>9 and price>10)
print(price<9 and price<10)
print(price<9 and price>10)

#2# or Operator -> If both the conditions are false then it will show result false otherwise it will show true #
price=9.5
print(price>9 or price<10)
print(price>9 or price>10)
print(price<9 or price<10)
print(price<9 or price>10)

#3# not Operator -> Not operator reverses the result to opposite #
price=9.5
print(not price >9)
print(not price <10)
print(not price >10)
print(not price >10)

print(not(price>9 and price<10))
print(not(price>9 and price>10))
print(not(price<9 and price<10))
print(not(price<9 and price>10))

#*****# On priority basis the operators are operated from left to right in a line and on priority basis sequence is (not>and>or)
# Example
# a or (b and c) - Here b and c are operated first and then the result is operated with a or .
# (a and b) or (c and d) - Here a and b is operated first then c and d are operated then both results are operated with or
# ((not a)and b)or c - Here not a is operated first then resukt is operated with and b and then the result is operated with or c.