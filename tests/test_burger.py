from unittest.mock import Mock

from praktikum.burger import Burger, Bun
from praktikum.database import Database
import praktikum.ingredient_types as IngredientTypes


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Краторная булка N-200i', 1255)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Краторная булка N-200i'
        mock_ingredient.get_price.return_value = 1255
        mock_ingredient.get_type.return_value = IngredientTypes.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
        assert burger.ingredients[
                   0].get_name() == 'Краторная булка N-200i'
        assert burger.ingredients[0].get_price() == 1255
        assert burger.ingredients[
                   0].get_type() == IngredientTypes.INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, "The burger should have no ingredients after removal."

    def test_get_price(self):
        burger = Burger()
        burger.set_buns(Database().available_buns()[1])  #200*2
        burger.add_ingredient(Database().available_ingredients()[1])  #200
        burger.add_ingredient(Database().available_ingredients()[5])  #300
        assert burger.get_price() == 900
    def test_get_receipt(self):
        burger = Burger()
        bun_selected = Database().available_buns()[1]
        burger.set_buns(bun_selected)
        ingredient1 = Database().available_ingredients()[1]
        ingredient2 = Database().available_ingredients()[5]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        Database().bun = bun_selected
        expected_receipt = "(==== white bun ====)\n"\
            "= sauce sour cream =\n"\
            "= filling sausage =\n"\
            "(==== white bun ====)\n\n"\
            "Price: 900"
        assert burger.get_receipt() == expected_receipt
