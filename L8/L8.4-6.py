# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.



class Depot:
    def __init__(self, title):
        self.title = title
        self.lists = {}
        self.give_lists = {}

    def take_to_depot(self, equipment):
        self.lists.update({equipment.serial_number:[equipment.title, self]})
        print(f'На объект {self.title} получено оборудование: {equipment.title} ,серийный номер - {str(equipment.serial_number)}')


    def give_to_depot(self, equipment, other):
        self.give_lists.update({equipment.serial_number: [equipment.title,other]})
        print(f'Передано оборудование: {equipment.title} ,серийный номер - {str(equipment.serial_number)}')
        other.take_to_depot(equipment)


    def list_equipments(self):
        print(f'На объект {self.title}  получено оборудование:')
        print(self.lists)
        print(f'Общее количество: {len(self.lists)}')
        print(f'Со объекта {self.title}  выдано оборудование:')
        print(self.give_lists)
        print(f'Общее количество:  {len(self.give_lists)}')




class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  f'Название модели: {Office_equipment.__str__(self)} Параметры: {str(self.print_velocity)}'


class Scanner(Office_equipment):
    def __init__(self, title,serial_number,Scanner_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.Scanner_velocity = Scanner_velocity

    def __str__(self):
        return  f'Название модели:{Office_equipment.__str__(self)} Параметры: {str(self.Scanner_velocity)}'

class Copier(Office_equipment):
    def __init__(self, title,serial_number, Copier_velocity):
        Office_equipment.__init__(self, title, serial_number)
        self.Copier_velocity = Copier_velocity

    def __str__(self):
        return  f'Название модели: {Office_equipment.__str__(self)} Параметры: {str(self.Copier_velocity)}'



store1 = Depot('Склад')
store2 = Depot('Офис')

a = Printer('Принтер',123456,100)
b = Scanner('Сканер',123457,30)
c = Copier('Копировальный аппарат',123458, 25)


print(a)
print(b)
print(c)

store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)



store1.give_to_depot(a,store2)
store1.give_to_depot(c,store2)

store1.list_equipments()
store2.list_equipments()