import unittest
from praktikum.database import Database
from praktikum.database import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    def test_buns_initialization(self):
        buns = self.database.available_buns()
        self.assertEqual(len(buns), 3)

    def test_ingredients_initialization(self):
        ingredients = self.database.available_ingredients()
        self.assertEqual(len(ingredients), 6)  # Проверяем, что есть шесть ингредиентов

    def test_ingredient_types(self):
        ingredients = self.database.available_ingredients()
        sauce_count = sum(1 for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE)
        filling_count = sum(1 for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING)
        self.assertEqual(sauce_count, 3)  # Проверяем, что три соуса
        self.assertEqual(filling_count, 3)  # Проверяем, что три начинки

if __name__ == '__main__':
    unittest.main()
