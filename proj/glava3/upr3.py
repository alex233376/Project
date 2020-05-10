the_guests = ['petro', 'valera', 'alex']
print(f'{the_guests[0].title()} приходи на обед')
print(f'{the_guests[1].title()} приходи на обед')
print(f'{the_guests[2].title()} приходи на обед')

print(f'\n{the_guests[2].title()} придти не сможет')
the_guests.remove('valera')  # Удалил пользователя
the_guests.insert(2, 'vasia')  # Вставил нового
print(f'\n{the_guests[0].title()} приходи на обед')
print(f'{the_guests[1].title()} приходи на обед')
print(f'{the_guests[2].title()} приходи на обед')
