import pytest
import data


class TestBurger:

    def test_setting_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_adding_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    @pytest.mark.parametrize(
        'ingredients, result',
        [
            (data.INGREDIENT_LIST, data.INGREDIENT_LIST_AFTER_REMOVE),
            (data.ONE_INGREDIENT, []),
        ]
    )
    def test_removing_ingredient(self, burger, ingredients, result):
        burger.ingredients = ingredients.copy()
        burger.remove_ingredient(0)
        assert burger.ingredients == result

    def test_moving_ingredient(self, burger):
        burger.ingredients = data.INGREDIENT_LIST.copy()
        burger.move_ingredient(0,2)
        assert burger.ingredients == data.INGREDIENT_LIST_AFTER_MOVING

    def test_getting_burger_price_without_ingredients(self, burger, mock_bun):
        burger.bun = mock_bun
        burger.ingredients = []
        assert burger.get_price() == 200.0

    def test_getting_burger_price_with_ingredients(self, burger, mock_bun, mock_ingredient):
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 270.0

    def test_getting_receipt_with_ingredients(self, burger, mock_bun, mock_ingredient):
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_receipt() == data.RECEIPT1

    def test_getting_receipt_without_ingredients(self, burger, mock_bun):
        burger.bun = mock_bun
        assert burger.get_receipt() == data.RECEIPT2
