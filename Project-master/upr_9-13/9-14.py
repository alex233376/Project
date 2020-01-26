from random import randint


class Die():
    def __init__(self, sides=6):  # задал атрибуты
        self.sides = sides

    def roll_die(self, rolls=1):  # метод для вывода случайного числа
        print(*[randint(1, self.sides) for _ in range(rolls)])


d1 = Die()       # 6-гранный кубик
d1.roll_die(10)  # 10 бросков

d2 = Die(10)  # 10 гранный кубик
d2.roll_die(10)  # 10 бросков

d3 = Die(20)  # 20 гранный кубик
d3.roll_die(10)  # 10 бросков
