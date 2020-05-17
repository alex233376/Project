import json

favorite_num = input('Ваше любимое число ')
filename = 'num.json'
with open(filename, 'w') as f:
    json.dump(favorite_num, f)  # Записываем ввод в файл

filename = 'num.json'
with open(filename) as f:
    num = json.load(f)
    print(f'Я знаю ваше число {num} ')
