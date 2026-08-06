import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.remove_ingredient(0)

        assert mock_ingredient_1 not in burger.ingredients
        assert mock_ingredient_2 in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    @pytest.mark.parametrize(
        "bun_price, ingredient_1_price, ingredient_2_price, expected_price",
        [
            (100.0, 50.0, 30.0, 280.0),
            (0.0, 0.0, 0.0, 0.0),
            (150.5, 99.5, 0.0, 400.5),
        ]
    )
    def test_get_price(self, bun_price, ingredient_1_price, ingredient_2_price, expected_price):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = ingredient_1_price

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = ingredient_2_price

        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "dinosaur"
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_price.return_value = 200.0
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert "black bun" in receipt
        assert "dinosaur" in receipt
        assert "400.0" in receipt