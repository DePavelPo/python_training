# Составить программу вывода таблицы умножения на число M. 
# Таблица составляется от M * a, до M * b, где M, a, b запрашиваются у пользователя. 
# Вывод должен осуществляется в столбик, по одному примеру на строку в следующем виде (например):
#       5 х 4 = 20
#       5 х 5 = 25
# И так далее.

import logging
import datetime
import time

logging.basicConfig(filename='logs' + datetime.datetime.now().strftime("%d.%m.%Y")+ '.log',
                    level=logging.INFO, 
                    format='%(levelname)s %(asctime)s : %(message)s', 
                    datefmt='%d/%m/%Y %I:%M:%S'
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s %(asctime)s : %(message)s')
console.setFormatter(formatter)

logging.getLogger('').addHandler(console)
logger = logging.getLogger(__name__)

logger.info('Start')

print("We need to output multiplication table for number M, from a to b.")
correct = True
while correct:

    try:
        M = int(input("Please input M: "))
        a = int(input("Input a: "))
        b = int(input("Input b: "))
    except Exception as e:
        logger.error("Incorrect input, " + str(e))
        print("Try again")
        continue
    correct = False

for x in range(a, b+1):
    print("%d x %d = %d" % (M, x, M*x))
    time.sleep(0.5)

logger.info('End')