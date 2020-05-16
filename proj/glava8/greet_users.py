def greet_users(names):
	"""Вывод простого приветствия для каждого пользователя в списке."""
	for name in names:
		msg = f'Hello {name.title()}'
		print(msg)


usernames = ['alex', 'petro', 'vasia']
greet_users(usernames)
