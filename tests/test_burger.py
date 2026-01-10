from praktikum.burger import Burger
import pytest
import allure
from conftest import *
class TestBurger():

    @allure.title('Проверка метода set_buns')
    def test_set_buns_works_correctly(self, mock_bun_one):
        burger = Burger()
        burger.set_buns(mock_bun_one)
        assert burger.bun == mock_bun_one

    @allure.title('Проверка метода add_ingredient')
    @pytest.mark.parametrize('ingredients, added_ingredients', [
                            [DataOne.SAUCE_NAME, DataOne.SAUCE_NAME],
                            [DataOne.FILLING_NAME, DataOne.FILLING_NAME],
                            [DataTwo.FILLING_NAME, DataTwo.FILLING_NAME]
    ])
    def test_add_ingredient_works_correctly (self, ingredients, added_ingredients):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredients] and len(burger.ingredients) == 1

    @allure.title('Проверка метода remove_ingredient')
    @pytest.mark.parametrize('ingredients, remove_ingredients', [
                            [DataOne.SAUCE_NAME, DataOne.SAUCE_NAME],
                            [DataTwo.FILLING_NAME, DataTwo.FILLING_NAME]
    ])
    def test_remove_ingredient_works_correctly(self, ingredients, remove_ingredients):
        burger = Burger()
        burger.add_ingredient(mock_filling_one)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert remove_ingredients not in burger.ingredients and mock_filling_one in burger.ingredients

    @allure.title('Проверка метода move_ingredient')
    def test_move_ingredient_works_correctly(self, mock_sauce_one, mock_filling_one):
        burger = Burger()
        burger.add_ingredient(mock_sauce_one)
        burger.add_ingredient(mock_filling_one)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling_one
        assert burger.ingredients[1] == mock_sauce_one

    @allure.title('Проверка метода get_price')
    def test_get_price_burger_works_correctly(self, mock_bun_two, mock_sauce_two, mock_filling_two):
        burger = Burger()
        burger.set_buns(mock_bun_two)
        burger.add_ingredient(mock_sauce_two)
        burger.add_ingredient(mock_filling_two)
        assert burger.get_price() == DataTwo.BURGER_PRICE

    @allure.title('get_receipt')
    def test_get_receipt_burger_works_correctly(self, mock_bun_one, mock_sauce_one, mock_filling_one, mock_filling_two):
        burger = Burger()
        burger.set_buns(mock_bun_one)
        burger.add_ingredient(mock_sauce_one)
        burger.add_ingredient(mock_filling_one)
        burger.add_ingredient(mock_filling_two)

        reciept = (
        '(==== Флюоресцентная булка R2-D3 ====)\n'
        '= sauce Соус Spicy-X =\n'
        '= filling Мясо бессмертных моллюсков Protostomia =\n'
        '= filling Сыр с астероидной плесенью =\n'
        '(==== Флюоресцентная булка R2-D3 ====)\n'
        '\n'
        f'Price: {burger.get_price()}'
    )

        assert burger.get_receipt() == reciept

