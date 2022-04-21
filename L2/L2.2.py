# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
from typing import List

C = {1, 2, 3, 4, 5}
B = [1, 2, 3, 4, 5]
List1 = [1, -1, "Кит", 2.33, True, C, B]
List2 = []
A = 0
A2 = 1
A3 = len(List1)
while A2 < A3:
    List2.append(List1[A2])
    List2.append(List1[A])
    A += 2
    A2 += 2
else:
    A4 = len(List2)
if A4 == A3:
    List1 = List2
    print(List1)
else:
    List2.append(List1[len(List1) - 1])
    List1 = List2
    print(List1)
