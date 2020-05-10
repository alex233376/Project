def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} 's name is {pet_name.title()}.")


# Пес по имени Вилли.
describe_pet('willie')
describe_pet(pet_name='wilie')

# Хомяк по имени Гарри.
describe_pet('hamster', 'harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
