import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:

    # ---------- set_buns ----------

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_set_buns_overwrites_previous_bun(self):
        burger = Burger()
        bun_old = Mock()
        bun_new = Mock()
        burger.set_buns(bun_old)

        burger.set_buns(bun_new)

        assert burger.bun == bun_new

    # ---------- add_ingredient ----------

    def test_add_ingredient_appends_to_list(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_add_ingredient_multiple_keeps_order(self):
        burger = Burger()
        first = Mock()
        second = Mock()

        burger.add_ingredient(first)
        burger.add_ingredient(second)

        assert burger.ingredients == [first, second]

    # ---------- remove_ingredient ----------

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        first = Mock()
        second = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.remove_ingredient(0)

        assert burger.ingredients == [second]

    def test_remove_ingredient_last_element(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert burger.ingredients == []

    # ---------- move_ingredient ----------

    def test_move_ingredient_forward(self):
        burger = Burger()
        first = Mock()
        second = Mock()
        third = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [second, third, first]

    def test_move_ingredient_backward(self):
        burger = Burger()
        first = Mock()
        second = Mock()
        third = Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        burger.move_ingredient(2, 0)

        assert burger.ingredients == [third, first, second]

    # ---------- get_price ----------

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected", [
        (100, [], 200),                 # только булка: 100 * 2 = 200
        (100, [50], 250),               # булка + один ингредиент
        (100, [50, 30], 280),           # булка + два ингредиента
        (0, [], 0),                     # нулевая булка
        (0, [10], 10),                  # нулевая булка + ингредиент
        (150.5, [20.5], 321.5),         # дробные цены
    ])
    def test_get_price(self, bun_price, ingredients_prices, expected):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        actual = burger.get_price()

        assert actual == expected

    # ---------- get_receipt ----------

    def test_get_receipt_without_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "Краторная булка N-200i"
        bun.get_price.return_value = 1255
        burger.set_buns(bun)

        actual = burger.get_receipt()

        expected = (
            "(==== Краторная булка N-200i ====)\n"
            "(==== Краторная булка N-200i ====)\n"
            "\n"
            "Price: 2510"
        )
        assert actual == expected

    def test_get_receipt_with_one_ingredient(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "Краторная булка N-200i"
        bun.get_price.return_value = 100
        burger.set_buns(bun)
        ingredient = Mock()
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "Соус Spicy-X"
        ingredient.get_price.return_value = 90
        burger.add_ingredient(ingredient)

        actual = burger.get_receipt()

        expected = (
            "(==== Краторная булка N-200i ====)\n"
            "= sauce Соус Spicy-X =\n"
            "(==== Краторная булка N-200i ====)\n"
            "\n"
            "Price: 290"
        )
        assert actual == expected

    def test_get_receipt_with_multiple_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "Флюоресцентная булка R2-D3"
        bun.get_price.return_value = 988
        burger.set_buns(bun)
        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "Соус традиционный галактический"
        sauce.get_price.return_value = 30
        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "Мясо бессмертных моллюсков Protostomia"
        filling.get_price.return_value = 1337
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        actual = burger.get_receipt()

        expected = (
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "= sauce Соус традиционный галактический =\n"
            "= filling Мясо бессмертных моллюсков Protostomia =\n"
            "(==== Флюоресцентная булка R2-D3 ====)\n"
            "\n"
            "Price: 3343"
        )
        assert actual == expected