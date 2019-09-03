class User():
    """Модель юзера"""

    def __init__(self, first_name, last_name):
        """Инициализирует атрибуты first_name, last_name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name.title() + "Имя юзера ")
        print(self.last_name.title() + "Фамилия юзера ")


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ('собщения', 'удалять', 'банить')

    def show_privileges(self):
        print("Привилегии" + str(self.privileges))


Admin = Admin('Petro ', 'Dust ')
print(Admin.describe_user())
Admin.show_privileges()
