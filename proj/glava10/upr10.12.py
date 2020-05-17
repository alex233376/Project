import json

filename = 'num.json'
try:
    with open(filename) as f:  # Открываем файл если
        # файл существует выводим Я знаю ваше число
        num = json.load(f)
except FileNotFoundError:
    num = input('Ваше число ')  # Если файла нет просим ввести число
    with open(filename, 'w') as f:
        json.dump(num, f)  # Записываем число
        print(f'Вот ваше число {num} ')
else:
    print(f'Я знаю ваше число {num} ')
