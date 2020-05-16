from random import randint


class Dice:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_dice(self, rolls=1):
		"""* распаковывает список
		randint(1, self.sides) генерирует число рандомное
		for производит заданное количество бросков
		"""
		print(*[randint(1, self.sides) for q in range(rolls)])


d1 = Dice()  # 6-граней
d1.roll_dice(10)  # 10 бросков

d2 = Dice(10)
d2.roll_dice(10)

d3 = Dice(20)
d3.roll_dice(10)
