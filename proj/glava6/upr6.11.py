cities = {
    'ptz': {
        'country': 'karelia',
        'population': '500',
        'fact': 'pizdos'
    },
    'msk': {
        'country': 'ru',
        'population': '100000',
        'fact': 'herovo'
    }
}
for gorod, info in cities.items():
    print(f"Город {gorod.title()}")
    full_info = f"Место {info['country']} население {info['population']}"
    facts = info['fact']
    print(full_info)
    print(f"Факты {facts}")
