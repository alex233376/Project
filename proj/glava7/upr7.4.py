pizza = input('Какую пицу вы хотите ')
pizza += ("\nНабирите 'quit' для выхода ")
message = ""
while message != 'quit':
    message = input(pizza)
    if message != 'quit':
        print(message)
