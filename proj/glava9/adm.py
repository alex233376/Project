class User():

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(
			f"Имя Фамилия {self.first_name.title()} {self.last_name.title()} ")

	def greet_user(self):
		print(f"Привет {self.first_name.title()} {self.last_name.title()} ")


class Privileges():
	def __init__(self, privileges=['разрешено удалять пользователей',
	                               'разрешено банить пользователей']):
		self.privileges = privileges

	def show_privileges(self):
		print(f"Админ {self.privileges}")


class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()
