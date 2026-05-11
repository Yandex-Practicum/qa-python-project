import pytest
from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun
        assert burger.bun.get_name() == "black bun"


    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]
        assert len(burger.ingredients) == 1


    def test_remove_ingredient(self, burger, mock_ingredient):
        ingredient_2 = Mock()
        burger.ingredients = [mock_ingredient, ingredient_2]

        burger.remove_ingredient(0)

        assert burger.ingredients == [ingredient_2]


    def test_move_ingredient(self, burger, mock_ingredient):
        ingredient_2 = Mock()

        burger.ingredients = [mock_ingredient, ingredient_2]

        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_2, mock_ingredient]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100, [100, 200], 500),
            (200, [100, 200], 700),
            (100, [300], 500),
        ],
    )
    def test_get_price(self, burger, bun_price, ingredient_prices, expected_price):
        bun = Mock()
        bun.get_price.return_value = bun_price

        ingredients = []
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)

        burger.set_buns(bun)
        burger.ingredients = ingredients

        assert burger.get_price() == expected_price

    
    def test_get_receipt(self, burger):
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100

        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 200

        burger.set_buns(bun)
        burger.ingredients = [sauce, filling]

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 500"
        )

        assert burger.get_receipt() == expected_receipt



    