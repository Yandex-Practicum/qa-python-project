import pytest
import allure
from praktikum.bun import Bun
from praktikum.burger import Burger
from data import Data, Data_0

class TestBurger:
    @allure.title('Проверка работает ли метод set_buns')
    @allure.description('Проверка добавления булки в бургер')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка работает ли метод add_ingredient')
    @allure.description('Проверка добавления ингредиента(соуса/начинки в бургер')
    @pytest.mark.parametrize('ingredients, added_ingredients',
                             [[Data.sauce_name, Data.sauce_name],
                              [Data_0.sauce_name, Data_0.sauce_name],
                              [Data.filling_name, Data.filling_name],
                              [Data_0.filling_name, Data_0.filling_name]
                              ]
                             )
    def test_add_ingredient(self, ingredients, added_ingredients):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredients] and len(burger.ingredients) == 1


    @allure.title('Проверка работает ли метод remove_ingredient')
    @allure.description('Проверка удаления ингредиента(соуса/начинки из бургера')
    @pytest.mark.parametrize('ingredients, removed_ingredient',
                             [[Data.sauce_name, Data.sauce_name],
                              [Data_0.filling_name, Data_0.filling_name]
                              ]
                             )
    def test_remove_ingredient(self, mock_filling, ingredients, removed_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    @allure.title('Проверка работает ли метод move_ingredient')
    @allure.description('Проверка перемещения ингредиентов в бургере')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2 and burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce

    @allure.title('Проверка работает ли метод get_price')
    @allure.description('Проверка итоговой цены бургера')
    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == Data.burger_cost

    @allure.title('Проверка работает ли метод get_receipt')
    @allure.description('Проверка получения рецепта бургера')
    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_receipt() == ('(==== Краторная булка N-200i ====)\n'
                                        '= sauce Соус фирменный Space Sauce =\n'
                                        '= filling Говяжий метеорит (отбивная) =\n'
                                        '(==== Краторная булка N-200i ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')