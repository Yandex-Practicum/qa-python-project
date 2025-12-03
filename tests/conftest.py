import random
import pytest
import sys
import os

# Добавляем текущую папку в путь поиска
sys.path.append(os.path.dirname(__file__))

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import praktikum.ingredient_types as types
import constants 


@pytest.fixture(scope="function")
def new_bun():
    """Фикстура создания булки с реальным названием и ценой из Stellar Burgers"""
    bun_index = random.randint(0, len(constants.bun_names) - 1)
    return Bun(constants.bun_names[bun_index], constants.bun_prices[bun_index])


@pytest.fixture(scope="function")
def new_ingredient():
    """Фикстура создания нового рандомного ингредиента: соуса или начинки с реальными данными"""
    ingredient_type = random.choice([types.INGREDIENT_TYPE_SAUCE, types.INGREDIENT_TYPE_FILLING])
    
    if ingredient_type == types.INGREDIENT_TYPE_FILLING:
        ingredient_data = random.choice(constants.fillings)
        ingredient_name, ingredient_price = ingredient_data
    else:
        ingredient_data = random.choice(constants.sauces)
        ingredient_name, ingredient_price = ingredient_data
        
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_sauce():
    """Фикстура создания соуса с реальным названием и ценой из Stellar Burgers"""
    ingredient_data = random.choice(constants.sauces)
    ingredient_name, ingredient_price = ingredient_data
    return Ingredient(types.INGREDIENT_TYPE_SAUCE, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_filling():
    """Фикстура создания начинки с реальным названием и ценой из Stellar Burgers"""
    ingredient_data = random.choice(constants.fillings)
    ingredient_name, ingredient_price = ingredient_data
    return Ingredient(types.INGREDIENT_TYPE_FILLING, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_burger(new_bun, new_filling, new_sauce):
    """Фикстура создания готового бургера с булкой, начинкой и соусом из реальных данных"""
    burger = Burger()
    burger.set_buns(new_bun)
    burger.add_ingredient(new_filling)
    burger.add_ingredient(new_sauce)
    return burger