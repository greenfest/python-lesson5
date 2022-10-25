from random import *
listNums = [randrange(1,11) for i in range(1,11)]
print(f"Исходный список: {listNums}")
print("-"*30)
listNums = list(filter(lambda x: x > 5, listNums))
print(f"Итоговый список: {listNums}")