prompt = input("\nСкажи мне что-нибудь, и я повторю это тебе: ")
prompt += "\nВведите 'quit' для выхода из программы:"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':  # Убираем quit из вывода
        print(message)
