import pytest
from unittest.mock import patch, MagicMock

from praktikum.praktikum import main
from praktikum.burger import Burger


@patch('praktikum.praktikum.print')
@patch('praktikum.praktikum.Database')
def test_main_function(mock_database_class, mock_print):
    """Тестируем основную функцию программы"""
    # Создаем моки для булочек и ингредиентов
    mock_buns = [MagicMock(), MagicMock(), MagicMock()]
    mock_buns[0].get_name.return_value = "black bun"
    mock_buns[0].get_price.return_value = 100
    
    mock_ingredients = [MagicMock() for _ in range(6)]
    # Настраиваем моки ингредиентов
    mock_ingredients[1].get_type.return_value = "SAUCE"
    mock_ingredients[1].get_name.return_value = "sour cream"
    mock_ingredients[1].get_price.return_value = 200
    
    mock_ingredients[4].get_type.return_value = "FILLING"
    mock_ingredients[4].get_name.return_value = "dinosaur"
    mock_ingredients[4].get_price.return_value = 200
    
    mock_ingredients[3].get_type.return_value = "FILLING"
    mock_ingredients[3].get_name.return_value = "cutlet"
    mock_ingredients[3].get_price.return_value = 100
    
    mock_ingredients[5].get_type.return_value = "FILLING"
    mock_ingredients[5].get_name.return_value = "sausage"
    mock_ingredients[5].get_price.return_value = 300
    
    # Настраиваем мок базы данных
    mock_database = mock_database_class.return_value
    mock_database.available_buns.return_value = mock_buns
    mock_database.available_ingredients.return_value = mock_ingredients
    
    # Вызываем тестируемую функцию
    main()
    
    # Проверяем, что был создан экземпляр Database
    mock_database_class.assert_called_once()
    
    # Проверяем, что были вызваны методы для получения данных из базы
    mock_database.available_buns.assert_called_once()
    mock_database.available_ingredients.assert_called_once()
    
    # Проверяем, что чек был напечатан
    mock_print.assert_called_once()