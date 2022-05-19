# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summary():
    try:
        with open('DZ55.txt', 'w+') as DZ55:
            line = input('Введите цифры через пробел>>> \n')
            DZ55.writelines(line)
            X = line.split()
            print(sum(map(int, X)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()