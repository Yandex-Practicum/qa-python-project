import sys
import os
# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    
    #Тест на соответствие выборанной булки
    def test_set_bun_in_burger_bun_is_correct(self):
        burger = Burger()
        bun = Mock(return_value="Тестовая булочка")
        burger.set_buns(bun=bun)
        
        assert burger.bun == bun

    #Тест на проверку добавления ингридиента в список ингридиентов
    def test_add_ingredient_in_burger_list_of_ingredients_is_correct(self):
        burger = Burger()
        ingredient = Mock()
        len_of_ingredients_before = len(burger.ingredients)
        burger.add_ingredient(ingredient=ingredient)
        
        assert ingredient in burger.ingredients
        assert (len(burger.ingredients) == len_of_ingredients_before + 1)

    #Тест на удаление ингридиента из списка ингридиентов
    def test_remove_ingredient_from_burger_list_of_ingredients_is_correct(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient=ingredient)
        len_of_ingredients_before = len(burger.ingredients)
        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients
        assert len(burger.ingredients) == len_of_ingredients_before - 1

    #Тест на перемену мест ингридиентов в списке
    def test_move_ingredient_new_place_is_correct(self):
        burger = Burger()
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        before_moving_ingredient = burger.ingredients[0] == ingredient_1
        burger.move_ingredient(0, 1)
        
        assert (before_moving_ingredient is True and
                burger.ingredients[0] == ingredient_2 and
                burger.ingredients[1] == ingredient_1)

    #Тест на проверку цены бургера
    def test_get_price_of_burger_price_is_correct(self):
        burger = Burger()
        bun = Mock()
        ingredient = Mock()
        bun.get_price.return_value = 1000
        ingredient.get_price.return_value = 111
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)
        assert burger.get_price() == 2111

    #Тест формирования корректного чека
    def test_get_receipt_of_burger_is_correct(self):
        burger = Burger()
        bun = Mock()
        ingredient = Mock()
        bun.get_name.return_value = 'Тестовая булочка'
        bun.get_price.return_value = 1000
        ingredient.get_name.return_value = 'Кетчунез'
        ingredient.get_price.return_value = 111
        ingredient.get_type.return_value = 'SAUCE'
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)

        assert burger.get_receipt() == \
'''(==== Тестовая булочка ====)
= sauce Кетчунез =
(==== Тестовая булочка ====)

Price: 2111'''
