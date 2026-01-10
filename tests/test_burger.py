import pytest
import allure
from praktikum.database import Database
from helpers import Data


class TestBurger:
    @allure.title('Проверяем добавление булки в бургер')
    @pytest.mark.parametrize('bun_name', [Data.WHITE_BUN, Data.RED_BUN, Data.BLACK_BUN])
    def test_set_bun(self, burger, bun_name):
        burger.set_buns(bun_name)

        assert burger.bun == bun_name

    @allure.title('Проверяем добавление в бургер 1 ингредиента')
    def test_add_one_ingredient(self, burger):
        burger.add_ingredient(Data.SOUR_CREAM)

        assert len(burger.ingredients) == 1

    @allure.title('Проверяем добавление в бургер 2х ингредиентов')
    def test_add_two_ingredients(self, burger):
        burger.add_ingredient(Data.CUTLET)
        burger.add_ingredient(Data.CHILI_SAUCE)

        assert len(burger.ingredients) == 2

    @allure.title('Проверяем удаление ингредиента из бургера')
    def test_remove_ingredient(self, burger):
        burger.add_ingredient(Data.SAUSAGE)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    @allure.title('Проверяем изменение ингредиентов местами по индексу')
    def test_move_ingredient(self, burger):
        burger.add_ingredient(Data.RED_BUN)
        burger.add_ingredient(Data.CUTLET)
        burger.move_ingredient(1, 0)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == Data.CUTLET and burger.ingredients[1] == Data.RED_BUN

    @allure.title('Проверяем получение стоимости бургера')
    def test_get_burger_price(self, burger):
        data = Database()
        burger.set_buns(data.available_buns()[1])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[3])

        assert burger.get_price() == 600

    @allure.title('Проверяем получение чека')
    def test_get_billing_cheque(self, burger):
        data = Database()
        burger.set_buns(data.available_buns()[0])
        burger.add_ingredient(data.available_ingredients()[0])
        burger.add_ingredient(data.available_ingredients()[1])
        burger.add_ingredient(data.available_ingredients()[2])

        assert burger.get_receipt() == Data.RECEIPT_TEXT
