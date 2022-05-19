# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
# "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name : str
    surname : str
    position : str
    _income = {"wage": float,"bonus": float}


    def __init__(self,name,surname,position,Wage=0,bonus=0):
        self.name = name
        self.surname=surname
        self.position=position
        self._income["wage"] = Wage
        self._income["bonus"] = bonus
class Position(Worker):
    def get_full_name (self):
      print(f'{self.surname} {self.name}')
    def get_total_income (self):
        print(Worker._income['wage']+ Worker._income["bonus"])


W1 = Position('Igor','Kar','Student',100,15)
print(W1.name,W1.surname,W1.position,W1._income)
W1.get_full_name()
W1.get_total_income()

