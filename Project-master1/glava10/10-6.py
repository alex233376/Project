while True:
    first_number = input("\nПервое число ")
    if first_number == 'q':
        break
    second_number = input("Второе число ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Вы ввели не число ")
    else:
        print(answer)
