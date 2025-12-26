import pytest
from unittest.mock import Mock
from burger import Burger
from data import BurgerComponents as BC



# Создаем объект класса Burger
@pytest.fixture
def burger():
    burger = Burger()
    return burger

# Cоздаем мок чёрной булочки
@pytest.fixture()
def mock_black_bun():
    mock_black_bun = Mock()
    mock_black_bun.name = BC.BUN_NAME_1
    mock_black_bun.price = BC.BUN_PRICE_1
    mock_black_bun.get_name.return_value = BC.BUN_NAME_1
    mock_black_bun.get_price.return_value = BC.BUN_PRICE_1
    return mock_black_bun

# Создаем мок соуса 1 (острый соус)
@pytest.fixture
def mock_sauce_1():
    mock_sauce = Mock()
    mock_sauce.type = BC.INGREDIENT_TYPE_1
    mock_sauce.name = BC.SAUCE_NAME_1
    mock_sauce.price = BC.SAUCE_PRICE_1
    mock_sauce.get_price.return_value = BC.SAUCE_PRICE_1
    mock_sauce.get_name.return_value = BC.SAUCE_NAME_1
    mock_sauce.get_type.return_value = BC.INGREDIENT_TYPE_1
    return mock_sauce

# Создаем мок соуса 2 (сметана)
@pytest.fixture
def mock_sauce_2():
    mock_sauce = Mock()
    mock_sauce.type = BC.INGREDIENT_TYPE_1
    mock_sauce.name = BC.SAUCE_NAME_2
    mock_sauce.price = BC.SAUCE_PRICE_2
    mock_sauce.get_price.return_value = BC.SAUCE_PRICE_2
    mock_sauce.get_name.return_value = BC.SAUCE_NAME_2
    mock_sauce.get_type.return_value = BC.INGREDIENT_TYPE_1
    return mock_sauce

# Создаем мок соуса 3 (чили-соус)
@pytest.fixture
def mock_sauce_3():
    mock_sauce = Mock()
    mock_sauce.type = BC.INGREDIENT_TYPE_1
    mock_sauce.name = BC.SAUCE_NAME_3
    mock_sauce.price = BC.SAUCE_PRICE_3
    mock_sauce.get_price.return_value = BC.SAUCE_PRICE_3
    mock_sauce.get_name.return_value = BC.SAUCE_NAME_3
    mock_sauce.get_type.return_value = BC.INGREDIENT_TYPE_1
    return mock_sauce

# Создаем мок начинки 1 (котлета)
@pytest.fixture
def mock_filling_1():
    mock_filling = Mock()
    mock_filling.type = BC.INGREDIENT_TYPE_2
    mock_filling.name = BC.FILLING_NAME_1
    mock_filling.price = BC.FILLING_PRICE_1
    mock_filling.get_price.return_value = BC.FILLING_PRICE_1
    mock_filling.get_name.return_value = BC.FILLING_NAME_1
    mock_filling.get_type.return_value = BC.INGREDIENT_TYPE_2
    return mock_filling

# Создаем мок начинки 2 (динозавр)
@pytest.fixture
def mock_filling_2():
    mock_filling = Mock()
    mock_filling.type = BC.INGREDIENT_TYPE_2
    mock_filling.name = BC.FILLING_NAME_2
    mock_filling.price = BC.FILLING_PRICE_2
    mock_filling.get_price.return_value = BC.FILLING_PRICE_2
    mock_filling.get_name.return_value = BC.FILLING_NAME_2
    mock_filling.get_type.return_value = BC.INGREDIENT_TYPE_2
    return mock_filling

# Создаем мок начинки 3 (сосиска)
@pytest.fixture
def mock_filling_3():
    mock_filling = Mock()
    mock_filling.type = BC.INGREDIENT_TYPE_2
    mock_filling.name = BC.FILLING_NAME_3
    mock_filling.price = BC.FILLING_PRICE_3
    mock_filling.get_price.return_value = BC.FILLING_PRICE_3
    mock_filling.get_name.return_value = BC.FILLING_NAME_3
    mock_filling.get_type.return_value = BC.INGREDIENT_TYPE_2
    return mock_filling





