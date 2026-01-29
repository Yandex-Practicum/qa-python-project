from data import DataIngredient
from praktikum.burger import Burger


class TestBurger:
    def test_set_bun_burger(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_burger(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_burger(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_ingredient]

    def test_move_ingredient_burger(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(DataIngredient.INGREDIENT)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price_burger(self, mock_ingredient, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 400

    def test_get_receipt_burger(self, mock_ingredient, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert '(==== Хлебная ====)\n= filling Крабовое =\n(==== Хлебная ====)\n\nPrice: 400' == burger.get_receipt()





