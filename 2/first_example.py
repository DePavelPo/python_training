# Написать программу, выводящую заданную пользователем строку как минимум в 3 разных кодировках. 
# При этом писать вызов метода encode() в программе можно только 1 раз.

string = input("Input string: ")
strUTF = string.encode("UTF-8")
strASC = string.encode("ASCII")
strCP = string.encode("CP1251")
print(strUTF)
print(strASC)
print(strCP)
print(str(strUTF, "UTF-8"))
print(str(strASC, "ASCII"))
print(str(strCP, "CP1251"))

