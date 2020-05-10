# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Вывод первых 5 пришельцев:
for alien in aliens[0:5]:
    print(alien)
print("...")
