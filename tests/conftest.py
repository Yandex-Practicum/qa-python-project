import pytest
from tests import data


@pytest.fixture
def mock_bun():
    return data.get_mock_bun()


@pytest.fixture
def mock_ingredient_sauce():
    return data.get_mock_ingredient_sauce()


@pytest.fixture
def mock_ingredient_filling():
    return data.get_mock_ingredient_filling()


@pytest.fixture
def mock_ingredient_cheese():
    return data.get_mock_ingredient_cheese()


@pytest.fixture
def empty_burger():
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def burger_with_bun(mock_bun):
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger
