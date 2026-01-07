import pytest
from unittest.mock import Mock, patch, call
from praktikum.praktikum import main


class TestPraktikum:
    """Тестирование основного модуля программы (функции main)"""
    
    # Фикстура mock_db_and_burger теперь находится в conftest.py

    @patch('praktikum.praktikum.print')
    def test_main_calls_database_methods(self, mock_print, mock_db_and_burger):
        """Проверка, что main обращается к базе данных за булками и ингредиентами"""
        mock_db_instance, _ = mock_db_and_burger
        main()
        mock_db_instance.available_buns.assert_called_once()
        mock_db_instance.available_ingredients.assert_called_once()

    @patch('praktikum.praktikum.print')
    def test_main_assembles_burger_with_correct_ingredients(self, mock_print, mock_db_and_burger):
        """Проверка, что в бургер устанавливаются правильные компоненты из базы"""
        mock_db_instance, mock_burger_instance = mock_db_and_burger
        mock_buns = mock_db_instance.available_buns.return_value
        mock_ingredients = mock_db_instance.available_ingredients.return_value

        main()

        # Проверяем установку булки (индекс 0)
        mock_burger_instance.set_buns.assert_called_once_with(mock_buns[0])
        # Проверяем добавление ингредиентов (индексы 1, 4, 3, 5)
        expected_calls = [call(mock_ingredients[1]), call(mock_ingredients[4]), 
                          call(mock_ingredients[3]), call(mock_ingredients[5])]
        mock_burger_instance.add_ingredient.assert_has_calls(expected_calls)

    @patch('praktikum.praktikum.print')
    def test_main_modifies_burger_structure(self, mock_print, mock_db_and_burger):
        """Проверка, что main вызывает методы перемещения и удаления ингредиентов"""
        _, mock_burger_instance = mock_db_and_burger
        main()
        mock_burger_instance.move_ingredient.assert_called_once_with(2, 1)
        mock_burger_instance.remove_ingredient.assert_called_once_with(3)

    @patch('praktikum.praktikum.print')
    def test_main_prints_receipt(self, mock_print, mock_db_and_burger):
        """Проверка, что main получает чек и выводит его в консоль"""
        _, mock_burger_instance = mock_db_and_burger
        mock_receipt = "Test Receipt"
        mock_burger_instance.get_receipt.return_value = mock_receipt

        main()

        mock_burger_instance.get_receipt.assert_called_once()
        mock_print.assert_called_once_with(mock_receipt)