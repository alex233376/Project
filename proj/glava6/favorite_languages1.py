favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, lang, in favorite_languages.items():  # Перебор ключ значение
    print(f"{name.title()} любимый язык {lang.title()}\n")
# for name in favorite_languages:  # Перебор всех ключей в словаре
    # print(name.title())
