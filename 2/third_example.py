# Написать программу декодирования телефонного номера для АОН.
# По запросу АОНа АТС посылает телефонный номер, используя следующие правила:
# — Если цифра повторяется менее 2 раз, то это помеха и она должна быть отброшена
# — Каждая значащая цифра повторяется минимум 2 раза
# — Если в номере идут несколько цифр подряд, то для обозначения «такая же цифра как предыдущая» используется идущий 2 или более подряд раз знак #

# Например, входящая строка 4434###552222311333661 соответствует номеру 4452136

from string import digits

while True:

    string = input('Input string: ')

    allowed = set(digits).union('#')
    if all(char in allowed for char in string):
        number = []
        prevChar = ''
        repeat = False
        rememberChar = ''
        for char in string:
            if char == '#' and prevChar != '#':
                rememberChar = prevChar
            elif char == '#' and prevChar == '#' and repeat == False:
                repeat = True
                number.append(rememberChar)
            elif char != prevChar:   
                repeat = False
            elif char == prevChar and repeat == False:
                repeat = True
                number.append(prevChar)
            
            prevChar = char
        
        print('Corrent number:', ''.join(number))
        break
    else:
        print('\nIncorrect input string. Try again...\n')   
