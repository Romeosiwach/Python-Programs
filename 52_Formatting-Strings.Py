'Formatting Strings -> Un Python we can format the strings by adding some more sub strings into it, the format() function allows us to format the strings.'
'Placeholders{} -> The place holdrs helps us to cotrol which part of the string shopld be formatted.They are defiined using curly braces'
'There are three types of formatting strings :-'
'1. Multiple place holders - If we want to format multiple parts of the string then we use multiple place holders '
'2. Using Indexes - We use index numbers to specify exactly here should we add the string, the index number sholbe nside the curly braces {index number} like {0} representing the first value and {1} as second value'
'3. Using named indexes - We can use the named indexes to specify exactly where to put the string likely numbers.'

# Example 1:-
mbd='The student {} is learning mbd course from Jetking'

student1=mbd.format('Romeo Siwach')
student2=mbd.format('Saksham')

print(student1)
print(student2)

# Example 2:-
mbd='The students {}, {} and {} are learning MBD course from the Jetking Institute.'

students=mbd.format('Romeo','Vinay','Saksham')
print(students)

# Example 3:-
mbd='The students {0}, {2}, and {1} are learning MBD course from Jetking Institute.'

students=mbd.format('Romeo','Saksham','Vinay')
print(students)

#  Example 4 :-
abc='The colour of {fruit} is {color}.'

result=abc.format(fruit='apple',color='red')

print(result)