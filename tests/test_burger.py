from praktikum.burger import Burger
from conftest import *
import pytest
import allure


class TestBurger:
    @allure.title('Проверка метода set_buns, добавляющего булку в бургер')
    def test_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка метода add_ingredient, добавляющего ингредиенты в бургер')
    @allure.description('С помощью параметризации выполняем три теста: проверяем по очереди '
                        'добавление соуса и двух разных начинок')
    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [Data1.sauce_name, Data1.sauce_name],
        [Data1.filling_name, Data1.filling_name],
        [Data2.filling_name, Data2.filling_name]
        ]
    )
    def test_add_ingredient_success(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @allure.title('Проверка метода remove_ingredient, удаляющего ингредиент из бургера')
    @allure.description('С помощью параметризации выполняем два теста: проверяем по очереди '
                        'удаление соуса и начинки')
    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [Data1.sauce_name, Data1.sauce_name],
        [Data2.filling_name, Data2.filling_name]
        ]
    )
    def test_remove_ingredient_success(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    @allure.title('Проверка метода move_ingredient, перемещающего ингредиенты в бургере')
    def test_move_ingredient_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce

    @allure.title('Проверка метода get_price, высчитывающего конечную стоимость бургера')
    def test_get_price_burger_success(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == Data2.burger_final_cost

    @allure.title('Проверка метода get_receipt, получающего рецепт собранного бургера и его стоимость')
    def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус традиционный галактический =\n'
                                        '= filling Мясо бессмертных моллюсков Protostomia =\n'
                                        '= filling Сыр с астероидной плесенью =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')
