current_users = ['alex', 'admin', 'petro', 'vasia', 'karl']
new_users = ['nata', 'ira', 'karl', 'Luba', 'admin']

for news_users in new_users:  # перебираем список новых юзеров
	if news_users in current_users:  # Проверяем вхождение имен
		print(f'Имя занято {news_users.lower()}')
	else:
		print(f'Имя свободно {news_users.lower()}')
