class User():

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		print(
			f"Имя Фамилия {self.first_name.title()} {self.last_name.title()} ")

	def greet_user(self):
		print(f"Привет {self.first_name.title()} {self.last_name.title()} ")

	def increment_login_attempts(self):
		self.login_attempts += 5
		print(f"Залогинился {self.login_attempts} раз")

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(f"Залогинился {self.login_attempts} раз")


users = User('ivan', 'ivanov')
users.describe_user()
users.greet_user()
users.increment_login_attempts()
users.reset_login_attempts()
