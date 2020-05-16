sandwich_orders = ['shawarma', 'kaskrut', 'fajitos']
finished_sandwiches = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f'Я сделал твой бутерброд с тунцом {sandwich}')
	finished_sandwiches.append(sandwich)
for sok in finished_sandwiches:
	print(f"Готовые бутеры {sok}")
