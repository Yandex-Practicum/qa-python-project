import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Создание mock булочки с ценой
@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "fluorescent bun"
    bun.get_price.return_value = 988
    bun.name = "fluorescent bun"
    bun.price = 988
    return bun

# Создание mock ингридиента с ценой
@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "Sauce Spicy-X"
    ingredient.get_price.return_value = 90
    ingredient.type = INGREDIENT_TYPE_SAUCE
    ingredient.name = "Sauce Spicy-X"
    ingredient.price = 90
    return ingredient

# Создание mock начинки с ценой
@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "Beef meteorite"
    ingredient.get_price.return_value = 3000
    ingredient.type = INGREDIENT_TYPE_FILLING
    ingredient.name = "Beef meteorite"
    ingredient.price = 3000
    return ingredient

# Создание mock пустого бургера
@pytest.fixture
def empty_burger():
    return Burger()


# Создание mock бургера с булочкой и начинкой
@pytest.fixture
def burger_with_one_ingredient(mock_bun, mock_ingredient_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_filling)
    return burger


# Создание mock бургера с булочкой, начинкой и соусом
@pytest.fixture
def burger_full(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger
