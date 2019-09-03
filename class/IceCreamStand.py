class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)


class IceCreamStand(Restaurant):
    """Выводит список мороженного"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['mal', 'klub', 'zer']

    def describe_flavors(self):
        """Список мороженного"""
        print("Мороженное " + str(self.flavors))


icecream = IceCreamStand('ptz', 'figu')
print(icecream.describe_restaurant())
icecream.describe_flavors()
