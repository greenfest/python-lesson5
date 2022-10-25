# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.

from random import *
from collections import Counter

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

listNums = [randrange(1,11) for i in range(1,11)]

print(f"Исходный список: {listNums}")
print("-"*30)

count = 0

for i in (list(Counter(listNums).values())):
  if i > 1:
    count += i

print(f"{count} элемента(ов) совпадают")
print(f"Список уникальных элементов: {f7(listNums)}")
