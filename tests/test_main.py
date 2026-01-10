import allure
from unittest import mock

from praktikum.praktikum import main

from data import buns_mock_data, ingredients_mock_data, main_expected_result


class TestMain:
    @allure.title("Проверка полноценной сборки бургера")
    def test_main(self, capsys):
        with (
            mock.patch("praktikum.database.Database.available_buns") as mock_available_buns,
            mock.patch("praktikum.database.Database.available_ingredients") as mock_available_ingredients,
        ):
            mock_available_buns.return_value = buns_mock_data
            mock_available_ingredients.return_value = ingredients_mock_data
            main()
            txt_stdout, txt_stderr = capsys.readouterr()

            assert txt_stdout == main_expected_result