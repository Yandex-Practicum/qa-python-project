from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]


    def test_remove_ingredient_OK(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []


    def test_move_ingredient_OK(self, mock_ingredient):
        burger = Burger()
        ingredient1 = Ingredient('filling', 'cutlet', 18)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient, ingredient1]

    def test_burger_price_OK(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert burger.get_price() == burger_price

    def test_get_receipt_OK(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert receipt == ("(==== sweet_bun ====)\n"
        "= filling hot sauce =\n"
        "(==== sweet_bun ====)\n"
        "\n"
        "Price: 276")


