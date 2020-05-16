# Начинаем с двух списков: пользователей для проверки
#  и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#  пользователи. Каждый пользователь, прошедший проверку,
# Проверяем каждого пользователя, пока остаются непроверенные
#  перемещается в список проверенных.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print(f"Верефицированный юзер: {current_user.title()}")
	confirmed_users.append(current_user)

# Вывод всех проверенных пользователей.
print(f"\nЭто проверенные пользователи")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
