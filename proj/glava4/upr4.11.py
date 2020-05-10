my_pizzas = ['margherita', 'capricciosa', 'hawaii']
friend_pizzas = my_pizzas[:]
my_pizzas.append('rezoto')
friend_pizzas.append('kolbasa')
print("Мои любимые пиццы:")
for pizza_my in my_pizzas:
	print(pizza_my)

print("\nЛюбимые пиццы друга:")
for pizza_frend in friend_pizzas:
	print(pizza_frend)
