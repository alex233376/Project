users = ['petro', 'ivan', 'vasia', 'admin', 'frol']
if users:  # Проверяем что список не пуст
    for user in users:
        if user == 'admin':  # Проверяем Админа
            print(f'Привет Админ как дела')
        print(f'Привет {user}')  # В цикле преветствуем юзеров
else:
    print('Нет пользователей')  # Если нет юзеров сообщаем
