pets = [
    {'Собака': 'бобик', 'Хозяин': 'иван'},
    {'Кошка': 'мурка', 'Хозяин': 'вася'}
]
for pet in pets:
    for k, v, in pet.items():
        print(f'{k} {v.title()}')
