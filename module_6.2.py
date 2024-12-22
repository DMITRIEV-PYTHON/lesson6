# Цели: Применить сокрытие атрибутов и повторить наследование.
# Рассмотреть на примере объекта из реального мира.
# Задача "Изменять нельзя получать":
# В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет,
# мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается
# не владельцем, а в специальных сервисах. Да, узнать значения этих свойств мы сможем,
# но вот изменить - нет.
# Пункты задачи:
# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают его методы, взяты из класса Vehicle.


class Vehicle:
    __COLOR_VARIANTS = ["blue", "red", "green", "black", "white"]

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):  # возвращает строку: "Модель: <название модели транспорта>"
        print(f"Модель: {self.__model}")

    def get_horsepower(self):  # возвращает строку: "Мощность двигателя: <мощность>"
        print(f"Мощность двигателя: :{self.__engine_power}")

    def get_color(self):  # возвращает строку: "Цвет: <цвет транспорта>"
        print(f"Цвет автомобиля:{self.__color.upper()}")

    def print_info(self):  # распечатывает результаты методов(в том же порядке)
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}\n")

    def set_color(self, new_color):
        color_auto = [name.lower() for name in self.__COLOR_VARIANTS] # переводим все названия цвета в нижний регистр
        if new_color.lower() in color_auto:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color.upper()}\n")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # в седан может поместиться только 5 пассажиров


vehicle1 = Sedan("Fedos", "Toyota Mark II", "blue", 500)
# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color("Pink")
vehicle1.set_color("BLaCk")
vehicle1.owner = "Vasyok"

# Проверяем что поменялось
vehicle1.print_info()
