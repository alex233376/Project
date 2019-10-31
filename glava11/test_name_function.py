import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):#создается класс NamesTestCase, который содержит серию модульных тестов для get_formatted_name()
    """Тесты для 'name_function.py'."""
    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')# Вызов означает: «Сравни значение formatted_name со строкой 'Janis Joplin'.
        #Если они равны, как и ожидалось, — хорошо.Но если они не равны, сообщи мне
    def test_first_last_middle_name(self):
        """Работают ли такие имена, как 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()# приказывает Python выполнить тесты из этого файла.