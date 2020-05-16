def make_album(name, album):
	full_info = (f"{name} {album}")
	return full_info


while True:
	executor = input("Иполнитель ")
	if executor == 'q':
		break
	name_a = input("\nНазвание альбома ")
	if name_a == 'q':
		break
	music = make_album(executor, name_a)
	print(f'Результат {music}')
