import allure
from praktikum.database import Database
from unittest.mock import Mock

class TestDataBase:

    @allure.title('Проверка доступности булок')
    def test_available_buns(self):

        d_base = Database()
        mock_base_bun = Mock()
        mock_base_bun2 = Mock()

        mock_base_bun.get_name.return_value = 'Космо Булка'
        mock_base_bun.get_price.return_value = 1.0

        mock_base_bun2.get_name.return_value = 'Космо Булка 2'
        mock_base_bun2.get_price.return_value = 2.0

        d_base.buns = [mock_base_bun, mock_base_bun2]
        result_list = d_base.available_buns()

        assert len(result_list) == 2 and result_list[0].get_name() == 'Космо Булка' and result_list[1].get_name() == 'Космо Булка 2'


    @allure.title('Проверка доступности ингредиентов')
    def test_available_ingredients(self):

        d_base = Database()
        mock_base_ingrit = Mock()
        mock_base_ingrit2 = Mock()

        mock_base_ingrit.get_name.return_value = 'Тот самый соус'
        mock_base_ingrit.get_price.return_value = 2.0

        mock_base_ingrit2.get_name.return_value = 'Самый сырный соус'
        mock_base_ingrit2.get_price.return_value = 2.0

        d_base.buns = [mock_base_ingrit, mock_base_ingrit2]

        result_list = d_base.available_buns()

        assert len(result_list) == 2 and result_list[0].get_name() == 'Тот самый соус' and result_list[
            1].get_name() == 'Самый сырный соус'



