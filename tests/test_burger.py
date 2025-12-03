import pytest
from unittest.mock import Mock, patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    """Создает новый бургер для каждого теста"""
    return Burger()

@pytest.fixture
def mock_bun():
    """Создает мок булочки"""
    mock = Mock()
    mock.get_price.return_value = 100
    mock.get_name.return_value = "test bun"
    return mock

@pytest.fixture  
def mock_ingredient():
    """Создает мок ингредиента"""
    mock = Mock()
    mock.get_price.return_value = 50
    mock.get_name.return_value = "test ingredient"
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock

class TestBurger:
    """Тесты для класса Burger"""
    
    def test_burger_initialization(self, burger):
        """ТЕСТ 1: Только инициализация"""
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns(self, burger, mock_bun):
        """ТЕСТ 2: Только установка булочки"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self, burger, mock_ingredient):
        """ТЕСТ 3: Только добавление ингредиента"""
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    def test_remove_ingredient(self, burger, mock_ingredient):
        """ТЕСТ 4: Только удаление ингредиента"""
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
    
    def test_move_ingredient(self, burger):
        """ТЕСТ 5: Только перемещение ингредиента"""
        mock1, mock2, mock3 = Mock(), Mock(), Mock()
        burger.ingredients = [mock1, mock2, mock3]
        
        burger.move_ingredient(2, 1)
        assert burger.ingredients == [mock1, mock3, mock2]
    
    def test_get_price(self, burger, mock_bun):
        """ТЕСТ 6: Только расчет цены"""
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        burger.ingredients = [mock_ingredient]
        
        assert burger.get_price() == 250  # 2*100 + 50
    
    def test_get_receipt(self, burger, mock_bun):
        """ТЕСТ 7: Формирование чека"""
        burger.set_buns(mock_bun)
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "test sauce"
        mock_ingredient.get_price.return_value = 50
        burger.ingredients = [mock_ingredient]
        
        receipt = burger.get_receipt()
        # ИСПРАВЛЕНИЕ: заменили "in" на полное сравнение строки
        expected_receipt = """(==== test bun ====)
= sauce test sauce =
(==== test bun ====)

Price: 250"""
        assert receipt == expected_receipt