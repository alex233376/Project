# Создание списка строк по содержимому файла
filename = 'D:/Project/glava10/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()# последовательно читает каждую строку из файла и сохраняет ее в списке.
for line in lines:
    print(line.rstrip())
