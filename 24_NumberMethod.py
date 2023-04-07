# Ronding a number -> In this method we use to round-off an number upto required decimals. Using formula [x = round(base,decimals)] #

pi = 3.1415926535897

twoDecimals = round(pi, 2)
print(twoDecimals)

threeDecimals = round(pi, 3)
print(threeDecimals)


# Raising a number to a power -> In this method we use to raise a number to a required power. Using formula [x=pow(base,exponential)] #

powerTwo = pow(2, 3)
print(powerTwo)

powerSix = pow(2, 6)
print(powerSix)


# Absolute Method -> Absolute or abs method is the method in mathematics to convert -ve value to +ve value. Using formula [x = abs(-value Or +ve value)]

negativeNum = abs(-2.55)
print(negativeNum)

positiveNum = abs(2.66)
print(positiveNum)


# Div-Mode Method -> In this method we can get the quotent and remainder after dividing two whole numbers whether they are intigers or floats but not complex numbers.
# Using formula [x=divmod(numerator,denominator)] result will be (quotent, remainder) And if num is lesser than deno then result will be (0,quotent)

numLarger = divmod(8, 6)
print(numLarger)

denoLarger = divmod(2, 5)
print(denoLarger)

denoLarger = divmod(3, 8)
print(denoLarger)
