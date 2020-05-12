class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

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


# создается экземпляр my_used_car
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
# инициализируем показания одометра значением 23 500
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
# увеличиваем показания одометра на 100 миль, пройденные
# с момента покупки
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
