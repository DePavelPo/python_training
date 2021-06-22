# Написать программу поиска самого длинного слова в строке, разделенной пробелами.

string = input('Input string: ')

stringWords = string.split(" ")

maxWord = ''
maxWordList = []

for str in stringWords:
    if len(str) > len(maxWord):
        maxWord = str
        maxWordList.clear()
        maxWordList.append(str)
    elif len(str) == len(maxWord):
        maxWordList.append(str)

# ', '.join() позволяет вывести все элементы списка с разделением их запятой

print('Longest word/words:', ', '.join(maxWordList))