import random
from random import randint
# выборка с заменой
rand = [2, 12, 7, 4, 3, 11, 15]
# Выбираем случайное количество значений из списка
# Без повторений random.sample
# Можно random.choices тогда повторяются
win_ticket = random.choices(rand, k=2)
print("Эта комбинация выиграла", win_ticket)
