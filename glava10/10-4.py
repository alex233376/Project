user_name = input('Введите своё имя\n')
print(user_name, 'Hello')
#while user_name:
filename = 'D:/Project/glava10/guest_book.txt'
with open(filename, 'a') as file_object:
    file_object.write( user_name )
    file_object.write(' Hello\n')
