import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from data import ingredient_1, ingredient_2, ingredient_3, actual_receipt


class TestBurger:

    def test_set_buns_success(self, mock_bun, mock_burger):
        mock_burger.set_buns(mock_bun)
        assert  mock_burger.bun == mock_bun

    def test_add_ingredient_success(self, mock_ingredient):
        burger = Burger() 
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients 


    @pytest.mark.parametrize('ingredients, count',
    [
        ([ingredient_1], 1),
        ([ingredient_2, ingredient_3], 2)
    ])
    def test_remove_ingredient_success(self, ingredients, count):
        burger = Burger() 
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == count
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == (count-1)


    def test_move_ingredient_success(self):
        burger = Burger()
        burger.ingredients = [ingredient_1, ingredient_2, ingredient_3]
        burger.move_ingredient(index=2, new_index=0)
        assert burger.ingredients[0] == ingredient_3


    @pytest.mark.parametrize('bun_price, ingredients_price, result',
    [
        (100,300,500),
        (100,0,200),
        (0,400,400)
    ])
    def test_get_price_success(self, mock_bun, mock_ingredient, bun_price, ingredients_price, result):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredients_price
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == result


    def test_get_receipt_success(self, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = 'bulochka'
        mock_bun.get_price.return_value = 100
        mock_ingredient.get_type.return_value = 'main'
        mock_ingredient.get_name.return_value = 'chicken'
        mock_ingredient.get_price.return_value = 300

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_receipt() == actual_receipt

