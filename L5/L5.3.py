# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('DZ53.txt', 'r') as my_file:
    S = []
    N = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        S.append(int(i[1]))
        if int(i[1]) < 20000:
          N.append(i[0])

print(f'Оклад меньше 20.000 {N}, средний оклад {sum(map(int, S)) / len(S)}')