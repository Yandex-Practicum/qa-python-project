import pytest
import allure

from praktikum import Burger, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:
    @allure.title('Проверка присвоения булочки бургеру')
    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == bun_mock.name and burger.bun.price == bun_mock.price

    @allure.title('Проверка добавления ингредиента в бургер')
    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    def test_add_ingredient(self, ingredient_mock, ingredient_type):
        ingredient_mock.type = ingredient_type
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[-1].type == ingredient_mock.type and \
               burger.ingredients[-1].name == ingredient_mock.name and \
               burger.ingredients[-1].price == ingredient_mock.price

    @allure.title('Проверка удаления ингредиента из бургерв')
    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    def test_remove_ingredient(self, ingredient_mock, ingredient_type):
        ingredient_mock.type = ingredient_type
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(-1)
        assert len(burger.ingredients) == 0

    @allure.title('Проверка перемешивания ингредиентов в бургере')
    def test_move_ingredient(self, sauce_mock, filling_mock):
        burger = Burger()
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        burger.move_ingredient(-1, 0)
        assert burger.ingredients[0] is filling_mock and burger.ingredients[1] is sauce_mock

    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    @allure.title('Проверка получения цены бургера c одним ингредиентом')
    def test_get_price_one_ingredient(self, bun_mock, ingredient_mock, ingredient_type):
        ingredient_mock.type = ingredient_type
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == bun_mock.price * 2 + ingredient_mock.price

    @allure.title('Проверка получения цены бургера c несколькими ингредиентами')
    def test_get_price(self, bun_mock, sauce_mock, filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        assert burger.get_price() == bun_mock.price * 2 + sauce_mock.price + filling_mock.price

    @pytest.mark.parametrize('ingredient_type', (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING))
    @allure.title('Проверка распечатки чека с информацией о бургере с одним ингредиентом')
    def test_get_receipt(self, bun_mock, ingredient_mock, ingredient_type):
        ingredient_mock.type = ingredient_type
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        receipt = burger.get_receipt()
        assert bun_mock.name in receipt \
               and ingredient_mock.name in receipt \
               and ingredient_type.lower() in receipt \
               and f'Price: {bun_mock.price * 2 + ingredient_mock.price}' in receipt

    @allure.title('Проверка распечатки чека с информацией о бургере с несколькими ингредиентами')
    def test_get_receipt(self, bun_mock, sauce_mock, filling_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        receipt = burger.get_receipt()
        assert bun_mock.name in receipt \
               and sauce_mock.name in receipt \
               and filling_mock.name in receipt \
               and sauce_mock.type.lower() in receipt \
               and filling_mock.type.lower() in receipt \
               and f'Price: {bun_mock.price * 2 + sauce_mock.price + filling_mock.price}' in receipt
