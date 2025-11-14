import unittest
from praktikum.praktikum import Ingredient

class TestIngredient(unittest.TestCase):

    def setUp(self):
        self.ingredient = Ingredient('Vegetable', 'Lettuce', 10.0)

    def test_ingredient_attributes(self):
        self.assertEqual(self.ingredient.type, 'Vegetable')
        self.assertEqual(self.ingredient.name, 'Lettuce')
        self.assertEqual(self.ingredient.price, 10.0)

    def test_get_price(self):
        self.assertEqual(self.ingredient.get_price(), 10.0)

    def test_get_name(self):
        self.assertEqual(self.ingredient.get_name(), 'Lettuce')

    def test_get_type(self):
        self.assertEqual(self.ingredient.get_type(), 'Vegetable')

if __name__ == '__main__':
    unittest.main()
