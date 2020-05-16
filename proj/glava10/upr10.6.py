print('Введите два числа и я сложу их ')
first_num = input("Первое число ")
second_num = input("Второе число ")
try:
    result = int(first_num) + int(second_num)
except ValueError:
    print('Введите число а не иной символ ')
else:
    print(result)
