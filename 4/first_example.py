# Напишите функции поиска НОД и НОК двух чисел.

from .second_example import functiontabl

def gcd(a, b):
    """Нахождение НОД"""
    while a != 0:
        a,b = b%a,a
    return b

def lcm(a, b, numgcd):
    """Нахождение НОК"""
    return int(a * b / numgcd)

while True:
    
    try:
        firstNumber = int(input('Input first number: '))
        secondNumber = int(input('Input second number: '))
        break
    except Exception as exc:
        print("Incorrect input, " + str(exc))
        print("Try again")
        continue

numGCD = gcd(firstNumber, secondNumber)

print(numGCD)

print(lcm(firstNumber, secondNumber, numGCD))
