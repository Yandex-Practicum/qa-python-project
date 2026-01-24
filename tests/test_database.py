from praktikum.database import Database
import pytest
from unittest.mock import Mock, patch

class TestDatabase:
    @patch('praktikum.bun.Bun')
    @pytest.mark.parametrize('name,price', [['black bun', 100], ['white bun', 200], ['red bun', 300]])
    def test_database_init_for_buns(self,mock_bun_class,name,price):
        mock_bun = Mock()
        mock_bun.name = name
        mock_bun.price = price
        mock_bun_class.return_value = mock_bun
        data = Database()
        assert any(bun.name == name and bun.price == price for bun in data.buns)
    @patch('praktikum.ingredient.Ingredient')
    @pytest.mark.parametrize('type,name,price',[['SAUCE','hot sauce',100],['SAUCE','sour cream',200],['SAUCE','chili sauce',300]])
    def test_database_init_for_ingredient_type_sauce(self,mock_ingredient_class,type,name,price):
        mock_ingredient = Mock()
        mock_ingredient.type = type
        mock_ingredient.name = name
        mock_ingredient.price = price
        mock_ingredient_class.return_value = mock_ingredient
        data = Database()
        assert any(ingredient.name == name and ingredient.price == price and ingredient.type == type for ingredient in data.ingredients)
    @patch('praktikum.ingredient.Ingredient')
    @pytest.mark.parametrize('type,name,price', [['FILLING','cutlet', 100], ['FILLING','dinosaur', 200], ['FILLING','sausage', 300]])
    def test_database_init_for_ingredient_type_filling(self, mock_ingredient_class, type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.type = type
        mock_ingredient.name = name
        mock_ingredient.price = price
        mock_ingredient_class.return_value = mock_ingredient
        data = Database()
        assert any(ingredient.type == type and ingredient.name == name and ingredient.price == price for ingredient in data.ingredients)
    @patch('praktikum.bun.Bun')
    @pytest.mark.parametrize('name,price', [['black bun', 100], ['white bun', 200], ['red bun', 300]])
    def test_available_buns_returns_available_buns(self,mock_bun_class,name,price):
        mock_bun = Mock()
        mock_bun.name = name
        mock_bun.price = price
        mock_bun_class.return_value = mock_bun
        data = Database()
        list = data.available_buns()
        assert any(bun.name == name and bun.price == price for bun in list)
    @patch('praktikum.ingredient.Ingredient')
    @pytest.mark.parametrize('type,name,price',[['SAUCE', 'hot sauce', 100], ['SAUCE', 'sour cream', 200], ['SAUCE', 'chili sauce', 300],['FILLING','cutlet', 100], ['FILLING','dinosaur', 200], ['FILLING','sausage', 300]])
    def test_available_ingredients_returns_available_ingredients(self,mock_ingredient_class,type,name,price):
        mock_ingredient = Mock()
        mock_ingredient.type = type
        mock_ingredient.name = name
        mock_ingredient.price = price
        mock_ingredient_class.return_value = mock_ingredient
        data = Database()
        list = data.available_ingredients()
        assert any(ingredient.type == type and ingredient.name == name and ingredient.price == price for ingredient in list)





