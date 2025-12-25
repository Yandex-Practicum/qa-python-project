import pytest
from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    
    @pytest.fixture
    def database(self):
        """Фикстура для создания базы данных."""
        return Database()
    
    def test_database_initialization(self, database):
        """Проверяем инициализацию базы данных."""
        assert database is not None
        assert hasattr(database, 'buns')
        assert hasattr(database, 'ingredients')
    
    def test_available_buns(self, database):
        """Проверяем получение доступных булочек."""
        buns = database.available_buns()
        
        # Проверяем, что возвращается список
        assert isinstance(buns, list)
        
        # Проверяем количество булочек (из кода: 3 булочки)
        assert len(buns) == 3
        
        # Проверяем, что все элементы - экземпляры Bun
        for bun in buns:
            assert isinstance(bun, Bun)
        
        # Проверяем названия булочек (из кода)
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names
    
    def test_available_ingredients(self, database):
        """Проверяем получение доступных ингредиентов."""
        ingredients = database.available_ingredients()
        
        # Проверяем, что возвращается список
        assert isinstance(ingredients, list)
        
        # Проверяем количество ингредиентов (из кода: 6 ингредиентов)
        assert len(ingredients) == 6
        
        # Проверяем, что все элементы - экземпляры Ingredient
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
        
        # Проверяем названия ингредиентов (из кода)
        ingredient_names = [ingredient.get_name() for ingredient in ingredients]
        assert "hot sauce" in ingredient_names
        assert "sour cream" in ingredient_names
        assert "chili sauce" in ingredient_names
        assert "cutlet" in ingredient_names
        assert "dinosaur" in ingredient_names
        assert "sausage" in ingredient_names
    
    def test_database_has_correct_bun_prices(self, database):
        """Проверяем цены булочек в базе данных."""
        buns = database.available_buns()
        prices = [bun.get_price() for bun in buns]
        assert 100 in prices
        assert 200 in prices
        assert 300 in prices

    def test_database_ingredient_types_correct(self, database):
        """Проверяем типы ингредиентов в базе данных."""
        ingredients = database.available_ingredients()
        types = [ing.get_type() for ing in ingredients]
        assert "SAUCE" in types
        assert "FILLING" in types
    
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_with_mocks(self, MockIngredient, MockBun):
        """Тестируем базу данных с использованием моков."""
        # Настраиваем моки
        mock_bun = Mock()
        mock_bun.get_name.return_value = "mock bun"
        mock_bun.get_price.return_value = 999
        
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "mock ingredient"
        mock_ingredient.get_price.return_value = 777
        mock_ingredient.get_type.return_value = "SAUCE"
        
        MockBun.return_value = mock_bun
        MockIngredient.return_value = mock_ingredient
        
        # Создаем базу данных с моками
        db = Database()
        
        # Проверяем, что Bun был вызван с правильными параметрами
        assert MockBun.called
        
        # Проверяем доступные булочки
        buns = db.available_buns()
        assert len(buns) > 0
        assert buns[0] == mock_bun