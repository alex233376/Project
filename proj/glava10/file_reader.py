filename = 'glava10/pi_digits.txt'
with open(filename) as file_object:
    # readlines() последовательно читает каждую строку из файла
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())  # выводятся все элементы списка lines
