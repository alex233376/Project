import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует.."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя."""
    username = input("Как ваше имя ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """"Приветствует пользователя по имени.."""
    username = get_stored_username()
    if username:
        correct = input('Это ваше имя ' + username + "? (y/n) ")
        if correct =='y':
            print("Привет с возвращением " + username )
        else:
            """Если имя не коректно то вызываем get_new_username и запркшиваем имя"""
            username = get_new_username()
            print("Мы сохраним ваши данные " + username)
greet_user()