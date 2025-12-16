import allure
import pytest
from praktikum.database import Database
from data_test import DatabaseList


class TestDatabase:
    @allure.title('Проверка доступных булок для бургера')
    @allure.description('Проверяем работу метода available_buns с данными из базы')
    @pytest.mark.parametrize('name,price,index', DatabaseList.BUN_LIST)
    def test_available_buns(self, name, price, index):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert (buns[index].get_name() == name and
               buns[index].get_price() == price)

    @allure.title('Проверка доступных ингредиентов для бургера')
    @allure.description('Проверяем работу метода available_ingredients с данными из базы')
    @pytest.mark.parametrize('type_ingredient,name,price,index', DatabaseList.INGREDIENT_LIST)
    def test_available_ingredients(self, type_ingredient, name, price, index):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert (ingredients[index].get_type() == type_ingredient and
                ingredients[index].get_name() == name and
                ingredients[index].get_price() == price)