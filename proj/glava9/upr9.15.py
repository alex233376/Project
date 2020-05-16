import random

# выборка с заменой
rand = [2, 12, 7, 4, 3, 11, 15]
test_ticket = []
# Выбираем случайное количество значений из списка
# Без повторений random.sample
# Можно random.choices тогда повторяются
win_ticket = random.choices(rand, k=2)
print("Эта комбинация выиграла", win_ticket)
rand1 = [2, 12, 7, 4, 3, 11, 15]

while rand1:
	test = random.choices(rand1, k=2)
	print(test)
	if test == win_ticket:
		print('Вот она', test)
		break
