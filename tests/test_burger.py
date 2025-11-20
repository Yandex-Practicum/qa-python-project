import allure

import helpers
import mocks


class TestBurger:
    @allure.title('Проверка добавления булки')
    def test_set_buns_expected_bun_ok(self, burger):
        bun = mocks.mock_bun()
        burger.set_buns(bun)
        assert burger.bun == bun

    @allure.title('Проверка добавления ингредиента')
    def test_add_ingredient_one_ingredient_added(self, burger):
        helpers.add_random_ingredient(burger)
        assert len(burger.ingredients) == 1

    @allure.title('Проверка удаления ингредиента')
    def test_remove_ingredient_one_ingredient_removed(self, burger):
        helpers.add_random_ingredient(burger)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title('Проверка перемещения ингредиента')
    def test_move_ingredient_one_ingredient_moved(self, burger):
        helpers.add_random_ingredient(burger)
        first = burger.ingredients[0]
        helpers.add_random_ingredient(burger)
        second = burger.ingredients[1]
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [second, first]

    @allure.title('Проверка цены бургера')
    def test_get_price_expected_price(self, burger):
        price = helpers.burger_example(burger)[0]
        assert burger.get_price() == price

    @allure.title('Проверка чека на бургер')
    def test_get_receipt_expected_receipt(self, burger):
        receipt = helpers.burger_example_receipt(burger)
        assert burger.get_receipt() == receipt



