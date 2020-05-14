import random
# выборка с заменой
rand = [20, 30, 40, 50, 60, 70, 80, 'd', 'f', 'g', 'a']
# Выбираем случайное количество значений из списка
# Без повторений random.sample
# Можно random.choices тогда повторяются
sampling = random.sample(rand, k=4)
print("Эта комбинация выиграла", sampling)
