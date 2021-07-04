# Перевести римское число в арабское.

import re

while True:

    roman = input('Input some roman number: ')
    isCorrectRoman = re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman)

    if isCorrectRoman != None:

        roman = re.sub('CM|XC|IX', '9', roman)
        roman = re.sub('DCCC|LXXX|VIII', '8', roman)
        roman = re.sub('DCC|LXX|VII', '7', roman)
        roman = re.sub('DC|LX|VI', '6', roman)
        roman = re.sub('D|L|V', '5', roman)
        roman = re.sub('CD|XL|IV', '4', roman)
        roman = re.sub('MMM|CCC|XXX|III', '3', roman)
        roman = re.sub('MM|CC|XX|II', '2', roman)
        roman = re.sub('M|C|X|I', '1', roman)

        t = ''
        roman += t.rjust(4 - len(roman), '0') 

        print('Arabic number is: ', roman)
        break
    else:
        print('Incorrect number. Try again')
