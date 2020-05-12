class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """ Модель ресторана название кухня """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Описание ресторана"""
        print(
            f'Ресторан {self.restaurant_name} с кухней {self.cuisine_type}')

    def set_number_served(self):
        """Количество поситителей"""
        print(f"Обслуженно {self.number_served}")

    def increment_number_served(self, visitors):
        """Увеличивает количество поситителей"""
        self.number_served += visitors


restaurant = Restaurant('Karel', 'karl')
restaurant.describe_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served(20)
restaurant.set_number_served()
