import pytest
from unittest.mock import Mock
from practicum_burgers.bun import Bun
from practicum_burgers.ingredient import Ingredient

@pytest.fixture
def bun_mock():
    def _create(burger, price=50, name="Булка"):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = price
        bun.get_name.return_value = name
        burger.set_buns(bun)
        return bun
    return _create

@pytest.fixture
def ingredient_mock():
    def _create(burger, ingredient_type='SAUCE', price=30, name="Сыр"):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_price.return_value = price
        ingredient.get_name.return_value = name
        burger.add_ingredient(ingredient)
        return ingredient
    return _create
