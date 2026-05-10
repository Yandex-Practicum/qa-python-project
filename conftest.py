import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun_mock():
    mock = Mock(Bun)
    mock.get_name.return_value = "Флюоресцентная булка R2-D3"
    mock.get_price.return_value = 988
    return mock

@pytest.fixture
def ingredient_mock():
    mock = Mock(Ingredient)
    mock.get_name.return_value = "Хрустящие минеральные кольца"
    mock.get_price.return_value = 300
    mock.get_type.return_value = "FILLING"
    return mock
