from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
import pytest
from unittest.mock import Mock


class TestBurger:
    def test_set_buns_bun_is_added(self):
        bun = Bun('red bun', 300)
        burger = Burger()
        burger.set_buns(bun)
        assert 'red bun' in burger.get_receipt()

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_prise",
                             [[ingredient_types.INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
                              [ingredient_types.INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
                              [ingredient_types.INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
                              [ingredient_types.INGREDIENT_TYPE_FILLING, 'sausage', 300]
                              ])
    def test_add_ingredient_ingredient_is_added(self, ingredient_type, ingredient_name, ingredient_prise):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_prise)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_ingredient_is_removed(self):
        burger = Burger()
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient_one = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'dinosaur', 200)
        ingredient_two = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_two

    def test_get_price(self):
        bun = Bun('red bun', 300)
        mock_ingredient = Mock()
        mock_ingredient.return_value = [ingredient_types.INGREDIENT_TYPE_FILLING, 'dinosaur', 200]
        mock_ingredient.get_price.return_value = 200
        burger = Burger()
        burger.set_buns(bun)
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 300*2+200

    def test_get_receipt(self):
        bun = Bun('red bun', 300)
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 200
        mock_ingredient.get_type.return_value = 'FILLING'
        mock_ingredient.get_name.return_value = 'dinosaur'
        burger = Burger()
        burger.set_buns(bun)
        burger.ingredients = [mock_ingredient]
        mock = Mock()
        mock.get_price.return_value = 800
        assert burger.get_receipt() == '(==== red bun ====)\n= filling dinosaur =\n(==== red bun ====)\n\nPrice: 800'
