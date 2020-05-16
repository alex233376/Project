favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
#  Перебираем имена
for name, languages in favorite_languages.items():
	if len(languages):  # Выводим количество языков
		print(f"\n{name.title()} любимые языки {len(languages)}")

	#  Перебираем языки
	for language in (languages):
		print(f"\t{language.title()}")
