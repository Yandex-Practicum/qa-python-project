import allure
from unittest import mock
from praktikum.database import Database


class TestDatabase:
    """
    ТЕСТЫ МЕТОДОВ КЛАССА Database
    """

    @allure.title('available_buns() - список доступных булочек')
    @allure.description('Проверяем, что выводится список доступных булочек')
    def test_available_buns(self):
        database = Database()
        mock_buns = [mock.Mock(name='Сырная'), mock.Mock(name='Злаковая'), mock.Mock(name='С кунжутом')]
        database.available_buns = mock.Mock(return_value=mock_buns)
        assert database.available_buns() == mock_buns

    @allure.title('available_buns() -список доступных ингредиентов')
    @allure.description('Проверяем, что выводится список доступных игредиентов')
    def test_available_ingredients(self):
        database = Database()
        mock_ingredients = [mock.Mock(name="Котлета"), mock.Mock(name="Сыр"), mock.Mock(name="Огурец"),
                            mock.Mock(name="Горчица"), mock.Mock(name="Салат"), mock.Mock(name="Кетчуп")]
        database.available_ingredients = mock.Mock(return_value=mock_ingredients)
        assert database.available_ingredients() == mock_ingredients
