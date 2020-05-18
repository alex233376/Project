from name_function import get_formatted_name

print("Введите 'q' в любое время, чтобы выйти")
while True:
    first = input("\nВведите своё имя ")
    if first == 'q':
        break

    last = input("Введите свою фамилию ")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tАккуратно отформатированное имя: {formatted_name}.")
