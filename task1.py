# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.

from random import *
listNums = [randrange(1,11) for i in range(1,11)]
print(f"Исходный список: {listNums}")
print("-"*30)
listNums = list(filter(lambda x: x > 5, listNums))
print(f"Итоговый список: {listNums}")