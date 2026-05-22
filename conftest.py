import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():

    return Burger()


@pytest.fixture
def mock_bun():

    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Флюоресцентная булка R2-D3"
    bun.get_price.return_value = 988.0
    return bun


@pytest.fixture
def mock_ingredient_sauce():

    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "Соус фирменный Space Sauce"
    ingredient.get_price.return_value = 80.0
    return ingredient


@pytest.fixture
def mock_ingredient_filling():

    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_name.return_value = "Мясо бессмертных моллюсков Protostomia"
    ingredient.get_price.return_value = 1337.0
    return ingredient
