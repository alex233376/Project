def list_pet(pet):#создаём фуркцию pet
    try:
        with open(pet) as f:
            contents = f.read()# метод read(),читает все содержимое файла и сохраняет его в строке
    except FileNotFoundError:# обрабатывает ошибку и выводит сообщение
        print("Извините файл не найден ")
    else:
        words = contents.split()
        print(words)
pets = 'D:/Project/glava10/cats', 'D:/Project/glava10/dogs'
for pet in pets:
    list_pet(pet)