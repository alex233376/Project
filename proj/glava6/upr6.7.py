people = [
    {
     'firstname': 'vasia',
     'lastname': 'petrov',
     'age': 30,
     'city': 'bamba'
    },
    {
     'first_name': 'ivan',
     'lastname': 'peps',
     'age': 32,
     'city': 'piter'
    },
    {
     'firstname': 'nata',
     'lastname': 'rez',
     'age': 56,
     'city': 'ptz'
    }
]
#  Перебираем словари в списке
for user in people:
    for k, v in user.items():  # Перебираем ключ значение
        print(f"{k}: {v}\n")
