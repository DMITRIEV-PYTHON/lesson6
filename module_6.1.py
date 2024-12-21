# Цель: применить базовые знания о наследовании классов для решения задачи
# Задача "Съедобное, несъедобное":
# Разнообразие животного мира давно будоражит умы человечества. Царства, классы, виды...
# Почему бы и нам не попробовать выстроить что-то подобное используя наследования классов?
# Необходимо описать пример иерархии животного мира, используя классы и принцип наследования.

class Animal:
    alive = True  # изначально живой
    fed = False  # изначально голодный

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:  # тут проверяем bool-атрибут для наследников Plant
            print(f"{self.name} съел {food.name}")
            self.fed = True  # тут переопределем атрибут сытости
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # тут переопределяем атрибут жизнеспособности


class Plant:
    edible = False  # по умолчанию все Plant несъедобные

    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass  # наследует атрибут несъедобное


class Fruit(Plant):
    edible = True  # переопределили атрибут для Fruit на съедобное


a1 = Predator("Волк с Уолл-Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")

print(a1.name)  # выврдим название первого животного
print(p1.name)  # выводим название первого растения

print(a1.alive)  # первое животное живое
print(a2.fed)  # второе животное голодное

a1.eat(p1)  # режим еды
a2.eat(p2)  # режим еды

print(a1.alive)  # животное умерло
print(a2.fed)  # животное наелось
