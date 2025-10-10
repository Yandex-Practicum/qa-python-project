import pytest
from unittest.mock import Mock

from praktikum_burger.burger import Burger
from praktikum_burger.bun import Bun
from praktikum_burger.ingredient import Ingredient
from praktikum_burger.database import Database


@pytest.fixture
def bun_mock():
    mock_bun = Mock(spec=Bun)    
    mock_bun.get_name.return_value = 'Сочная булочка'
    mock_bun.get_price.return_value = 50.0
    return mock_bun

@pytest.fixture
def sauce_mock():
    mock_sauce = Mock(spec=Ingredient)
    mock_sauce.get_name.return_value = 'Горчичный соус для бургера с мёдом'
    mock_sauce.get_type.return_value = 'соус'
    mock_sauce.get_price.return_value = 10.0
    return mock_sauce

@pytest.fixture
def filling_mock():
    mock_filling = Mock(spec=Ingredient)
    mock_filling.get_name.return_value = 'Сочная куриная котлета'
    mock_filling.get_type.return_value = 'начинка'
    mock_filling.get_price.return_value = 100.0
    return mock_filling

