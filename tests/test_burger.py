import allure

from praktikum.burger import Burger
from conftests import *

class TestBurger:
    @allure.title('Проверка добавления булки в бургер')
    def test_add_bun(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == bun_mock.name

    @allure.title('Проверка добавления ингредиента в бургер')
    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[0].name == ingredient_mock.name

    @allure.title('Проверка удаления ингредиента из бургера')
    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title('Проверка перемещения ингредиента')
    def test_move_ingredient(self, ingredient_mock, sauce_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(sauce_mock)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].get_name() == sauce_mock.name and len(burger.ingredients) == 2

    @allure.title('Проверка подсчёта цены бургера')
    def test_get_price(self, bun_mock, ingredient_mock, sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(sauce_mock)
        final_price = burger.get_price() # 10*2 + 30 + 20 = 70
        assert final_price == 70

    @allure.title('Проверка корректного формирования чека')
    def test_get_receipt(self, bun_mock, ingredient_mock, sauce_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(sauce_mock)
        receipt = burger.get_receipt()
        result = (
            '(==== Булка ====)\n'
            '= filling Котлета =\n'
            '= sauce Соус =\n'
            '(==== Булка ====)\n'
            '\n'
            'Price: 70.0'
        )
        assert result == receipt
