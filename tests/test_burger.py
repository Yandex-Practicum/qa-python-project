import pytest

from praktikum.burger import Burger
from helpers import create_bun, create_ingredient

class TestBurger:

    def test_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = create_bun()
        burger.set_buns(bun)
        assert burger.bun is bun
        assert burger.bun.get_name() == "Булочка"
        assert burger.bun.get_price() == 100

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = create_ingredient()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]
        assert burger.ingredients[0].get_name() == "Соус"

    def test_remove_ingredient(self):
        burger = Burger()
        first = create_ingredient(name="РџРµСЂРІС‹Р№")
        second = create_ingredient(name="Соус")
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.remove_ingredient(0)
        assert burger.ingredients == [second]
        assert burger.ingredients[0].get_name() == "Соус"

    @pytest.mark.parametrize("index, new_index, expected",
        [
            (0, 1, ["B", "A", "C"]),
            (2, 0, ["C", "A", "B"]),
            (1, 1, ["A", "B", "C"]),
        ],
    )
    def test_move_ingredient(self, index, new_index, expected):
        burger = Burger()
        for name in ["A", "B", "C"]:
            burger.add_ingredient(create_ingredient(name=name))
        burger.move_ingredient(index, new_index)
        actual = [
            ingredient.get_name()
            for ingredient in burger.ingredients
        ]
        assert actual == expected

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price",
        [
            (100, [], 200),
            (100, [50], 250),
            (100, [50, 30, 20], 300),
            (0, [10, 15], 25),
        ],
    )
    def test_get_price(self, bun_price, ingredient_prices, expected_price):
        burger = Burger()
        burger.set_buns(create_bun(price=bun_price))

        for price in ingredient_prices:
            burger.add_ingredient(create_ingredient(price=price))
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(create_bun(name="Р¤Р»СЋРѕСЂРµСЃС†РµРЅС‚РЅР°СЏ Р±СѓР»РѕС‡РєР°", price=100))
        burger.add_ingredient(create_ingredient("SAUCE", "РЎС‹СЂРЅС‹Р№", 50))
        burger.add_ingredient(create_ingredient("FILLING", "РљРѕС‚Р»РµС‚Р°", 100))

        expected_receipt = (
            "(==== Р¤Р»СЋРѕСЂРµСЃС†РµРЅС‚РЅР°СЏ Р±СѓР»РѕС‡РєР° ====)\n"
            "= sauce РЎС‹СЂРЅС‹Р№ =\n"
            "= filling РљРѕС‚Р»РµС‚Р° =\n"
            "(==== Р¤Р»СЋРѕСЂРµСЃС†РµРЅС‚РЅР°СЏ Р±СѓР»РѕС‡РєР° ====)\n"
            "\n"
            "Price: 350"
        )

        assert burger.get_receipt() == expected_receipt


