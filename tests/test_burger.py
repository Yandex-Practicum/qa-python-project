import praktikum.ingredient_types


from unittest.mock import Mock
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:
    def test_set_buns_correct(self):
        burger = Burger()

        bun = Bun('Name_bun', 100.0)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_correct(self):
        burger = Burger()
        mock_ingredient = Mock()

        mock_ingredient.get_price.return_value = 9.0
        mock_ingredient.get_name.return_value = 'тест'
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        assert burger.ingredients[0].get_price() == 9.0
        assert burger.ingredients[0].get_name() == 'тест'
        

    def test_remove_ingredient_successful(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_get_price_correct(self):
        burger = Burger()
        base = Database()

        burger.set_buns(base.available_buns()[0])
        burger.add_ingredient(base.available_ingredients()[0])
        burger.add_ingredient(base.available_ingredients()[3])

        assert burger.get_price() == 400.0

    def test_get_receipt_correct(self):
        burger = Burger()
        base = Database()

        burger.set_buns(base.available_buns()[1])
        burger.add_ingredient(base.available_ingredients()[1])
        burger.add_ingredient(base.available_ingredients()[3])

        expected_receipt = "(==== white bun ====)\n"\
                           "= sauce sour cream =\n"\
                           "= filling cutlet =\n"\
                           "(==== white bun ====)\n\n"\
                           "Price: 700"
        assert expected_receipt == burger.get_receipt()

    def test_move_ingredient_forward(self):
        burger = Burger()

        burger.ingredients = ["bun", "cutlet", "cheese", "sauce"]
        burger.move_ingredient(2, 1)
        expected = ["bun", "cheese", "cutlet", "sauce"]

        assert burger.ingredients == expected