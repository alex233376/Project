def list_pet(pet):#создаём фуркцию 
    try:
        with open(pet) as f:
            contents = f.read()# метод read(),читает все содержимое файла и сохраняет его в строке
    except FileNotFoundError:# обрабатывает ошибку и выводит сообщение если файл не найден
        pass
    else:# если исключений нет срабатывает этот код
        words = str(contents)# если использовать метод .split() то выведет список[]
        print(words)
pets = 'D:/Project/glava10/cats', 'D:/Project/glava10/dogs'
for pet in pets:# создаём цикл
    list_pet(pet)# вызываем функцию выводим содержание обоих файлов