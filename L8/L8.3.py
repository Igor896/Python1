# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу
# исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                a = (input('Введите значение и нажмите Enter - (для завершения введите q)'))
                val = int(a)
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                if a != 'q':
                    print(f"Недопустимое значение")

                else:
                    print(f'Текущий список - {self.my_list} \n ')
                    break


try_except = Error(1)
try_except.my_input()