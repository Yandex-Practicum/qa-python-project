from unittest.mock import Mock
import pytest
import pytest_cov
import allure
from praktikum.ingredient import Ingredient

class TestBurger:
    @allure.story('Установка булочки')
    def test_set_buns(self, burger_fixture, mock_bun):
        burger_fixture.set_buns(mock_bun)
        assert burger_fixture.bun == mock_bun

    @allure.step("установка ингредиента")
    def test_add_ingredient(self,burger_fixture, mock_ingredient):
        burger_fixture.add_ingredient(mock_ingredient)
        assert len(burger_fixture.ingredients) == 1
        assert burger_fixture.ingredients[0] == mock_ingredient

    @allure.story('Удаление ингредиентов')
    def test_remove_ingredient(self,burger_fixture, mock_ingredient):
        burger_fixture.add_ingredient(mock_ingredient)
        burger_fixture.remove_ingredient(0)
        assert len(burger_fixture.ingredients) == 0

    @allure.story('Перемещение ингредиентов')
    def test_move_ingredient(self,burger_fixture, mock_ingredient):
        burger_fixture.add_ingredient(mock_ingredient)
        new_ingredient = Mock(spec=Ingredient)
        new_ingredient.get_name.return_value = "Соус"
        burger_fixture.add_ingredient(new_ingredient)

        burger_fixture.move_ingredient(0, 1)
        assert burger_fixture.ingredients[0] == new_ingredient
        assert burger_fixture.ingredients[1] == mock_ingredient

    @allure.story('Расчёт цены')
    def test_get_price(self, burger_fixture, mock_bun, mock_ingredient):
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient)
        price = burger_fixture.get_price()
        assert price == 1.5 * 2 + 0.5

    @allure.story('Генерация чека')
    def test_get_receipt(self, burger_fixture, mock_bun, mock_ingredient):
        burger_fixture.set_buns(mock_bun)
        burger_fixture.add_ingredient(mock_ingredient)
        receipt = burger_fixture.get_receipt()
        assert (f'(==== {mock_bun.get_name()} ====)' + '\n' + f'= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =' + '\n' + f'(==== {mock_bun.get_name()} ====)' + '\n' + '\n' + f'Price: {burger_fixture.get_price()}') == burger_fixture.get_receipt()

