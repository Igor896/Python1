# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            z= divider/denominator
            print (z)
        except:
            return print(f"Делить на ноль нельзя")


x = int(input('Введите числитель'))
y = int(input("Введите знаменатель"))
DivisionByNull.divide_by_null(x,y)
