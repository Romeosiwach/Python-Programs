message='This is an example of single quote'
print(message)

message="This is an example of double quotes"
print(message)

message="This's an example of single quote in double quote"
print(message)

message='This"s an example of double quote in single quotes'
print(message)

message='"Beautyful is better than ugly",said Tim Peters'
print(message)

message='it\'s also a valid string'
print(message)

message=r'c:\python\user'
print(message)


# Multi line strings #
help_message='''
usage:mysql commands
-h host name
-d database name
-u username
-p password
'''
print(help_message)

#  Using varibles in strings #
name="Romeo"
message=f'Hi,{name}'
print(message)