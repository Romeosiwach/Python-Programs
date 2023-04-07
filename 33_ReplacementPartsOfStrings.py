# Replacing parts of python strings -> 
# In this if we want to modify a string by replacing any of its part then we can use this type of string.
# This replacement process is case sensitive we have to check the upper and lower case letters carefully before using it
#  Example 1
string1= "Romeo Siwach"
print(string1)

string2= string1.replace("Romeo", "Saksham")
print(string2)

# Example 2
line1="I love my India"
print(line1)
line2= line1.replace("India", "Country") 
print(line2)

# Example 3
line1="I hate India!!I hate India!!I hate India!!I hate India!!I hate India"
line2=line1.replace('hate', 'love')
print(line2)