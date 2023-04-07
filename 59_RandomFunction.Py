# 'Random Function :- The random function lets us to generate a random float number from 0.0 to 1.0'
# 'To use random() function we have to import it first'

# # Example 1:-
# import random
# randomNumber= random.random()
# print(randomNumber)

# '# The random.randint(x,y) method generates the random intiger in the range of x to y '
# # Example 2:-
# import random
# xValue=random.randint(1,10)
# print(xValue)
# yValue=random.randint(1,10)
# print(yValue)
# print(xValue,yValue)

'# Example program for generating random password for Banking customers'
# Example 3:-
import random

lower="abcdefghijklmnopqrstuvwxyz"

upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numbers='0123456789'

symbols='!@#$%^&*()_-=+{}[]<>;:|?/'

length=5

requirementsPassword=lower+upper+numbers+symbols

requirementsCaptcha=lower+upper+numbers

strongPassword=" ".join(random.sample(requirementsPassword,length))

Captcha=" ".join(random.sample(requirementsCaptcha,length))

print('Congratulations, Your password is generated')
print(strongPassword)

print('Captcha generated successfully')
print(Captcha)





