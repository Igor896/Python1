# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до
# 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.


Line = [x for x in range(100, 1001) if x % 2 == 0]
n = 0
s = 1
while n < len(Line):
    s = s * Line[n]
    n += 1
else:
    print(Line)
    print(s)


from functools import reduce
Line2 = [x for x in range(100, 1001) if x % 2 == 0]

s2 = reduce((lambda x, y: x * y), Line2)

print(s2)