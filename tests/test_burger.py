from unittest.mock import patch

from helper import get_random_bun, get_random_ingredient
from praktikum import Database, main


class TestBurger:
    dbs = Database()

    def test_set_bun(self, burger):
        bun = get_random_bun(self.dbs)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_set_ingredient(self, burger):
        ingredient = get_random_ingredient(self.dbs)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, burger):
        ingredient = get_random_ingredient(self.dbs)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients and len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        first_ingredient = get_random_ingredient(self.dbs)
        second_ingredient = get_random_ingredient(self.dbs)
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == first_ingredient

    @patch('bun.Bun.get_price')
    @patch('ingredient.Ingredient.get_price')
    def test_get_price(self, mock_bun_get_price, mock_ingredient_get_price, burger):
        bun = get_random_bun(self.dbs)
        burger.set_buns(bun)
        mock_bun_get_price.return_value = 100
        mock_ingredient_get_price.return_value = 100
        ingredient = get_random_ingredient(self.dbs)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 300

    @patch('burger.Burger.get_price')
    @patch('bun.Bun.get_name')
    def test_get_receipt(self, mock_bun_get_name, mock_burger_get_price, burger):
        bun = get_random_bun(self.dbs)
        burger.set_buns(bun)
        price_val = 100
        name_val = 'bulka'
        mock_burger_get_price.return_value = price_val
        mock_bun_get_name.return_value = name_val
        assert f'(==== {name_val} ====)\n(==== {name_val} ====)\n\nPrice: {price_val}' == burger.get_receipt()

    def test_main(self):
        assert not main()
