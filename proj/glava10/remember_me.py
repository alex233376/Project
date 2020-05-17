import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
#  В противном случае она запрашивает имя пользователя и сохраняет его.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Введите ваше имя ")
    with open(filename, 'w') as f:
        json.dump(username, f)  # сохраняем данные пользователя
        print(f"Мы будем помнить тебя, когда ты вернешься {username}")
else:
    print(f'С возвращением {username}')
