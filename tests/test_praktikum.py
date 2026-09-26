import runpy
from unittest.mock import patch, Mock

from praktikum.praktikum import main


class TestPraktikum:

    @patch('praktikum.praktikum.Database')
    @patch('praktikum.praktikum.Burger')
    def test_main_executes_all_actions(
        self,
        mock_burger_class,
        mock_database_class
    ):
        mock_database = Mock()
        mock_database_class.return_value = mock_database

        bun = Mock()
        ingredients = [Mock() for _ in range(6)]

        mock_database.available_buns.return_value = [bun]
        mock_database.available_ingredients.return_value = ingredients

        mock_burger = Mock()
        mock_burger.get_receipt.return_value = 'receipt'
        mock_burger_class.return_value = mock_burger

        with patch('builtins.print') as mock_print:
            main()

        mock_database.available_buns.assert_called_once()
        mock_database.available_ingredients.assert_called_once()

        mock_burger.set_buns.assert_called_once_with(bun)

        mock_burger.add_ingredient.assert_any_call(ingredients[1])
        mock_burger.add_ingredient.assert_any_call(ingredients[4])
        mock_burger.add_ingredient.assert_any_call(ingredients[3])
        mock_burger.add_ingredient.assert_any_call(ingredients[5])

        mock_burger.move_ingredient.assert_called_once_with(2, 1)
        mock_burger.remove_ingredient.assert_called_once_with(3)

        mock_burger.get_receipt.assert_called_once()
        mock_print.assert_called_once_with('receipt')

        assert mock_burger.add_ingredient.call_count == 4

    @patch('praktikum.database.Database')
    @patch('praktikum.burger.Burger')
    def test_praktikum_runs_as_main(
        self,
        mock_burger_class,
        mock_database_class
    ):
        mock_database = Mock()
        mock_database_class.return_value = mock_database

        bun = Mock()
        ingredients = [Mock() for _ in range(6)]

        mock_database.available_buns.return_value = [bun]
        mock_database.available_ingredients.return_value = ingredients

        mock_burger = Mock()
        mock_burger.get_receipt.return_value = 'receipt'
        mock_burger_class.return_value = mock_burger

        with patch('builtins.print'):
            runpy.run_module(
                'praktikum.praktikum',
                run_name='__main__'
            )

        assert mock_burger_class.called