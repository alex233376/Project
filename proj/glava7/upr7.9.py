sandwich_orders = ['shawarma', 'pastrami', 'kaskrut', 'fajitos', 'pastrami']
print('Pastrami больше нет')
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

for sok in sandwich_orders:
	print(f"Есть только это {sok}")
