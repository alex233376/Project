class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		""" Модель ресторана название кухня """
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Описание ресторана"""
		print(
			f'Ресторан {self.restaurant_name} с кухней {self.cuisine_type}')

	def open_restaurant(self):
		"""Ресторан открыт"""
		print(f"{self.restaurant_name} Открыт ")


restaurant = Restaurant('Karel', 'karl')
restaurant.describe_restaurant()
restaurant.open_restaurant()
