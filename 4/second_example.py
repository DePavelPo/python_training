# Напишите подпрограмму табулирования функции, переданной в качестве аргумента. 
# Так же аргументами задается начальное, конечное значение и шаг табуляции.

import logging

TRY_AGAIN = 'Try again\n'

logging.basicConfig(format='\n%(levelname)s %(asctime)s : %(message)s', 
                    datefmt='%d/%m/%Y %I:%M:%S'
)

def func(x):
    return str(x * x - (x%3))

def functiontabl(func, xn, xk, dx):
    result = []
    
    while xn <= xk:
        couple = {}
        if xn + dx > xk:
            couple['x'] = str(xk)
            couple['result'] = func(xk)
            result.append(couple)
            break
        couple['x'] = str(xn)
        couple['result'] = func(xn)
        result.append(couple)
        xn = xn + dx
        
    return result

while True:

    try:
        xn = int(input('Input initial segment\'s value for tabulation: '))
        xk = int(input('Input final segment\'s value for tabulation: '))
        dx = int(input('Input step for tabulation: '))
    except Exception as exc:
        logging.error('Incorrect input, ' + str(exc))
        print(TRY_AGAIN)
        continue     
    
    if xn > xk:
        logging.error('The initial value must be less than the final')
        print(TRY_AGAIN)
        continue
    if dx <= 0:
        logging.error('The path value must be greater than 0')
        print(TRY_AGAIN)
        continue
    break

print('Results :', functiontabl(func, xn, xk, dx))
