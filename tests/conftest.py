import pytest
from unittest.mock import Mock

@pytest.fixture
def burger_with_mocks():
    burger = Burger()
    mock_bun = Mock()
    mock_bun.get_price.return_value = 50
    burger.set_buns(mock_bun)
    ing1 = Mock()
    ing1.get_price.return_value = 30
    ing2 = Mock()
    ing2.get_price.return_value = 20
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    return burger