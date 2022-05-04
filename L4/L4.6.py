# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count , cycle
n = int(input("Введите число>>>"))
List = count (n,1)
List2 = []
for x in List:
    List2.append(x)
    if x == n+10:
        break
print(List2)

from itertools import cycle

nn = ["a", "b", "c", "d", "f"]
List3 = cycle(nn)
List4 = []

for xx in List3:
    List4.append(xx)
    if len(List4) == 20:
        break
print(List4)