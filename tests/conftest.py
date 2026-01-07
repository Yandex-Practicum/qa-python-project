"""
Общие фикстуры для тестов
"""
import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Тестовая булочка"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce_ingredient():
    """Фикстура для создания мока соуса"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "кетчуп"
    ingredient.get_price.return_value = 50.0
    return ingredient


@pytest.fixture
def mock_filling_ingredient():
    """Фикстура для создания мока начинки"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "котлета"
    ingredient.get_price.return_value = 100.0
    return ingredient


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_sauce_ingredient, mock_filling_ingredient):
    """Фикстура для создания бургера с ингредиентами"""
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce_ingredient)
    burger.add_ingredient(mock_filling_ingredient)
    return burger


@pytest.fixture
def mock_database():
    """Фикстура для создания мока базы данных"""
    database = Mock()
    
    # Создаем моки для булочек
    mock_buns = [Mock(), Mock(), Mock()]
    mock_buns[0].get_name.return_value = "black bun"
    mock_buns[0].get_price.return_value = 100.0
    
    # Создаем моки для ингредиентов
    mock_ingredients = [Mock() for _ in range(6)]
    
    # Настраиваем ингредиенты
    for i in range(3):  # Соусы
        mock_ingredients[i].get_type.return_value = "SAUCE"
        mock_ingredients[i].get_price.return_value = (i + 1) * 100.0
    
    for i in range(3, 6):  # Начинки
        mock_ingredients[i].get_type.return_value = "FILLING"
        mock_ingredients[i].get_price.return_value = (i - 2) * 100.0
    
    database.available_buns.return_value = mock_buns
    database.available_ingredients.return_value = mock_ingredients
    
    return database


@pytest.fixture
def mock_db_and_burger():
    """Фикстура для настройки общего мока базы данных и бургера"""
    from unittest.mock import Mock, patch
    
    with patch('praktikum.praktikum.Database') as mock_db_class, \
         patch('praktikum.praktikum.Burger') as mock_burger_class:

        mock_db_instance = Mock()
        mock_db_class.return_value = mock_db_instance

        mock_burger_instance = Mock()
        mock_burger_class.return_value = mock_burger_instance

        # Настройка минимально необходимых данных в БД
        mock_buns = [Mock() for _ in range(3)]
        mock_ingredients = [Mock() for _ in range(6)]
        mock_db_instance.available_buns.return_value = mock_buns
        mock_db_instance.available_ingredients.return_value = mock_ingredients

        yield mock_db_instance, mock_burger_instance