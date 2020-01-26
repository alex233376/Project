filename = 'D:/Project/glava10/programming.txt'

with open(filename, 'w') as file_object:# 'w' аргумент записи
    # метод write() используется для записи строки в файл
    file_object.write("I love programming.\n")# делаем перенос строк \n
    file_object.write("I love creating new games.\n")