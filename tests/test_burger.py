from burger import Burger
from unittest.mock import Mock

class TestBurger:

    def setup_method(self):
        self.burger = Burger()
        self.mock_bun = Mock()
        self.mock_ingredient_1 = Mock()
        self.mock_ingredient_2 = Mock()

    def test_set_buns_is_success(self):
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun

    def test_add_ingredients_is_success(self):
        self.burger.add_ingredient(self.mock_ingredient_1)
        self.burger.add_ingredient(self.mock_ingredient_2)
        assert self.burger.ingredients == [self.mock_ingredient_1, self.mock_ingredient_2]

    def test_remove_ingredient_is_success(self):
        self.burger.add_ingredient(self.mock_ingredient_1)
        self.burger.add_ingredient(self.mock_ingredient_2)
        self.burger.remove_ingredient(0)
        assert self.burger.ingredients[0] == self.mock_ingredient_2

    def test_move_ingredient_is_success(self):
        self.burger.add_ingredient(self.mock_ingredient_1)
        self.burger.add_ingredient(self.mock_ingredient_2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients == [self.mock_ingredient_2, self.mock_ingredient_1]

    def test_get_price_with_ingredients(self):
        self.mock_bun.get_price.return_value = 2.0
        self.mock_ingredient_1.get_price.return_value = 4.0
        self.mock_ingredient_2.get_price.return_value = 3.0

        self.burger.bun = self.mock_bun
        self.burger.ingredients = [self.mock_ingredient_1, self.mock_ingredient_2]

        expected_price = (2.0 * 2) + 4.0 + 3.0
        assert self.burger.get_price() == expected_price

    def test_get_receipt(self):
        self.mock_bun.get_price.return_value = 2.0
        self.mock_ingredient_1.get_price.return_value = 4.0
        self.mock_ingredient_2.get_price.return_value = 3.0

        self.mock_bun.get_name.return_value = "black bun"
        self.mock_ingredient_1.get_name.return_value = "sour cream"
        self.mock_ingredient_2.get_name.return_value = "sausage"
        self.mock_ingredient_1.get_type.return_value = "sauce"
        self.mock_ingredient_2.get_type.return_value = "filling"

        self.burger.bun = self.mock_bun
        self.burger.ingredients = [self.mock_ingredient_1, self.mock_ingredient_2]

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce sour cream =\n"
            "= filling sausage =\n"
            "(==== black bun ====)\n"
            "\n"
            f"Price: {self.burger.get_price()}"
        )
        assert self.burger.get_receipt() == expected_receipt
