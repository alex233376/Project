age = 'Введите свой возраст\n'
exx = 'Выход '
active = True
while active:
	message = input(age)
	message = int(message)
	if message < 3:
		print('0$')
	elif message < 12:
		print('10$')
	else:
		print('15$')
	message1 = input(exx)
	if message1 == 'quit':
		active = False
