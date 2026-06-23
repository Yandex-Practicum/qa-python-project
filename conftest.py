import pytest
import data


from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture(scope='function')
def bun():
    bun = Bun(name="Булочка с маком", price=45.0)
    return bun

@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger

@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="сырный", price=30.0)
    return ingredient

@pytest.fixture
def db():
    return Database()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.name = 'Булка с маком'
    bun.price = 45.0
    bun.get_name.return_value = "Булочка с маком"
    bun.get_price.return_value = 45.0
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.ingredient_type = INGREDIENT_TYPE_SAUCE
    ingredient.name = 'сырный'
    ingredient.price = 30.0
    return ingredient

@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.type = INGREDIENT_TYPE_FILLING
    ingredient.name = data.INGREDIENT_FILLING_NAME
    ingredient.price = data.PRICE_FILLING
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = data.INGREDIENT_FILLING_NAME
    ingredient.get_price.return_value = data.PRICE_FILLING
    return ingredient

@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.type = INGREDIENT_TYPE_SAUCE
    ingredient.name = data.INGREDIENT_SAUCE_NAME
    ingredient.price = data.PRICE_SAUCE
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = data.INGREDIENT_SAUCE_NAME
    ingredient.get_price.return_value = data.PRICE_SAUCE
    return ingredient

@pytest.fixture
def mock_burger_with_two_ingredients(mock_ingredient_filling, mock_ingredient_sauce):
    """Фикстура с бургером, у которого в списке два мок-ингредиента"""
    burger = Burger()
    
    burger.ingredients = [mock_ingredient_filling, mock_ingredient_sauce]
    return burger