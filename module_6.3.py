# Задача "Ошибка эволюции":
# Создать 5 классов

import random


class Animal:
    live = True
    sound = None  # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве.
        self.speed = speed  # скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True  # обладает наличием клюва

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f"Here are(is) {eggs_count} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        if self._cords[2] - dz * (self.speed / 2) < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] -= dz * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"


# Пример использования классов
if __name__ == "__main__":
    db = Duckbill(speed=10)

    print(db.live)  # вывод атрибута "живой"
    print(db.beak)  # вывод наличия клюва

    db.speak()  # голос утконоса
    # print(Animal._DEGREE_OF_DANGER)  # степень опасности существа
    db.attack()  # существо опасно

    db.move(1, 2, 3)  #
    db.get_cords()  # поскольку Z>0 изменения вносятся
    db.dive_in(6)  #
    db.get_cords()  # поскольку перед этим Z=30, теперь 30-6*(10/2) = 0

    db.lay_eggs()  # вывод случайного числа яиц
