import unittest
from parameterized import parameterized
from praktikum.ingredient import Ingredient


class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.ingredient = Ingredient('соус', 'Томатный', 50.0)

    def test_get_price(self):
        self.assertEqual(self.ingredient.get_price(), 50.0)

    def test_get_name(self):
        self.assertEqual(self.ingredient.get_name(), 'Томатный')

    def test_get_type(self):
        self.assertEqual(self.ingredient.get_type(), 'соус')


class TestIngredientParameterized(unittest.TestCase):
    @parameterized.expand([
        ('соус', 'Томатный', 50.0),
        ('начинка', 'Сыр', 40.0),
        ('соус', 'Чесночный', 30.0),
    ])
    def test_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        self.assertEqual(ingredient.get_type(), type)
        self.assertEqual(ingredient.get_name(), name)
        self.assertEqual(ingredient.get_price(), price)
