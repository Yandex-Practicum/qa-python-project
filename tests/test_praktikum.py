import pytest
from unittest.mock import patch, Mock
from praktikum.praktikum import main


class TestPraktikum:
    def test_main_prints_receipt(self, capsys):
        """Проверяет, что main() выводит рецепт через print()"""
        # Мокаем зависимости
        with patch('praktikum.praktikum.Database') as mock_db, \
                patch('praktikum.praktikum.Burger') as mock_burger:
            # Настраиваем моки
            mock_bun = Mock()
            mock_ingredient = Mock()

            mock_db.return_value.available_buns.return_value = [mock_bun]
            mock_db.return_value.available_ingredients.return_value = [mock_ingredient] * 6

            mock_burger.return_value.get_receipt.return_value = "Test receipt"

            # Вызываем main()
            from praktikum.praktikum import main
            main()

            # Проверяем вывод
            captured = capsys.readouterr()
            assert "Test receipt" in captured.out

    def test_main_workflow(self):
        """Проверяет основной workflow функции main"""
        with patch('praktikum.praktikum.Database') as mock_db, \
                patch('praktikum.praktikum.Burger') as mock_burger:
            mock_bun = Mock()
            mock_ingredient = Mock()

            mock_db.return_value.available_buns.return_value = [mock_bun]
            mock_db.return_value.available_ingredients.return_value = [mock_ingredient] * 6

            main()

            # Проверяем вызовы методов
            mock_burger.return_value.set_buns.assert_called_once_with(mock_bun)
            assert mock_burger.return_value.add_ingredient.call_count == 4
            mock_burger.return_value.move_ingredient.assert_called_once()
            mock_burger.return_value.remove_ingredient.assert_called_once()

    def test_main_with_empty_database(self):
        """Проверяем обработку пустой базы данных"""
        with patch('praktikum.praktikum.Database') as mock_db:
            mock_db.return_value.available_buns.return_value = []
            mock_db.return_value.available_ingredients.return_value = []

            from praktikum.praktikum import main
            with pytest.raises(IndexError):
                main()
