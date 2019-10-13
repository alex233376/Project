filename = 'D:/Project/glava10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''

for line in lines:
    pi_string += line.rstrip()
birthday = input("Введите свой день рождения в виде mmddyy: ")

if birthday in pi_string: # проверяет вхождение этой строки в pi_string
    print("Ваш день рождения есть в первом миллионе цифр числа пи!")
else:
    print("Вашего деня рождения нет в первом миллионе цифр числа пи.")
