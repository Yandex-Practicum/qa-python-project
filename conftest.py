import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from data import BUN_PARAMS, SAUCE_PARAMS, FILLING_PARAMS
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock


@pytest.fixture() # создание экземпляра булочки
def bun():
    bun = Bun(BUN_PARAMS['name'], BUN_PARAMS['price'])
    return bun

@pytest.fixture() # создание экземпляра бургера
def burger():
    burger = Burger()
    return burger

@pytest.fixture # создание экземпляра соуса
def sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_PARAMS['name'], SAUCE_PARAMS['price'])
    return sauce

@pytest.fixture # создание экземпляра начинки
def filling():
    filling = Ingredient(INGREDIENT_TYPE_FILLING, FILLING_PARAMS['name'], FILLING_PARAMS['price'])
    return filling

@pytest.fixture() # создание бургера с булкой
def burger_with_bun(burger):
    mock_bun = Mock() # создание мок булки
    mock_bun.get_name.return_value = BUN_PARAMS['name']
    mock_bun.get_price.return_value = BUN_PARAMS['price']
    burger.set_buns(mock_bun) # добавляем булку в бургер
    price = BUN_PARAMS['price']*2 # задаем цену бургера по  цене за две булки
    receipt1: List[str] = [f'(==== {BUN_PARAMS['name']} ====)']
    receipt2: List[str] = [f'(==== {BUN_PARAMS['name']} ====)\n']
    receipt2.append(f'Price: {BUN_PARAMS['price']*2}')
    return burger, price, receipt1, receipt2

@pytest.fixture()  # создание бургера с булкой и соусом
def burger_with_ingredient(burger_with_bun):
    mock_ingredient_sauce = Mock() # создаем мок соуса
    mock_ingredient_sauce.get_name.return_value = SAUCE_PARAMS['name']
    mock_ingredient_sauce.get_price.return_value = SAUCE_PARAMS['price']
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    burger_with_bun[0].add_ingredient(mock_ingredient_sauce) # добавляем ингредиент в бургер
    price = burger_with_bun[1] + SAUCE_PARAMS['price'] # добавляем к цене бургера цену соуса
    receipt1: List[str] = burger_with_bun[2]
    receipt1.append(f'= {INGREDIENT_TYPE_SAUCE.lower()} {SAUCE_PARAMS['name']} =')
    receipt2: List[str] = [f'(==== {BUN_PARAMS['name']} ====)\n']
    receipt2.append(f'Price: {BUN_PARAMS['price']*2+SAUCE_PARAMS['price']}')
    return burger_with_bun[0], price, receipt1, receipt2

@pytest.fixture()  # создание бургера с булками, соусом и начинкой
def burger_with_ingredients(burger_with_ingredient):
    mock_ingredient_filling = Mock() # создаем мок начинки
    mock_ingredient_filling.get_name.return_value = FILLING_PARAMS['name']
    mock_ingredient_filling.get_price.return_value = FILLING_PARAMS['price']
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    burger_with_ingredient[0].add_ingredient(mock_ingredient_filling) # добавляем ингредиент в бургер
    price = burger_with_ingredient[1] + FILLING_PARAMS['price'] # добавляем к цене бургера цену начинки
    receipt1: List[str] = burger_with_ingredient[2]
    receipt1.append(f'= {INGREDIENT_TYPE_FILLING.lower()} {FILLING_PARAMS['name']} =')
    receipt2: List[str] = [f'(==== {BUN_PARAMS['name']} ====)\n']
    receipt2.append(f'Price: {BUN_PARAMS['price']*2+SAUCE_PARAMS['price']+FILLING_PARAMS['price']}')
    return burger_with_ingredient[0], price, receipt1, receipt2
