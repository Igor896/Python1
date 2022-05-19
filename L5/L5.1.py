# 1. Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

DZ51 = open('DZ51.txt', 'w')
line = input('Введите текст>>> ' )
DZ51.writelines(f"{line}\n")
while line:
    line = input('Введите текст или нажмите энтр для окончания>>> ')
    DZ51.write(f"{line}\n")
    if not line:
        break
DZ51.close()
DZ51 = open('DZ51.txt', 'r')
line2  = DZ51.readlines()
for ln in line2:
  print(ln.replace("\n",""))
DZ51.close()