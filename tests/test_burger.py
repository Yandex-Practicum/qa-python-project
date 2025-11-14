import unittest
from praktikum.praktikum import Burger
from praktikum.praktikum import Bun
from praktikum.praktikum import Ingredient

class TestBurger(unittest.TestCase):

    def setUp(self):
        self.burger = Burger()
        self.bun = Bun('Sesame', 20.0)
        self.ingredient1 = Ingredient('Vegetable', 'Lettuce', 10.0)
        self.ingredient2 = Ingredient('Vegetable', 'Tomato', 5.0)

    def test_set_buns(self):
        self.burger.set_buns(self.bun)
        self.assertEqual(self.burger.bun, self.bun)

    def test_add_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.assertIn(self.ingredient1, self.burger.ingredients)

    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.remove_ingredient(0)
        self.assertNotIn(self.ingredient1, self.burger.ingredients)

    def test_move_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.move_ingredient(0, 1)
        self.assertEqual(self.burger.ingredients[0], self.ingredient2)

    def test_get_price(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        expected_price = (20.0 * 2) + 10.0
        self.assertEqual(self.burger.get_price(), expected_price)

    def test_get_receipt(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient1)
        receipt = self.burger.get_receipt()
        expected_receipt = "(==== Sesame ====)\n= vegetable Lettuce =\n(==== Sesame ====)\n\nPrice: 50.0"
        self.assertEqual(receipt, expected_receipt)

if __name__ == '__main__':
    unittest.main()
