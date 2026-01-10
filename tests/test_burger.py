import pytest
from conftest import mock_bun, mock_filling, mock_sauce
from praktikum.burger import Burger
from data import TestBurgerData
import allure


@allure.suite('Тестирование класса - Burger')
class TestBurger:

    @allure.title('Проверка добавления булочки в бургер - set_buns')
    def test_set_buns_is_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка добавления ингредиентов в бургер - add_ingredient')
    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [TestBurgerData.sauce_name, TestBurgerData.sauce_name],
        [TestBurgerData.filling_name, TestBurgerData.filling_name],
        [TestBurgerData.sauce_name_2, TestBurgerData.sauce_name_2],
        [TestBurgerData.filling_name_2, TestBurgerData.filling_name_2]
    ])
    def test_add_ingredient_is_success(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @allure.title('Проверка удаления ингредиентов из бургера (соус, начинка) - remove_ingredient')
    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [TestBurgerData.sauce_name, TestBurgerData.sauce_name],
        [TestBurgerData.filling_name, TestBurgerData.filling_name]
    ])
    def test_remove_ingredient_is_success(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    @allure.title('Проверка возможности перемещения ингредиентов в бургере - move_ingredient')
    def test_move_ingredient_is_success(self, mock_filling, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_filling and len(burger.ingredients) == 2

    @allure.title('Проверка вычисления конечной стоимости всего бургера - get_price')
    def test_get_burger_price_is_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == TestBurgerData.burger_total_price

    @allure.title('Проверка получения состава и стоимости бургера - get_receipt')
    def test_get_burger_receipt_is_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус Spicy-X =\n'
                                        '= filling Говяжий метеорит (отбивная) =\n'                                        
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')