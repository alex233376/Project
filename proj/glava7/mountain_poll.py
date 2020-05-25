responses = {}
# Установка флага продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nКак тебя зовут? ")
    response = input("На какую гору вы хотели бы подняться ")

    # Ответ сохраняется в словаре:
    responses[name] = response

    # Проверка продолжения опроса.
    repeat = input("Продолжать опрос? (да/нет) ")
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты.
print("\n---Результат---")
for name, response in responses.items():
    print(f"{name}  хотел бы подняться {response}")
