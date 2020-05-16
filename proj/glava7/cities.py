prompt = input("\nПожалуйста, введите название города, который вы посетили ")
prompt += "\nВведите 'quit' для выхода из программы:"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"Я хотел бы поехать в {city.title()}!")
