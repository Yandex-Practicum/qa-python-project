from unittest.mock import Mock
from praktikum.burger import Burger
import allure
import pytest


class TestBurger:
    @allure.title('Успешное добавление булки для бургера')
    def test_set_buns(self, mock_bun):
        burg = Burger()
        burg.set_buns(mock_bun)
        assert burg.bun == mock_bun

    @allure.title("Успешное добвление начинки в бургер")
    def test_add_ingredient(self, mock_ingredient):
        burg = Burger()
        burg.add_ingredient(mock_ingredient)
        assert burg.ingredients[0] == mock_ingredient

    @allure.title("Успешное удаление ингредиента бургера")
    def test_remove_ingredient(self, mock_ingredient):
        burg = Burger()
        burg.add_ingredient(mock_ingredient)
        burg.remove_ingredient(0)
        assert len(burg.ingredients) == 0

    @allure.title("Успешное перемещение ингредиентов бургера ")
    def test_move_ingredient(self, mock_ingredient):
        burg = Burger()
        burg.ingredients =[Mock(),mock_ingredient]
        burg.move_ingredient(1,0)
        assert burg.ingredients[0] == mock_ingredient

    @allure.title("Успешное получение цены при разной стоимости продуктов")
    @pytest.mark.parametrize("bun_price, ingredient_price, expected_price",[(50,100,200), (60,110,230),(70,120,260)])
    def test_get_price(self, mock_bun, mock_ingredient, bun_price, ingredient_price,expected_price):
        burg =Burger()
        burg.set_buns(mock_bun)
        burg.add_ingredient(mock_ingredient)
        expected_result = burg.get_price()
        actual_price = burg.get_price()
        assert expected_result == actual_price

    @allure.title("Успешный чек  с названием булки, ингридиентов и цены")
    def test_get_recept(self, mock_bun, mock_ingredient):
        burg = Burger()
        burg.set_buns(mock_bun)
        burg.add_ingredient(mock_ingredient)
        expected_result = '(==== big_bun ====)\n= filling x_ingredient =\n(==== big_bun ====)\n\nPrice: 343'
        actual_result = burg.get_receipt()
        assert actual_result == expected_result
