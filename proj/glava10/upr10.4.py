filename = 'glava10/guest.txt'
while True:
    message = input("Введите ваше имя ")
    with open(filename, 'a') as file_object:
        file_object.writelines(f"Your name {message}\n")
