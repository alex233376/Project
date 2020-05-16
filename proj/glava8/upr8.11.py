def show_messagaes(messages, comp_messages):
	"""Перемещаем все сообщения в comp_messages """
	while messages:
		v_messages = messages.pop()
		print(f"Printing {v_messages}")
		comp_messages.append(v_messages)


def send_messages(comp_messages):
	"""Выводим все сообщения """
	print(f"Accepted ")
	for comp_message in comp_messages:
		print(comp_message)


messages = ['alex hello', 'petro hello']
un_messages = []
# Передаём копию списка messages с помощью messages[:]
show_messagaes(messages[:], un_messages)
send_messages(un_messages)
