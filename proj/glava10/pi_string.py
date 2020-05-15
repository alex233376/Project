filename = 'glava10/pi_million_digits.txt'

with open(filename) as file_object:
    # readlines() последовательно читает каждую строку из файла
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Какого числа вы родились ")
if birthday in pi_string:
    print("Ваш день рождения в ходит в 1 миллион числа пи ")
else:
    print("Ваш день рождения не появляется в первом миллионе цифр числа пи ")
