import allure
import pytest

from data import Data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger

from conftest import burger

class TestBurger:
    @allure.title('Тест на проверку успешного добавления булочки в бургер')
    def test_set_buns_successfully(self, burger):
        set_new_bun = Bun(Data.fluorescent_bun, Data.fluorescent_bun_price)
        burger.set_buns(set_new_bun)
        assert burger.bun == set_new_bun

    @allure.title('Тест на проверку успешного добавления ингредиента в бургер')
    def test_add_ingredient_successfully(self, burger):
        count_ingredient_in_burger = len(burger.ingredients)
        set_new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,
                                        Data.sause_traditional_galaxy,
                                        Data.sause_traditional_galaxy_price)
        burger.add_ingredient(set_new_ingredient)
        assert len(burger.ingredients) == count_ingredient_in_burger + 1

    @allure.title('Тест на проверку успешного удаления ингредиента в бургер')
    def test_remove_ingredient_successfully(self, burger):
        count_ingredient_in_burger = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == count_ingredient_in_burger - 1

    @allure.title('Тест на проверку успешного перемещения ингредиента в бургер')
    @pytest.mark.parametrize('from_index, to_index', [(0, 1), (1, 0)])
    def test_move_ingredient_successfully(self, burger, from_index, to_index):
        expected_result = burger.ingredients[from_index]
        burger.move_ingredient(from_index, to_index)
        assert burger.ingredients[to_index] == expected_result

    @pytest.mark.parametrize(
        "bun_price, ingredients_price, total",
        [
            (100.0, [20.0, 30.0], 250.0),
            (150.0, [40.0, 60.0], 400.0)
        ]
    )
    @allure.title('Тест на проверку успешного получения цены бургера')
    def test_get_price_successfully(self, bun_price, ingredients_price, total):
        burger = Burger()
        burger.bun = Bun(Data.fluorescent_bun, bun_price)

        for price in ingredients_price:
            burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING,
                                             Data.sause_traditional_galaxy,
                                             price))
        assert burger.get_price() == total
