from praktikum.burger import Burger
from conftest import *
import allure
import pytest



class TestBurger:
    @allure.title('Проверка метода set_buns, который добавляет булочку в бургер')
    def test_set_buns_checking_the_addition_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка метода add_ingredient, который добавляет ингредиенты в бургер')
    @allure.description('Выполняем три теста - проверяем добавление соуса, и двух разных начинок')
    @pytest.mark.parametrize('ingredients, added_ingredient',[
        [BunData1.sauce_name, BunData1.sauce_name],
        [BunData1.filling_name, BunData1.filling_name],
        [BunData2.filling_name, BunData2.filling_name]
        ]
    )
    def test_add_ingredient_checking_the_addition_success(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @allure.title('Проверка метода remove_ingredient, который удаляет ингредиенты из бургера')
    @allure.description('Выполняем два теста - удаление соуса, и начинки')
    @pytest.mark.parametrize('ingredients, removed_ingredient',[
        [BunData1.sauce_name, BunData1.sauce_name],
        [BunData2.filling_name, BunData2.filling_name]
        ]
    )
    def test_remove_ingredient_checking_for_deletion_success(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    @allure.title('Проверка метода move_ingredient, который перемещает ингредиенты в бургере')
    def test_move_ingredient_checking_the_movement_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] ==mock_sauce

    @allure.title('Проверка метода get_price, который получает цену бургера')
    def test_get_price_check_the_price_burger_success(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == BunData2.burger_final_cost

    @allure.title('Проверка метода get_receipt, который получает рецепт и цену бургера')
    def test_get_receipt_checking_receipt_success(self, mock_bun, mock_sauce, mock_filling, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус традиционный галактический =\n'
                                        '= filling Говяжий метеорит (отбивная) =\n'
                                        '= filling Филе Люминисцентного тетраодонтимформа =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')


