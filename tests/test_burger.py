import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from conftest import mock_bun, mock_ingredients


class TestBurgerFunction:
    @pytest.mark.parametrize(
        'name,price',
        [
            ['Звёздная булка JK-22', 1232],
            ['Краторная булка N-200i', 1255]
        ]
    )
    def test_burger_successfully_set_buns(self, name, price):
        burger = Burger()
        bun = Bun(name, price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == name

    def test_burger_successfully_add_ingredient(self):
        burger = Burger()
        fill = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        burger.add_ingredient(fill)
        assert len(burger.ingredients) == 1

    def test_burger_successfully_remove_ingredient(self):
        burger = Burger()
        fill = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        burger.add_ingredient(fill)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_burger_successfully_move_ingredient(self):
        burger = Burger()
        fill_1 = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        fill_2 = Ingredient(INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337)
        burger.add_ingredient(fill_1)
        burger.add_ingredient(fill_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == fill_1

    def test_burger_successfully_get_price(self):
        burger = Burger()
        fill = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 80)
        burger.add_ingredient(fill)
        bun = Bun('Краторная булка N-200i', 1255)
        burger.set_buns(bun)
        assert burger.get_price() == 2590.0

    def test_burger_get_receipt_mock(self, mock_bun, mock_ingredients):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)
        receipt = burger.get_receipt()
        assert 'Price: 2126' in receipt