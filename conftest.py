import pytest
import allure

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from data import Data

from unittest.mock import Mock


@pytest.fixture(scope='function')
@allure.title('Фикстура для создания бургера')
def burger():
    burger = Burger()
    burger.bun = Bun(Data.crater_bun, Data.crater_bun_price)
    burger.ingredients = [
        Ingredient(INGREDIENT_TYPE_SAUCE,
                   Data.sauce_spicy,
                   Data.sauce_spicy_price),
        Ingredient(INGREDIENT_TYPE_FILLING,
                   Data.filling_beef_meteorite,
                   Data.filling_beef_meteorite_price)
    ]
    return burger

@pytest.fixture(scope='function')
@allure.title('Фикстура для создания мок-объекта')
def mock_db():
    return Mock()

