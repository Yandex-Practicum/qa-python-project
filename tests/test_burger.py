import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from data.test_data import BurgerTestData


class TestBurger:
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_bun(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)

        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_by_index(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(0)

        assert burger.ingredients == [ing2]

    def test_move_ingredient_from_to_index(self):
        burger = Burger()
        ing1 = Mock(spec=Ingredient)
        ing2 = Mock(spec=Ingredient)
        ing3 = Mock(spec=Ingredient)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    @pytest.mark.parametrize('bun_price, ingredients_price, expected_price', BurgerTestData.BUN_PR)
    def test_get_price_burger(self, bun_price, ingredients_price, expected_price):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredients_price:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_price

    @pytest.mark.parametrize('bun_name, bun_price, ingredients_data, expected_receipt', BurgerTestData.RECEIPT_DATA)
    def test_get_receipt(self, bun_name, bun_price, ingredients_data, expected_receipt):
        burger = Burger()

        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = bun_price
        bun_mock.get_name.return_value = bun_name
        burger.set_buns(bun_mock)

        for ing_data in ingredients_data:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_type.return_value = ing_data[0]
            mock_ing.get_name.return_value = ing_data[1]
            mock_ing.get_price.return_value = ing_data[2]
            burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        assert receipt == expected_receipt
