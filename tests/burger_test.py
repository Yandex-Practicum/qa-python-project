from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger() -> Burger:
    """Пустой бургер для каждого теста."""
    return Burger()


def make_bun(name: str = 'black bun', price: float = 100) -> Mock:
    """Мок булочки с заданным именем и ценой."""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun


def make_ingredient(name: str, ingredient_type: str, price: float) -> Mock:
    """Мок ингредиента с заданным именем, типом и ценой."""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = name
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_price.return_value = price
    return ingredient


class TestBurgerInit:

    def test_new_burger_has_no_bun(self, burger):
        assert burger.bun is None

    def test_new_burger_has_no_ingredients(self, burger):
        assert burger.ingredients == []


class TestSetBuns:

    def test_set_buns_sets_bun(self, burger):
        bun = make_bun()

        burger.set_buns(bun)

        assert burger.bun is bun


class TestAddIngredient:

    def test_add_ingredient_appends_to_list(self, burger):
        ingredient = make_ingredient('hot sauce', INGREDIENT_TYPE_SAUCE, 100)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('count', [1, 2, 5])
    def test_add_ingredient_adds_all_in_order(self, burger, count):
        ingredients = [
            make_ingredient(f'ingredient_{n}', INGREDIENT_TYPE_FILLING, 10)
            for n in range(count)
        ]

        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.ingredients == ingredients


class TestRemoveIngredient:

    @pytest.mark.parametrize(
        'index, expected_names',
        [
            (0, ['b', 'c']),
            (1, ['a', 'c']),
            (2, ['a', 'b']),
        ],
    )
    def test_remove_ingredient_removes_item_by_index(self, burger, index, expected_names):
        for name in ['a', 'b', 'c']:
            burger.add_ingredient(make_ingredient(name, INGREDIENT_TYPE_FILLING, 10))

        burger.remove_ingredient(index)

        assert [ingredient.get_name() for ingredient in burger.ingredients] == expected_names


class TestMoveIngredient:

    @pytest.mark.parametrize(
        'index, new_index, expected_names',
        [
            (0, 1, ['b', 'a', 'c']),
            (0, 2, ['b', 'c', 'a']),
            (1, 2, ['a', 'c', 'b']),
            (2, 0, ['c', 'a', 'b']),
        ],
    )
    def test_move_ingredient_changes_order(self, burger, index, new_index, expected_names):
        for name in ['a', 'b', 'c']:
            burger.add_ingredient(make_ingredient(name, INGREDIENT_TYPE_FILLING, 10))

        burger.move_ingredient(index, new_index)

        assert [ingredient.get_name() for ingredient in burger.ingredients] == expected_names


class TestGetPrice:

    @pytest.mark.parametrize(
        'bun_price, ingredient_prices, expected',
        [
            (100, [], 200),
            (100, [100], 300),
            (200, [50, 150], 600),
            (0, [0], 0),
            (12.5, [7.5, 5.0], 37.5),
        ],
    )
    def test_get_price_sums_bun_twice_and_ingredients(
        self, burger, bun_price, ingredient_prices, expected
    ):
        burger.set_buns(make_bun(price=bun_price))
        for price in ingredient_prices:
            burger.add_ingredient(make_ingredient('ingredient', INGREDIENT_TYPE_FILLING, price))

        assert burger.get_price() == expected


class TestGetReceipt:

    def test_get_receipt_builds_expected_text(self, burger):
        burger.set_buns(make_bun(name='black bun', price=100))
        burger.add_ingredient(make_ingredient('hot sauce', INGREDIENT_TYPE_SAUCE, 100))
        burger.add_ingredient(make_ingredient('cutlet', INGREDIENT_TYPE_FILLING, 200))

        expected = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 500'
        )

        assert burger.get_receipt() == expected

    def test_get_receipt_without_ingredients(self, burger):
        burger.set_buns(make_bun(name='white bun', price=200))

        expected = (
            '(==== white bun ====)\n'
            '(==== white bun ====)\n'
            '\n'
            'Price: 400'
        )

        assert burger.get_receipt() == expected
