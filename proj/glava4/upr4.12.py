my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Создаём копию списка
my_foods.append('cannoli')  # Добавляем блюда
friend_foods.append('ice cream')  # Добавляем блюда
print('Мои любимые блюда:')
for my_food in my_foods:
	print(my_food)
print('\nЛюбимые блюда друга:')
for fr_foods in friend_foods:
	print(fr_foods)
