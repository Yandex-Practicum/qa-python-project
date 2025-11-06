import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec= Ingredient)
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec= Ingredient)
        burger.ingredients = [mock_ingredient]

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredients(self):
        burger = Burger()
        mock_ingredient_1 = Mock(spec= Ingredient)
        mock_ingredient_2 = Mock(spec= Ingredient)
        burger.ingredients = [mock_ingredient_1, mock_ingredient_2]

        burger.move_ingredient(0, 1)

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected",
        [
            (100, [], 200),
            (50, [10, 20], 130),
            (0, [10, 15], 25),
        ]
    )
    def test_get_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        result = burger.get_price()
        assert result  == expected

    @pytest.mark.parametrize(
        "bun_name,ingredient_data,expected_lines",
        [
            (
                "Флюоресцентная булка",
                [("SAUCE", "Соус традиционный")],
                [
                    "(==== Флюоресцентная булка ====)",
                    "= sauce Соус традиционный =",
                    "(==== Флюоресцентная булка ====)",
                    "Price: 2300"
                ]
            ),
            (
                "Кратерная булка",
                [("FILLING", "Биокотлета"), ("SAUCE", "Фирменный")],
                [
                    "(==== Кратерная булка ====)",
                    "= filling Биокотлета =",
                    "= sauce Фирменный =",
                    "(==== Кратерная булка ====)",
                    "Price: 2600"
                ]
            )
        ]
    )
    def test_get_receipt(self, bun_name, ingredient_data, expected_lines):
        burger = Burger()
        
        # Мок булки
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 1000
        burger.set_buns(mock_bun)
        
        # Моки ингредиентов
        for ingredient_type, ingredient_name in ingredient_data:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_name.return_value = ingredient_name
            mock_ingredient.get_price.return_value = 300
            burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        assert receipt.split('\n') == expected_lines

    def test_get_receipt_no_bun_raises_error(self):
        burger = Burger()
        assert burger.bun is None, "Бургер должен быть создан без булки"

        with pytest.raises(ValueError, match="Cannot generate receipt: bun is not set") as exc_info:
            burger.get_receipt()
        assert exc_info.type is ValueError