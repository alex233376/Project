class Car():
	"""Простая модель автомобиля."""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Выводит пробег машины в милях."""
		print(f"Пробег этой машины {self.odometer_reading} ")

	def update_odometer(self, mileage):
		"""
		Устанавливает на одометре заданное значение.
		При попытке обратной подкрутки изменение отклоняется.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Вы не можете скрутить одометр ")

	def increment_odometer(self, miles):
		"""Увеличивает показания одометра с заданным приращением."""
		self.odometer_reading += miles


class Battery():
	"""Простая модель аккумулятора электромобиля."""

	def __init__(self, battery_size=75):
		"""Инициализирует атрибуты аккумулятора."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора."""
		print(f'Эта машина имеет батарею {self.battery_size} кВч')

	def upgrade_battery(self):
		if self.battery_size != 100:
			self.battery_size = 100
			print(f'Теперь есть батарея на {self.battery_size} кВч ')

	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"Эта машина может ездить {range} миль на полном заряде ")


class ElectricCar(Car):
	"""аспекты автомобиля, специфичные для электромобилей."""

	def __init__(self, make, model, year):
		"""
		Инициализировать атрибуты родительского класса.
		Затем инициализируйте атрибуты, характерные для электромобиля.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def describe_battery(self):
		"""Выводит размер батареи."""
		print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
