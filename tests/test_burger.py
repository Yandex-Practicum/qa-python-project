from unittest.mock import Mock

import pytest

from praktikum.praktikum import Burger
from . import data


@pytest.fixture
def burger() -> Burger:
    """Новый пустой бургер для каждого теста."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Булочка с фиксированными тестовыми параметрами."""
    bun = Mock()
    bun.get_name.return_value = data.BUN_NAME_BLACK
    bun.get_price.return_value = data.BUN_PRICE_DEFAULT
    return bun


@pytest.fixture
def burger_with_bun(burger, mock_bun):
    """Бургер, в который уже установлена булочка."""
    burger.set_buns(mock_bun)
    return burger


@pytest.fixture
def mock_sauce():
    """Соус с фиксированными тестовыми параметрами."""
    sauce = Mock()
    sauce.get_type.return_value = data.INGREDIENT_TYPE_SAUCE
    sauce.get_name.return_value = data.INGREDIENT_NAME_HOT_SAUCE
    sauce.get_price.return_value = data.INGREDIENT_PRICE_HOT_SAUCE
    return sauce


class TestBurger:
    """Набор тестов для класса Burger."""

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = data.INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = data.INGREDIENT_NAME_HOT_SAUCE
        mock_ingredient.get_price.return_value = data.INGREDIENT_PRICE_HOT_SAUCE

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    def test_move_ingredient(self, burger):
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(2, 0)

        assert burger.ingredients[0] == mock_ingredient3
        assert burger.ingredients[1] == mock_ingredient1
        assert burger.ingredients[2] == mock_ingredient2

    def test_get_receipt(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)

        receipt = burger_with_bun.get_receipt()

        expected_receipt = "\n".join(
            [
                f"(==== {data.BUN_NAME_BLACK} ====)",
                f"= {data.INGREDIENT_TYPE_SAUCE.lower()} {data.INGREDIENT_NAME_HOT_SAUCE} =",
                f"(==== {data.BUN_NAME_BLACK} ====)\n",
                f"Price: {burger_with_bun.get_price()}",
            ]
        )

        assert receipt == expected_receipt

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        data.PRICE_COMBINATIONS,
    )
    def test_get_price_with_different_combinations(
        self, burger, bun_price, ingredient_prices, expected_total
    ):
        # mock булочки
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        # mock ингредиентов
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total
