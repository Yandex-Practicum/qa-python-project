from praktikum.burger import Burger
from unittest.mock import Mock

class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredients(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredients(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.ingredients[0] == ingredient_1 and burger.ingredients[1] == ingredient_2
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_2 and burger.ingredients[1] == ingredient_1

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        price = 0
        burger.set_buns(mock_bun)
        price += mock_bun.get_price() * 2
        burger.add_ingredient(mock_ingredient)
        price += mock_ingredient.get_price()
        assert price == burger.get_price()

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        price = 0
        burger.set_buns(mock_bun)
        price += mock_bun.get_price() * 2
        burger.add_ingredient(mock_ingredient)
        price += mock_ingredient.get_price()
        receipt = burger.get_receipt()
        format_receipt = "\n".join([
            f'(==== {mock_bun.get_name()} ====)',
            f'= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =',
            f'(==== {mock_bun.get_name()} ====)\n',
            f'Price: {price}',
        ])
        assert receipt == format_receipt












