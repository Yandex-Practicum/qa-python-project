import unittest
from unittest.mock import Mock

from ..bun import Bun
from ..ingredient import Ingredient
from ..burger import Burger


class TestBurger(unittest.TestCase):
    def setUp(self):
        self.burger = Burger()

    def test_set_buns(self):
        bun = Mock(spec=Bun)
        self.burger.set_buns(bun)
        self.assertEqual(self.burger.bun, bun)

    def test_add_ingredient(self):
        ingredient = Mock(spec=Ingredient)
        self.burger.add_ingredient(ingredient)
        self.assertIn(ingredient, self.burger.ingredients)

    def test_remove_ingredient(self):
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        self.burger.ingredients = [ingredient1, ingredient2]
        self.burger.remove_ingredient(0)
        self.assertNotIn(ingredient1, self.burger.ingredients)

    def test_move_ingredient(self):
        ingredient1 = Mock(spec=Ingredient)
        ingredient2 = Mock(spec=Ingredient)
        self.burger.ingredients = [ingredient1, ingredient2]
        self.burger.move_ingredient(0, 1)
        self.assertEqual(self.burger.ingredients, [ingredient2, ingredient1])

    def test_get_price(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 2.0
        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 1.0
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 1.5
        self.burger.set_buns(bun)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        exp_price = ((2 * bun.get_price.return_value) +
                     ingredient1.get_price.return_value + ingredient2.get_price.return_value)
        self.assertEqual(self.burger.get_price(), exp_price)

    def test_get_receipt(self):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = 'Brioche'
        bun.get_price.return_value = 2.0
        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_type.return_value = 'Sauce'
        ingredient1.get_name.return_value = 'Ketchup'
        ingredient1.get_price.return_value = 1.0
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_type.return_value = 'Meat'
        ingredient2.get_name.return_value = 'Beef'
        ingredient2.get_price.return_value = 1.5
        self.burger.set_buns(bun)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        self.assertEqual(self.burger.get_receipt(),
                         '(==== Brioche ====)\n= sauce Ketchup =\n= meat Beef =\n(==== Brioche ====)\n\nPrice: 6.5')
