prompt = input("\nСкажи мне что-нибудь, и я повторю это тебе: ")
prompt += "\nВведите 'quit' для выхода из программы:"
active = True  # Задали флаг на активацию
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
