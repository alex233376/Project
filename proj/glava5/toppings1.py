available_toppings = [
	'mushroms', 'olives', 'green peppers',
	'pepperoni', 'pineapple', 'extra cheese'
]
requested_toppings = ['mushroms', 'french fries', 'pop', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Добавленно {requested_topping}')
	else:
		print(f'Извините, у нас нет {requested_topping}')
print('\nВаша пицца готова')
