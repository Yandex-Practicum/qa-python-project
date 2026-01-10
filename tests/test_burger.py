# Burger Class tests
from data import RECEIPT_TEMPLATE
from utils import set_burger_ingrs, expected_price


class TestBurger:

    def test_burger_init_default_values_check(self, test_burger):
        assert test_burger.bun is None
        assert len(test_burger.ingredients) == 0

    def test_set_buns_is_correct(self, test_burger, mock_bun):
        test_burger.set_buns(mock_bun)
        assert test_burger.bun == mock_bun

    def test_add_ingredient_is_correct(self, test_burger, mock_ingredient):
        test_burger.add_ingredient(mock_ingredient)
        assert len(test_burger.ingredients) == 1
        assert test_burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_is_correct(self, test_burger, mock_ingredient):
        test_burger = set_burger_ingrs(test_burger, mock_ingredient, 'ingredient')
        test_burger.remove_ingredient(0)
        assert len(test_burger.ingredients) == 1

    def test_move_ingredient_is_correct(self, test_burger, mock_ingredient):
        test_burger = set_burger_ingrs(test_burger, 'ingredient', mock_ingredient)
        test_burger.move_ingredient(1, 0)
        assert test_burger.ingredients[1] == 'ingredient'

    def test_get_price_returns_correct_price(self, test_burger, mock_bun, mock_ingredient):
        test_burger = set_burger_ingrs(test_burger, mock_ingredient, bun=mock_bun)
        assert (test_burger.get_price() == expected_price(mock_ingredient, bun=mock_bun))

    def test_get_receipt_returns_correct_receipt(self, test_burger, mock_bun, mock_ingredient):
        test_burger = set_burger_ingrs(test_burger, mock_ingredient, bun=mock_bun)
        data = {
            'bun_name': mock_bun.get_name(),
            'ingredient_type': str(mock_ingredient.get_type()).lower(),
            'ingredient_name': mock_ingredient.get_name(),
            'price': expected_price(mock_ingredient, bun=mock_bun)
        }
        assert test_burger.get_receipt() == RECEIPT_TEMPLATE.format(**data)
