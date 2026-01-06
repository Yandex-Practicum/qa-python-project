import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conftest import bunsandOtherIngredients
import pytest
from data import *
from burger import Burger
from bun import Bun

class TestBurger:
    
    """Добавление булочек"""
    @pytest.mark.parametrize("buns", TestData.buns_available)  
    def test_set_bun_success(self, buns):
        burger = Burger()
        burger.set_buns(buns)  
        assert burger.bun ==buns

    
    """Замена булочек"""
    @pytest.mark.parametrize("buns", TestData.buns_available)  
    def test_move_bun_success(self, buns):
        burger = Burger()
        burger.set_buns(buns[0])
        burger.set_buns(buns[1])
        assert burger.bun ==buns[1]

    """Добавление ингредиентов"""
    @pytest.mark.parametrize("ingredient", TestData.ingredients_available)
    def test_add_ingredient_success(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    """Удаление ингредиентов"""
    @pytest.mark.parametrize("ingredient", TestData.ingredients_available)
    def test_remove_ingredients_success(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)      
        burger.remove_ingredient(0)  
        assert burger.ingredients ==[] and ingredient not in burger.ingredients

    """Перемещение ингредиентов"""
    @pytest.mark.parametrize("ingredient_indices", [(0, 5)])
    def test_move_ingredients_success(self, ingredient_indices):
        burger = Burger()
        ingredient1=TestData.ingredients_available[ingredient_indices[0]]
        ingredient2=TestData.ingredients_available[ingredient_indices[1]]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] ==ingredient1

    """Добавление нескольких ингредиентов и удаление одного из них"""
    @pytest.mark.parametrize("ingredient_indices", [(0, 5)])
    def test_addtwo_move_one_ingredients_success(self, ingredient_indices):
        burger = Burger()
        ingredient1=TestData.ingredients_available[ingredient_indices[0]]
        ingredient2=TestData.ingredients_available[ingredient_indices[1]]
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)  
        assert burger.ingredients[0] == ingredient2 and len(burger.ingredients) ==1

    """Получение цены бургера"""
    @pytest.mark.parametrize('id_item', [0, 1])
    def test_burger_get_price_success(self, id_item, bunsandOtherIngredients):
        burger = Burger()
        burger.set_buns(bunsandOtherIngredients[0][id_item])
        burger.add_ingredient(bunsandOtherIngredients[1][id_item]) 
        assert burger.get_price() ==(bunsandOtherIngredients[0][id_item].get_price()*2+bunsandOtherIngredients[1][id_item].get_price())

    """Получение чека"""
    @pytest.mark.parametrize('id_item', [0, 1])
    def test_get_receipt(self, id_item, bunsandOtherIngredients):
        burger = Burger()
        burger.set_buns(bunsandOtherIngredients[0][id_item]) 
        burger.add_ingredient(bunsandOtherIngredients[1][id_item])  
        
        expected_receipt = BunsandOtherIngredients.get_receipt(
            bunsandOtherIngredients[0][id_item],
            bunsandOtherIngredients[1][id_item]
        )
        
        assert burger.get_receipt() == expected_receipt
