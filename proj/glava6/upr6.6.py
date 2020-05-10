favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for k, v, in favorite_languages.items():
    print(f'{k.title()} {v.title()} спасибо что прошли опрос\n')
# Если нет в списке просим пройти опрос
if 'erin' not in favorite_languages.keys():
    print('Erin пройди опрос ')
