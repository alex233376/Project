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
