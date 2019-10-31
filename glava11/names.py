from name_function import get_formatted_name

print("Введите 'q' чтобы выйти ")
while True:
    first = input("\nПожалуйста введите ваше имя: ")
    if first == 'q':
        break
    last = input("Введите вашу фамилию ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tОтформатированное имя " + formatted_name)