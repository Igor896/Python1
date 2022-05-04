# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import random

Line =[ x for x in range(0,100)]
print(Line)
random.shuffle(Line)
print(Line)
n = 0
a = int(len(Line) - 1)
Line2=[]
while n < a:
    if Line[n] < Line[n+1]:
        Line2.append(Line[n+1])
        n += 1
    else:
        n +=1

else:
   print(Line2)