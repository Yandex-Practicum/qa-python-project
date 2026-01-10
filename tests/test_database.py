import unittest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_init(self):
        self.assertEqual(len(self.db.buns), 3)
        self.assertEqual(len(self.db.ingredients), 6)

    def test_available_buns(self):
        mock_buns = [Bun("mock bun", 50) for _ in range(3)]
        self.db.buns = mock_buns

        buns = self.db.available_buns()
        self.assertEqual(buns, mock_buns)

    def test_available_ingredients(self):
        mock_ingredients = [Ingredient(INGREDIENT_TYPE_SAUCE, "mock sauce", 50) for _ in range(3)] + \
                           [Ingredient(INGREDIENT_TYPE_FILLING, "mock filling", 75) for _ in range(3)]
        self.db.ingredients = mock_ingredients

        ingredients = self.db.available_ingredients()
        self.assertEqual(ingredients, mock_ingredients)


if __name__ == '__main__':
    unittest.main()
