import pytest
from praktikum.bun import Bun
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture  # фикстура для создания тестового экземпляра булочки
def bun():
    return Bun('Краторная булка', 125.50)


@pytest.fixture  # мок для булочки
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture   # мок для соуса
def mock_ingredient_sauce():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50
    return ingredient

@pytest.fixture   # мок для начинки
def mock_ingredient_filling():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "cheese"
    ingredient.get_price.return_value = 30
    return ingredient

@pytest.fixture   # фикстура готового бургера с моками (булочка + соус + начинка)
def prepared_burger(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger
