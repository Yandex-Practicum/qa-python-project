from Diplom_1.data import DataForTests
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE
from Diplom_1.burger import Burger


class TestBurger:

    def test_set_buns_successfully(self, mock, bun):
        burger = Burger()
        mock.get_name.return_value = DataForTests.BLACK_BUN
        mock.get_price.return_value = DataForTests.PRICE_BLACK_BUN
        burger.set_buns(mock)
        assert (burger.bun.get_name() == DataForTests.BLACK_BUN and
                burger.bun.get_price() == DataForTests.PRICE_BLACK_BUN)

    def test_add_ingredient_successfully(self, mock):
        burger = Burger()
        mock.get_price.return_value = DataForTests.PRICE_HOT_SAUSE
        mock.get_name.return_value = DataForTests.HOT_SAUSE
        mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock)
        assert burger.ingredients == [mock]

    def test_remove_ingredient_successfully(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_successfully(self):
        burger = Burger()
        ingredient_0 = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.HOT_SAUSE, DataForTests.PRICE_HOT_SAUSE)
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.CHILI_SAUSE, DataForTests.PRICE_CHILI_SAUSE)
        burger.add_ingredient(ingredient_0)
        burger.add_ingredient(ingredient_1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1].name == DataForTests.HOT_SAUSE

    def test_get_price_successfully(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.HOT_SAUSE, DataForTests.PRICE_HOT_SAUSE))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.CHILI_SAUSE, DataForTests.PRICE_CHILI_SAUSE))
        assert burger.get_price() == 140

    def test_get_receipt_successfully(self, mock):
        burger = Burger()
        mock.get_name.return_value = DataForTests.BLACK_BUN
        mock.get_price.return_value = DataForTests.PRICE_BLACK_BUN
        burger.set_buns(mock)
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.SOUR_CREAM, DataForTests.PRICE_SOUR_CREAM))
        assert burger.get_receipt() == DataForTests.RECEIPT
