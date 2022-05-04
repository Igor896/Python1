# !!!!!!!!Не уверен, что правильно понял задание, на всякий случай добавляю такой вариант!!!!!!!


from itertools import count
from math import factorial

def for_el_in_fact():
    for el in count(int(input("Введите число>>>"))):
        yield factorial(el)

gen = for_el_in_fact()
x = 0
for i in gen:
    if x < 10:
        print(i)
        x += 1
    else:
        break