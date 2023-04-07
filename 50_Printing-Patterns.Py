'Patterns in Python -> We need to take two loops  one is for row(i) and one is for column(j) that we want to print'
# Example 1:
for i in range(1, 11):
    for j in range(1, 11):
        print('~', end='')
    print()
    
# Example 2:
row=10
for i in range(1,row+1):
    for j in range(1,i+1):
        print('@',end='')
    print('')    
    
# Example 3:
for i in range(5):
    for j in range(5):
        print('^',end="") # Here end=" ", is used to print # in same line and not in new line.
    print()    
 
#  Example 4:
for i in range(10):
    for j in range(i+1):
        print('$',end='')       
    print()  
    
# Example 5:
for i in range(10):
    for j in range(10-i):
        print('%',end='')
    print()    