from unittest.mock import Mock

import pytest


class TestBurger:
    def test_burger_set_bun(self, burger):
        bun_mock = Mock()
        burger.set_buns(bun_mock)

        assert burger.bun == bun_mock

    def test_burger_add_ingredient(self, burger):
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)

        assert ingredient_mock in burger.ingredients

    def test_burger_remove_ingredient(self, burger):
        ingredient_mock = Mock()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)

        assert ingredient_mock not in burger.ingredients


    @pytest.mark.parametrize("index, new_index", [
        (0, 1),   
        (0, 0),  
    ])
    def test_burger_move_ingredient(self, index, new_index, burger):
        ingredient_mock1 = Mock()
        ingredient_mock2 = Mock()
        burger.add_ingredient(ingredient_mock1)
        burger.add_ingredient(ingredient_mock2)
        burger.move_ingredient(index, new_index)

        assert burger.ingredients[new_index] == ingredient_mock1

    @pytest.mark.parametrize("bun_price, ingredient_price, expected_price", [
        (10, 5, 25),  
        (20, 10, 50)
    ])
    def test_burger_get_price(self, bun_price, ingredient_price, expected_price, burger):
        bun_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        burger.set_buns(bun_mock)

        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = ingredient_price
        burger.add_ingredient(ingredient_mock)

        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, burger):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "Булка"
        bun_mock.get_price.return_value = 0
        burger.set_buns(bun_mock)

        ingredient_mock = Mock()
        ingredient_mock.get_type.return_value = "Начинка"
        ingredient_mock.get_name.return_value = "Сыр"
        ingredient_mock.get_price.return_value = 0
        burger.add_ingredient(ingredient_mock)

        expected_receipt = (
            "(==== Булка ====)\n"
            "= начинка Сыр =\n"
            "(==== Булка ====)\n"
            "\n"
            "Price: 0"
        )

        assert burger.get_receipt() == expected_receipt