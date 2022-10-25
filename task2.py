# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.

from random import *
listNums = [randrange(1,11) for i in range(1,11)]
print(f"Исходный список: {listNums}")
print("-"*30)

listSequenceOfNums = []
listSequenceOfNums.append(listNums[0])
for i, value in enumerate(listNums):
  if listSequenceOfNums[-1] < listNums[i]:
    listSequenceOfNums.append(value)
    
print(f"Возрастающая последовательность: {listSequenceOfNums}")


