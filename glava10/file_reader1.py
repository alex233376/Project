# последовательная обработка каждой строки в файле
filename = 'D:/Project/glava10/pi_digits.txt'

with open (filename) as file_object:
    for line in file_object:
        print(line.rstrip()) #rstrip() в команде print удаляет лишние пустые строки
