# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

n = int(input("Введите целое число>>>"))
if n < 10:
    print("максимальная цифра",n)
else:
    c = 0
    while n > 10:
        a = n % 10
        n = n // 10
        if a >= c:
            c = a
        else:
            c = c
    else:
        if c > n:
            print("максимальная цифра", c)
        else:
            print("максимальная цифра", n)