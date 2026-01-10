import pytest
from unittest.mock import create_autospec
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.database import Database

# Фикстура для создания тестового объекта Bun
@pytest.fixture
def test_bun():
    return Bun(name="Kratorskaya", price=1255)

# Фикстура для создания мок-объекта Bun
@pytest.fixture
def mock_bun():
    mock_bun = create_autospec(Bun, instance=True)
    mock_bun.get_name.return_value = "Sesame Bun"
    mock_bun.get_price.return_value = 1.5
    return mock_bun

# Фикстура для создания мок-объекта Ingredient
@pytest.fixture
def mock_ingredient():
    mock_ingredient = create_autospec(Ingredient, instance=True)
    mock_ingredient.get_name.return_value = "Lettuce"
    mock_ingredient.get_type.return_value = "topping"
    mock_ingredient.get_price.return_value = 1
    return mock_ingredient

# Фикстура для создания объекта Burger с одним ингредиентом
@pytest.fixture
def burger(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger

# Фикстура для создания объекта Burger с несколькими ингредиентами
@pytest.fixture
def burger_with_ingredients(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)

    ingredient_1 = create_autospec(Ingredient, instance=True)
    ingredient_1.get_name.return_value = "Lettuce"
    ingredient_1.get_type.return_value = "topping"
    ingredient_1.get_price.return_value = 0.5
    burger.add_ingredient(ingredient_1)

    ingredient_2 = create_autospec(Ingredient, instance=True)
    ingredient_2.get_name.return_value = "Tomato"
    ingredient_2.get_type.return_value = "filling"
    ingredient_2.get_price.return_value = 0.75
    burger.add_ingredient(ingredient_2)

    ingredient_3 = create_autospec(Ingredient, instance=True)
    ingredient_3.get_name.return_value = "Cheese"
    ingredient_3.get_type.return_value = "filling"
    ingredient_3.get_price.return_value = 1.0
    burger.add_ingredient(ingredient_3)

    return burger

# Фикстура для создания объекта Database
@pytest.fixture
def database():
    return Database()

# Фикстура для создания тестового объекта Ingredient
@pytest.fixture
def ingredient():
    return Ingredient("filling", "Tomato", 0.75)

# Фикстура для создания тестового объекта Ingredient с типом "sauce"
@pytest.fixture
def sauce():
    return Ingredient("sauce", "Ketchup", 1.0)



