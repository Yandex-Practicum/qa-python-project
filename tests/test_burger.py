from typing import List
import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from data import Data
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    @pytest.mark.parametrize('choise',[0,1,2])
    def test_create_burger_only_buns(self, things, choise):   
        buns, ingredients, burger = things
        burger.set_buns(buns[choise])
        burger.add_ingredient(ingredients[1])
        burger.remove_ingredient(0)
        result_burger = burger.get_receipt().split('\n')

        assert result_burger[0] == result_burger[1]

    def test_add_and_remove_ingredients(self, things):
        buns, ingredients, burger = things
        burger.set_buns(buns[1])
        burger.add_ingredient(ingredients[5])
        burger.remove_ingredient(0)
        result_burger = burger.get_receipt().split('\n')

        assert result_burger[0] == result_burger[1]        

    @pytest.mark.parametrize('result, after_move',[
        [1,2], 
        [2, 1] ]) 
    def test_move_ingredients(self, things, result, after_move):
        buns, ingredients, burger = things
        burger.set_buns(buns[1])
        burger.add_ingredient(ingredients[5])
        burger.add_ingredient(ingredients[0])
        result_burger = burger.get_receipt().split('\n')
        burger.move_ingredient(0, 1)
        burger_after_move = burger.get_receipt().split('\n')

        assert result_burger[result] == burger_after_move[after_move]    

    @pytest.mark.parametrize('choise, price',[
        [0, 400.0], 
        [1, 800.0], 
        [2, 1200.0] ])  
    def test_get_price_burger(self, things, choise, price):
        buns, ingredients, burger = things
        burger.set_buns(buns[choise])
        burger.add_ingredient(ingredients[choise])
        burger.add_ingredient(ingredients[3 + choise])

        assert burger.get_price() == price

    @pytest.mark.parametrize('choise', [0,1,2])
    def test_create_burger(self, choise):
        moc_databese = Mock()
        moc_databese.available_buns.return_value = [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
        moc_databese.available_ingredients.return_value = [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),

            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
        burger: Burger = Burger()
        buns: List[Bun] = moc_databese.available_buns()
        ingredients: List[Ingredient] = moc_databese.available_ingredients()
        burger.set_buns(buns[choise])
        burger.add_ingredient(ingredients[choise])
        burger.add_ingredient(ingredients[3 + choise])
        result_burger = burger.get_receipt()

        assert Data.expect_burger(choise) == result_burger

    @pytest.mark.parametrize('choise',[0,1,2])
    def test_set_buns(self, things, choise):  
        buns, ingredients, burger = things
        burger.set_buns(buns[choise])
        result_burger = burger.bun.get_name()

        assert Data.expect_bun(choise) == result_burger

    @pytest.mark.parametrize('choise',[0,1,2,3,4,5])
    def test_add_ingredient(self, things, choise):
        buns, ingredients, burger = things
        burger.add_ingredient(ingredients[choise])
        result_burger = burger.ingredients[0].get_name()

        assert Data.expect_ingredient(choise) == result_burger
