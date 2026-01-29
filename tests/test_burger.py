
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        assert mock_ingredient1 in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient1):
        burger.add_ingredient(mock_ingredient1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_ingredient1, mock_ingredient2):
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient1]

    @pytest.mark.parametrize("bun_price, ingredients_price, expected", [
        (100, [], 200),
        (50, [10, 20], 130),
        (0, [0, 0, 0], 0)
    ])
    def test_get_price(self, burger, mock_bun, bun_price, ingredients_price, expected):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredients_price:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected

    def test_get_receipt(self, burger, mock_bun, mock_ingredient1, mock_ingredient2):
        mock_bun.get_name.return_value = 'black bun'
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = 'hot sauce'
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = 'cutlet'

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'  # Обратите внимание: тип в нижнем регистре
            '= filling cutlet =\n'   # Обратите внимание: тип в нижнем регистре
            '(==== black bun ====)\n'
            '\n'
            'Price: 450'
        )

        assert burger.get_receipt() == expected_receipt
