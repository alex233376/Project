import json


def get_stored_username():
    """Получить сохраненное имя пользователя, если доступно."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрос нового имени пользователя."""
    username = input("Как ваше имя? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствовать пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Это твоё имя?, {username}!")
        check = input("Если нет нажми 'n'")
        check == 'n'
        get_new_username()
    else:
        username = get_new_username()
        print(f"Мы будем помнить тебя, когда ты вернешься, {username}!")


greet_user()
