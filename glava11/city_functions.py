"""Коллекция функций для работы с городами"""
def city_country(city, country, population = ''):
    """Вернуть строку, представляющую пару город-страна и население."""
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string