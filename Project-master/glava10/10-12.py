import json

favorite_number = 'user_number.json'
try:
    with open(favorite_number) as f_obj:#открываем файл user_number.json
        user_number = json.load(f_obj)#если файл существует, программа читает его в память
except FileNotFoundError:#если файла нет запрашивает число с нова и записывает его
    user_number = input('Ваше число ')
    with open(favorite_number,'w') as f_obj:
        json.dump(user_number, f_obj)
        print('Ваше число сохранено ' + user_number)
else:
    print('Вот ваше число ' + user_number)#если файл есть выводит число