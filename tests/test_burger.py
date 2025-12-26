import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestBurger:
    def test_set_bun(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Name_bun'
        mock_bun.get_price.return_value = 9.0
        burger.set_buns(mock_bun)
        assert burger.bun.get_price() == 9.0
        assert burger.bun.get_name() == 'Name_bun'
        
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_bun'
        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 9.0
        assert burger.ingredients[0].get_name() == 'Name_bun'
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_bun'
        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []
        
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Name_bun'
        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.ingredients[0].get_price() == 9.0
        burger.ingredients[0].get_name() == 'Name_bun'
        burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] is mock_ingredient

    @pytest.mark.parametrize(
    "bun_price, ingredients, expected_price",
    [
        (9.0, [], 18.0),
        (10.0, [(5.0, INGREDIENT_TYPE_FILLING)], 25.0),
        (8.0, [(3.0, INGREDIENT_TYPE_FILLING), (4.0, INGREDIENT_TYPE_FILLING)], 23.0),
        (7.5, [(0.0, INGREDIENT_TYPE_FILLING)], 15.0),
    ]
    )
    def test_get_price(self, bun_price, ingredients, expected_price):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Name_bun'
        mock_bun.get_price.return_value = bun_price
        burger.bun = mock_bun

        for price, type_ in ingredients:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            mock_ingredient.get_type.return_value = type_
            burger.add_ingredient(mock_ingredient)

        total_price = burger.get_price()
        assert total_price == expected_price

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Classic Bun'
        burger.bun = mock_bun
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_name.return_value = 'Cutlet'
        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_name.return_value = 'Hot Sauce'
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.get_price = Mock(return_value=155.00)
        receipt = burger.get_receipt()
        expected = (
            '(==== Classic Bun ====)\n'
            '= filling Cutlet =\n'
            '= sauce Hot Sauce =\n'
            '(==== Classic Bun ====)\n'
            '\n'
            'Price: 155.0'
        )
        assert receipt == expected