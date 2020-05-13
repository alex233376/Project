"""Класс, который можно использовать для представления автомобиля."""


class Car:
    """
Простая попытка представить автомобиль."""

    def __init__(self, make, model, year):
        """Инициализировать атрибуты для описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Вернуть аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Распечатать отчет с указанием пробега автомобиля."""
        print(f"Этот автомобиль проехал {self.odometer_reading} миль.")

    def update_odometer(self, mileage):
        """
        Установите показания одометра на заданное значение
        Отклонить изменение, если оно пытается откатить одометр.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить одометр !")

    def increment_odometer(self, miles):
        """Добавьте данную сумму к показаниям одометра."""
        self.odometer_reading += miles


class Battery:
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
