"""Набор классов для представления электромобилей."""

from car import Car


class Battery():
    """Простая попытка моделировать аккумулятор для электромобиля."""

    def __init__(self, battery_size=75):
        """
Инициализируйте атрибуты батареи."""
        self.battery_size = battery_size

    def describe_battery(self):
        """описанием размера батареи."""
        print(f"Эта батарея имеет заряд {self.battery_size}-kWh.")

    def get_range(self):
        """Расстояние которое обеспечит эта батарея."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Эта машина сможет проехать {range} миль на полной зарядке.")


class ElectricCar(Car):
    """Особенности модели автомобиля, специфичные для электромобилей."""

    def __init__(self, make, model, year):
        """
        Инициализировать атрибуты родительского класса.
        Затем инициализируйте атрибуты, характерные для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
