from unittest.mock import Mock

from info import InfoBun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger():

    def test_set_buns(self):
        mock_bun = Mock()
        burger = Burger()
        mock_bun.get_price.return_value = 10
        mock_bun.get_name.return_value = InfoBun.BUN_WITH_POPPY_SEED
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        mock_ingredient.get_price.return_value = 9
        mock_ingredient.get_name.return_value = InfoBun.INGREDIENT_BACON
        mock_ingredient.get_type.return_value = InfoBun.INGREDIENT_CHICKEN
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.ingredients.append(mock_ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients.append(mock_ingredient_1)
        burger.ingredients.append(mock_ingredient_2)
        assert burger.ingredients[0] == mock_ingredient_1
        assert burger.ingredients[1] == mock_ingredient_2

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 11
        burger.bun = mock_bun
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 10
        burger.ingredients.append(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 9
        burger.ingredients.append(mock_ingredient_2)

        expected_price = (11 * 2) + 10 + 9
        assert burger.get_price() == expected_price
    def test_get_receipt(self):
        mock_receipt = Mock()
        burger = Burger()
        mock_receipt.get_name.return_value = InfoBun.SOURDOUND_BUN
        mock_receipt.get_price.return_value = 10
        burger.set_buns(mock_receipt)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, InfoBun.SOURDOUND_BUN, 10)
        burger.add_ingredient(sauce)
        assert sauce in burger.ingredients
