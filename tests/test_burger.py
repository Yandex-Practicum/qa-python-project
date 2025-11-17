from helpers import data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Булка', 100)
        burger.set_buns(bun)

        assert burger.bun.get_name() == 'Булка'
        assert burger.bun.get_price() == 100

    def test_add_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Ingredient)

        assert burger.ingredients == [Ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_burger_move_ingredient(self):
        burger = Burger()
        burger.add_ingredient(Ingredient)
        burger.add_ingredient(Ingredient)
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [Ingredient, Ingredient]

    def test_get_price(self):
        burger = Burger()
        burger.set_buns(data.mock_bun)
        burger.add_ingredient(data.mock_filling)
        burger.add_ingredient(data.mock_sauce)
        burger_price = data.mock_bun.get_price() * 2 + data.mock_filling.get_price() + data.mock_sauce.get_price()

        assert burger.get_price() == burger_price

    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(data.mock_bun)
        burger.add_ingredient(data.mock_filling)
        burger.add_ingredient(data.mock_sauce)
        burger_receipt = (
            f"(==== {data.mock_bun.get_name()} ====)\n"
            f"= {data.mock_filling.get_type().lower()} {data.mock_filling.get_name()} =\n"
            f"= {data.mock_sauce.get_type().lower()} {data.mock_sauce.get_name()} =\n"
            f"(==== {data.mock_bun.get_name()} ====)\n\n"
            f"Price: {data.mock_bun.get_price() * 2 + data.mock_filling.get_price() + data.mock_sauce.get_price()}"
        )

        assert burger.get_receipt() == burger_receipt




