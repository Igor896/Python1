# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
# !!!!! В задание не было сказано, что требуется создать функцию!!!!!
S = 0
C = ""
while C =="":
    Line = input("Напишите послидовательность чисел, разделенных пробелом. Для выхода введите`q`>>>")
    Line2 = Line.split(" ")
    for el in Line2:
        if el == "q":
            print(S)
            break
        else:
            S = S + int(el)
            print(S)
    else:
        C = input("Продолжить?")

