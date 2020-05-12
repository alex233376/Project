class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f'{self.name} is now sitting ')

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name} rolled over!")


my_dog = Dog('wille', 6)
your_dog = Dog('loci', 4)

print(f"Мою собаку зовут {my_dog.name} ")
print(f"Моей собаке {my_dog.age} лет ")
my_dog.sit()

print(f"\nМою собаку зовут {your_dog.name} ")
print(f"\nМоей собаке {your_dog.age} лет ")
your_dog.sit()
