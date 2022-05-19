# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go
# stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.

class Car:
    speed : float
    color : str
    name : str
    is_police : bool

    def __init__(self,speed,  color, name, is_police):
        self.name=name
        self.color=color,
        self.spee=speed
        self.is_police=is_police

    def go(self):
        self.speed = float(input('Укажите скорость движения>>>'))
        print(f'{self.name} начала движение')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась')

    def turn(self):
        n=input('Укажите направление поворота>>>')
        print(f'{self.name} повернула на {n}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')

        if self.speed > 60:
            print(f'Превышение скорости!!!!!!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')

        if self.speed > 40:
            print(f'Превышение скорости!!!!!!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            print(f'{self.name} полицейская машина')
        else:
            print(f'Внимание {self.name} не полицейская машина!!!!!!!!!!!')

BMW = PoliceCar(0,'standart','BMW',True)
Opel = WorkCar(0,"белый", 'Opel',False)

BMW.go()
BMW.turn()
BMW.show_speed()
BMW.stop()
BMW.show_speed()
Opel.go()
Opel.turn()
Opel.show_speed()
Opel.stop()