import unittest
from unittest.mock import MagicMock
from parameterized import parameterized
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger(unittest.TestCase):
    def setUp(self):
        self.mock_bun = MagicMock(spec=Bun)
        self.mock_ingredient = MagicMock(spec=Ingredient)
        self.burger = Burger()

    def test_set_buns(self):
        self.mock_bun.get_name.return_value = 'Булочка'
        self.mock_bun.get_price.return_value = 50.0
        self.burger.set_buns(self.mock_bun)
        self.assertIs(self.burger.bun, self.mock_bun)

    @parameterized.expand([
        (0, 1),
        (1, 0),
        (2, 3),
    ])
    def test_move_ingredient(self, index, new_index):
        self.burger.ingredients = [MagicMock(spec=Ingredient) for _ in range(4)]
        moved_ingredient = self.burger.ingredients[index]
        self.burger.move_ingredient(index, new_index)
        self.assertEqual(self.burger.ingredients[new_index], moved_ingredient)

    def test_add_ingredient(self):
        self.mock_ingredient.get_name.return_value = 'Сыр'
        self.mock_ingredient.get_price.return_value = 20.0
        self.burger.add_ingredient(self.mock_ingredient)
        self.assertIn(self.mock_ingredient, self.burger.ingredients)

    def test_remove_ingredient(self):
        self.burger.ingredients = [MagicMock(spec=Ingredient) for _ in range(3)]
        remove_index = 1
        ingredient_to_remove = self.burger.ingredients[remove_index]
        self.burger.remove_ingredient(remove_index)
        self.assertNotIn(ingredient_to_remove, self.burger.ingredients)

    def test_get_price(self):
        self.mock_bun.get_price.return_value = 50.0
        self.mock_ingredient.get_price.return_value = 20.0
        self.burger.set_buns(self.mock_bun)
        self.burger.ingredients = [self.mock_ingredient, self.mock_ingredient]
        expected_price = 50.0 * 2 + 20.0 * 2  # Цена булочек и двух ингредиентов
        self.assertAlmostEqual(self.burger.get_price(), expected_price)

    def test_get_receipt(self):
        self.mock_bun.get_name.return_value = 'Булочка'
        self.mock_bun.get_price.return_value = 50.0
        self.mock_ingredient.get_type.return_value = 'Начинка'
        self.mock_ingredient.get_name.return_value = 'Сыр'
        self.mock_ingredient.get_price.return_value = 20.0
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient)
        expected_receipt = (
            '(==== Булочка ====)\n'
            '= начинка Сыр =\n'
            '(==== Булочка ====)\n\n'
            'Price: 120.0'
        )
        self.assertEqual(self.burger.get_receipt(), expected_receipt)
