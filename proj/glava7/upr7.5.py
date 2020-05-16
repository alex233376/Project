age = ('Введите свой возраст\n')
message = ""
while message == '':
	message = input(age)
	message = int(message)
	if message < 3:
		print('0$')
	elif message < 12:
		print('10$')
	else:
		print('15$')
	break
