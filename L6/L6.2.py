# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для
# покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
class road:
    lenght : float
    width : float
    thickness : float(0.05)
    weight : float(2.25)

    def __init__(self, lenght, width, thickness=0.05, weight=2.25):
        self.weight = weight
        self.width = width
        self.lenght = lenght
        self.thickness = thickness

    def Total_weight(self):
        tw = self.weight*self.width*self.lenght*self.thickness
        print(f'Общий вес асфальтового покрытия {tw} т.')


M60 = road(float(input("Введите длину дороги в метрах>>>")),float(input("Введите ширину дороги в метрах>>>")))
M60.Total_weight()
