print("Введите два числа и я поделю их ")
print("Нажмите 'q' для выхода" )

while True:
    first_number = input("\nПервое число ")
    if first_number == 'q':
        break
    second_number = input("Второе число ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("На ноль не делится ")
    else:
        print(answer)