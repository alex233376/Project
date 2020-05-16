import json

username = input('Как ваше имя ')

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f'Мы будем помнить тебя, когда ты вернешься {username}')
    