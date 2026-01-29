import pytest
from unittest.mock import Mock

from Diplom_1.data import DataForTests
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture(scope='function')
def bun():
    return Bun(DataForTests.BLACK_BUN, DataForTests.PRICE_BLACK_BUN)


@pytest.fixture(scope='function')
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, DataForTests.CHILI_SAUSE, DataForTests.PRICE_CHILI_SAUSE)


@pytest.fixture(scope='function')
def mock():
    return Mock()
