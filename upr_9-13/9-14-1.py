from random import randint

class Die():
    """Описание класса кубиков."""

    def __init__(self, sides=6):
        """"Инициализировать кубик."""
        self.sides = sides

    def roll_die(self):
        """Возвращает число от 1 до количества сторон."""
        return randint(1, self.sides)

# Сделайте 6-гранный кубик и покажите результаты 10 бросков.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 бросков 6-сторон:")
print(results)

# Сделайте 10-гранный кубик и покажите результаты 10 бросков.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 бросков a 10-сторон:")
print(results)

# Сделайте 20-гранный кубик и покажите результаты 10 бросков.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 бросков of a 20-сторон:")
print(results)