import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    DATA_FOR_GET_PRICE = [(['roll', 125], [[INGREDIENT_TYPE_FILLING, 'cheese', 50]], 300),
                          (['pancake', 100],
                           [[INGREDIENT_TYPE_FILLING, 'chicken', 350], [INGREDIENT_TYPE_SAUCE, 'ketchup', 50]],
                           600)]
    DATA_INGREDIENTS = [([[INGREDIENT_TYPE_FILLING, 'cheese', 50]], 1),
                        ([[INGREDIENT_TYPE_FILLING, 'chicken', 350], [INGREDIENT_TYPE_SAUCE, 'ketchup', 50]], 2)]

    def test_set_buns(self):
        burger_name = 'roll'
        burger = Burger()
        burger.set_buns(burger_name)

        assert burger_name == burger.bun

    @pytest.mark.parametrize('ingredients,count', DATA_INGREDIENTS)
    def test_add_ingredients(self, ingredients, count):

        burger = Burger()
        for element in ingredients:
            burger.add_ingredient(element)

        assert ingredients == burger.ingredients
        assert count == len(burger.ingredients)

    def test_remove_one_ingredient(self):
        ingredients = [[INGREDIENT_TYPE_FILLING, 'sausage', 100], [INGREDIENT_TYPE_SAUCE, 'honey', 110]]
        burger = Burger()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        burger.remove_ingredient(0)

        assert ingredients[1] in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        ingredients = [[INGREDIENT_TYPE_FILLING, 'cheese', 100], [INGREDIENT_TYPE_SAUCE, 'honey', 100]]

        burger = Burger()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[1])
        burger.move_ingredient(1, 0)

        assert ingredients[::-1] == burger.ingredients
        assert len(burger.ingredients) == 2

    @pytest.mark.parametrize('my_bun, my_ingredient, result', DATA_FOR_GET_PRICE)
    def test_get_burger_price(self, my_bun, my_ingredient, result):
        bun = Bun(*my_bun)
        burger = Burger()
        burger.set_buns(bun)
        for element in my_ingredient:
            ingredient = Ingredient(*element)
            burger.add_ingredient(ingredient)

        assert result == burger.get_price()

    def test_get_burger_receipt_one_ingredient(self):
        ingredients = [INGREDIENT_TYPE_SAUCE, 'ketchup', 250]
        buns = ['roll', 200]

        bun = Bun(*buns)
        ingredient = Ingredient(*ingredients)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        answer = (f'(==== {buns[0]} ====)\n= {ingredients[0].lower()} {ingredients[1]} =\n(==== {buns[0]} ====)\n'
                  f'\nPrice: {buns[1] * 2 + ingredients[2]}')

        assert answer == burger.get_receipt()
