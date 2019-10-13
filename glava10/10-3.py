user_name = input('Введите своё имя\n')
filename = 'D:/Project/glava10/guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(user_name)