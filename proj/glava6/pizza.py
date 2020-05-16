# Сохранение информации о заказанной пицце.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
# Описание заказа.
print(f"Вы заказали {pizza['crust']} "
      "со следующими начинками:")

for topping in pizza['toppings']:
	print(f"\t" + topping)
