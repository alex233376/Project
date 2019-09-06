class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('Имя: ' + self.first_name)
        print('Фамилия: ' + self.last_name)

    # def great_user(self):
        #full_name = self.first_name + ' ' + self.last_name
        #print('Привет, ' + full_name + '!')


class Privileges:
    def __init__(self, privileges=''):
        self.privileges = privileges

    def show_privileges(self):
        self.privileges = [
            'Отправлять сообщения',
            'Удалять сообщения',
            'Банить юзеров'
        ]#список привелегий
        for priveleg in self.privileges:
            print(priveleg)


class Admin(User):
    privileges = Privileges()#это атрибут класса

    def __init___(self, first_name, last_name):
        super().__init__(first_name, last_name)


admin = Admin('Петро', 'Потапов')

admin.describe_user()
admin.privileges.show_privileges()
