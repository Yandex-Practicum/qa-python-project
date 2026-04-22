from unittest.mock import Mock
import pytest

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 100
    bun.get_name.return_value = "black bun"
    return bun

@pytest.fixture
def mock_ingredients():
    ing1 = Mock()
    ing1.get_price.return_value = 50
    ing1.get_name.return_value = "ketchup"
    ing1.get_type.return_value = "SAUCE"

    ing2 = Mock()
    ing2.get_price.return_value = 30
    ing2.get_name.return_value = "cutlet"
    ing2.get_type.return_value = "FILLING"

    return [ing1, ing2]