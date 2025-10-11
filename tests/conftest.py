import pytest
from unittest.mock import MagicMock


@pytest.fixture
def new_bun():
    new_bun_mock = MagicMock()
    new_bun_mock.get_name.return_value = "VeryBigMac"
    new_bun_mock.get_price.return_value = 700.0
    return new_bun_mock

@pytest.fixture
def new_ingredient_filling():
    new_filling = MagicMock()
    new_filling.get_name.return_value = "Stardust"
    new_filling.get_type.return_value = "FILLING"
    new_filling.get_price.return_value = 10.0
    return new_filling

@pytest.fixture
def new_ingredient_sauce():
    new_sauce = MagicMock()
    new_sauce.get_name.return_value = "Molten Mithril"
    new_sauce.get_type.return_value = "SAUCE"
    new_sauce.get_price.return_value = 5.0
    return new_sauce
