users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }
#  сохраняет каждый ключ в переменной username
for username, user_info in users.items():
    print(f"\nUsername: {username}")  # выводится имя пользователя
#  Сохраняем имя фамилию
    fullname = f"{user_info['first']} {user_info['last']}"
#  Сохраняем место
    location = user_info['location']
    print(f"\tПолное имя {fullname.title()}")
    print(f"\tМесто {location.title()}")
