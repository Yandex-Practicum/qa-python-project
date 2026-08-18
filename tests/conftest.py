# tests/conftest.py
import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    # Фикстура для мока булочки

    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredients():
    # Фикстура для моков ингредиентов

    ing1 = Mock()
    ing1.get_name.return_value = "hot sauce"
    ing1.get_price.return_value = 100
    ing1.get_type.return_value = "SAUCE"

    ing2 = Mock()
    ing2.get_name.return_value = "cutlet"
    ing2.get_price.return_value = 150
    ing2.get_type.return_value = "FILLING"

    ing3 = Mock()
    ing3.get_name.return_value = "sour cream"
    ing3.get_price.return_value = 200
    ing3.get_type.return_value = "SAUCE"

    return [ing1, ing2, ing3]