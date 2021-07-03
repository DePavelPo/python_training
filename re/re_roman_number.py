# Перевести римское число в арабское.

import re

roman = input('Input some roman number: ')

isCorrectRoman = re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', roman)

if isCorrectRoman != None:
    print('Correct')
else:
    print('Incorrect')
