import unittest
from city_functions import str_city


class NamesTestCase(unittest.TestCase):
    """Тесты для 'city_function.py'."""

    def test_city_country(self):
        country = str_city('santiago', 'chile')
        self.assertEqual(country, 'Santiago Chile')

    def test_city_country_population(self):
        country = str_city('santiago', 'chile', 'population=5000000')
        self.assertEqual(country, 'Santiago Chile Population=5000000')


if __name__ == '__main__':
    unittest.main()
