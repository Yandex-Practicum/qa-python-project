import pytest
from data_test import BunConstants as BC, IngredientConstants as IC
from utils import Utils


@pytest.fixture
def mock_bun():
    mock_bun = Utils.mock_bun([BC.BUN_NAME, BC.BUN_PRICE])
    return mock_bun


@pytest.fixture
def mock_sauce():
    mock_sauce = Utils.mock_ingredient([IC.SAUCE_TYPE, IC.SAUCE_NAME, IC.SAUCE_PRICE])
    return mock_sauce


@pytest.fixture
def mock_filling():
    mock_filling = Utils.mock_ingredient([IC.FILLING_TYPE, IC.FILLING_NAME, IC.FILLING_PRICE])
    return mock_filling