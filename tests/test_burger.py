from burger import Burger
from unittest.mock import Mock
import pytest


@pytest.fixture
def burger():
    return Burger()

class TestBurger:
    def test_set_buns(self, burger):
        mock_bun = Mock()
        mock_bun.name = "Чесночная"
        mock_bun.price = 120.0
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient
        burger.remove_ingredient(0)

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger):
        mock_ingredient_1 = Mock()
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_2)

        mock_ingredient_3 = Mock()
        burger.add_ingredient(mock_ingredient_3)

        burger.move_ingredient(1, 0)
        assert burger.ingredients == [
            mock_ingredient_2,
            mock_ingredient_1,
            mock_ingredient_3]

    @pytest.mark.parametrize(
        "bun_price, ingredient_price, expected",
        [
            (120, 50, 290),  # один ингредиент
            (100, 30, 230),  # другой вариант
            (150, 70, 370),  # ещё вариант
        ]
    )
    def test_get_price(
            self, burger, bun_price, ingredient_price, expected):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.bun = mock_bun

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger.ingredients = [mock_ingredient]

        assert burger.get_price() == expected

    def test_get_receipt(self, burger):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Чесночная"
        mock_bun.get_price.return_value = 120
        burger.bun = mock_bun

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "Овощи"
        mock_ingredient.get_name.return_value = "Помидоры"
        mock_ingredient.get_price.return_value = 50
        burger.ingredients = [mock_ingredient]

        result = burger.get_receipt()

        expected = (
            "(==== Чесночная ====)\n"
            "= овощи Помидоры =\n"
            "(==== Чесночная ====)\n\n"
            "Price: 290"
        )
        assert result == expected
