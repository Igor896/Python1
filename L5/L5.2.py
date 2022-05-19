# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('DZ52.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('DZ52.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    content2 =content[i].split(" ")
    print(content2)
    print(f'Окличество слов {i + 1}-ой строке {len(content2)}')

my_file.close()