favorite_places = {
	'nata': ['les', 'ozero', 'dom'],
	'petro': ['reka', 'voda', 'pole'],
	'ivan': ['gorod', 'club', 'rabota']
}
#  Перебираем и выводим ключи
for name, mesto in favorite_places.items():
	print(f'\n{name.title()}')
	#  Перебираем и выводим места
	for m in mesto:
		print(m.title())
