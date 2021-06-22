# Написать программу, которая получив на входе произвольный список удалит из него все повторяющиеся элементы.

string = input('Please input a sequence of list items separated by a space: ')

currentList = string.split(' ')
finalList = []
for item in currentList:
    if item == ' ':
        continue
    current = True
    while current:

        try:
            i = currentList.index(item)
            currentItem = currentList.pop(i)
            currentList.insert(i,' ')
        except Exception:
            finalList.append(currentItem)
            current = False

print('In the end we got such a list:', finalList)
