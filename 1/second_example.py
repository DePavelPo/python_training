# Составить программу нахождения корней квадратного уравнения в общем виде. 
# Коэффициенты запрашиваются у пользователя.

import math

print("There is quadratic ax^2 + bx + c = 0. We can come up and to decide this quadratic. ")

aRatio = float(input("Input a number: "))
bRatio = float(input("Input b number: "))
cRatio = float(input("Input c number: "))

discriminant = bRatio **  2 - 4 * aRatio * cRatio
print("Discriminant is:", discriminant)

if discriminant < 0:
    print("There is no roots of quadratic.")
elif discriminant == 0:
    sqrtDisc = math.sqrt(discriminant)
    print("there is only one root and this is:", round((-bRatio + sqrtDisc) / (2 * aRatio), 2))
else:
    #sqrtDisc = math.sqrt(discriminant)
    sqrtDisc = math.sqrt(discriminant)
    print("first root is:", round((-bRatio + sqrtDisc) / (2 * aRatio), 2))
    print("second root is:", round((-bRatio - sqrtDisc) / (2 * aRatio), 2))
