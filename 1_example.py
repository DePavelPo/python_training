# Составить программу расчета гипотенузы прямоугольного треугольника. 
# Длина катетов запрашивается у пользователя.

import math

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

out = math.sqrt(num1 ** 2 + num2 ** 2)

print("The result number is: ", out)