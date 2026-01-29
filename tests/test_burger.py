import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import ingredient_name_first, ingredient_price_first, ingredient_type_first, ingredient_type_double, ingredient_name_double, ingredient_price_double
class TestBurgers:

    def test_set_buns_true(self, item_of_mock_bun_class):

        burger = Burger()
        burger.set_buns(item_of_mock_bun_class)
        assert burger.bun == item_of_mock_bun_class

    @pytest.mark.parametrize('ingredients_type,ingredients_name,ingredients_price',
    [
        [ingredient_type_first, ingredient_name_first, ingredient_price_first],
        [ingredient_type_double, ingredient_name_double, ingredient_price_double],

    ]
                             )
    def test_add_ingredient_true(self, ingredients_type, ingredients_name, ingredients_price):
        ingredient = Ingredient(ingredients_type, ingredients_name, ingredients_price)
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]


    def test_remove_ingredient_true(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_true(self):

        ingredient_first = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient_double = Ingredient(ingredient_type_double, ingredient_name_double, ingredient_price_double)
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_double)
        burger.move_ingredient(1,0)

        assert burger.ingredients[0] == ingredient_double
        assert burger.ingredients[1] == ingredient_first


    def test_get_price_true(self, item_of_mock_bun_class):
        burger = Burger()
        burger.set_buns(item_of_mock_bun_class)
        ingredient_first = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient_double = Ingredient(ingredient_type_double, ingredient_name_double, ingredient_price_double)
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_double)

        assert burger.get_price() == 115.0


    def test_get_receipt_true(self, item_of_mock_bun_class):
        burger = Burger()
        burger.set_buns(item_of_mock_bun_class)
        ingredient_first = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)
        ingredient_double = Ingredient(ingredient_type_double, ingredient_name_double, ingredient_price_double)
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_double)
        assert ('(==== Bulka ====)\n' '= sauce Cheese =\n' '= filling Spicy =\n' '(==== Bulka ====)\n' '\n' 'Price: 115.0') == burger.get_receipt()

