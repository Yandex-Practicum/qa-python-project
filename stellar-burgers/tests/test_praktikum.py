import pytest
from unittest.mock import patch, Mock
import io
from praktikum.praktikum import main
from data import (
    TEST_EXPECTED_TOTAL,
)


class TestPraktikum:
    """Тестовый класс для основного модуля."""

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    @patch('builtins.print')
    def test_main_function_executes_complete_flow(self, mock_print, mock_burger_class, mock_database_class):
        """Тест функция main выполняет полный поток создания бургера."""
        mock_database = Mock()
        mock_burger = Mock()
        
        mock_buns = [Mock() for _ in range(3)]
        mock_ingredients = [Mock() for _ in range(6)]

        mock_database.available_buns.return_value = mock_buns
        mock_database.available_ingredients.return_value = mock_ingredients
        mock_burger.get_receipt.return_value = "Тестовый чек бургера"

        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        # Проверки
        mock_database_class.assert_called_once()
        mock_burger_class.assert_called_once()
        mock_database.available_buns.assert_called_once()
        mock_database.available_ingredients.assert_called_once()
        mock_burger.set_buns.assert_called_once_with(mock_buns[0])
        mock_burger.move_ingredient.assert_called_once_with(2, 1)
        mock_burger.remove_ingredient.assert_called_once_with(3)
        mock_burger.get_receipt.assert_called_once()
        mock_print.assert_called_once_with("Тестовый чек бургера")

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    def test_main_uses_correct_ingredient_indices(self, mock_burger_class, mock_database_class):
        """Тест проверяет правильное использование индексов ингредиентов."""
        mock_database = Mock()
        mock_burger = Mock()
        mock_ingredients = [Mock() for _ in range(6)]
        mock_database.available_ingredients.return_value = mock_ingredients
        mock_database.available_buns.return_value = [Mock()]
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        expected_calls = [
            ((mock_ingredients[1],),),
            ((mock_ingredients[4],),),
            ((mock_ingredients[3],),),
            ((mock_ingredients[5],),),
        ]

        assert mock_burger.add_ingredient.call_args_list == expected_calls

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    @patch('builtins.print')
    def test_main_execution_flow_order(self, mock_print, mock_burger_class, mock_database_class):
        """Тест проверяет порядок выполнения операций."""
        mock_database = Mock()
        mock_burger = Mock()
        mock_database.available_buns.return_value = [Mock()]
        mock_database.available_ingredients.return_value = [Mock() for _ in range(6)]
        mock_burger.get_receipt.return_value = "Чек"
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        assert mock_database_class.called
        assert mock_burger_class.called
        assert mock_database.available_buns.called
        assert mock_database.available_ingredients.called
        assert mock_burger.set_buns.called

    def test_main_module_can_be_imported_and_has_main_function(self):
        """Тест: модуль можно импортировать и он содержит функцию main."""
        from praktikum import praktikum
        assert hasattr(praktikum, 'main')
        assert callable(praktikum.main)

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_prints_to_stdout(self, mock_stdout, mock_burger_class, mock_database_class):
        """Тест проверяет, что main печатает результат в stdout."""
        mock_database = Mock()
        mock_burger = Mock()
        mock_database.available_buns.return_value = [Mock()]
        mock_database.available_ingredients.return_value = [Mock() for _ in range(6)]
        mock_burger.get_receipt.return_value = f"Цена: {TEST_EXPECTED_TOTAL}"
        mock_database_class.return_value = mock_database
        mock_burger_class.return_value = mock_burger

        main()

        assert f"{TEST_EXPECTED_TOTAL}" in mock_stdout.getvalue()
