from unittest.mock import patch
import pytest
import data


@pytest.fixture()
@patch('praktikum.bun.Bun')
def mock_bun(bun_mock):
    # фикстура, возвращающая в тест замокированный объект булки (black bun)
    mock_bun = bun_mock
    mock_bun.name, mock_bun.price, mock_bun.get_name.return_value, mock_bun.get_price.return_value = data.bun_test()
    return mock_bun


@pytest.fixture()
@patch('praktikum.ingredient.Ingredient')
def mock_ingredient_1(bun_ingredient):
    # фикстура, возвращающая в тест замокированный объект ингредиента (hot sauce)
    mock_ingredient_1 = bun_ingredient
    (mock_ingredient_1.type, mock_ingredient_1.name, mock_ingredient_1.price, mock_ingredient_1.get_type.return_value,
     mock_ingredient_1.get_name.return_value, mock_ingredient_1.get_price.return_value) = data.ingredient_1_test()
    return mock_ingredient_1


@pytest.fixture()
@patch('praktikum.ingredient.Ingredient')
def mock_ingredient_2(bun_ingredient):
    # фикстура, возвращающая в тест замокированный объект ингредиента (sausage)
    mock_ingredient_2 = bun_ingredient
    (mock_ingredient_2.type, mock_ingredient_2.name, mock_ingredient_2.price, mock_ingredient_2.get_type.return_value,
     mock_ingredient_2.get_name.return_value, mock_ingredient_2.get_price.return_value) = data.ingredient_2_test()
    return mock_ingredient_2

