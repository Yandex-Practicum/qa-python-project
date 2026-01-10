from praktikum.burger import Burger
from data import *
import allure


class TestBurger:
    @allure.title('Проверка работы метода, добавляющего булку в бургер set_buns')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Проверка метода, добавляющего ингредиенты в бургер add_ingredient')
    @allure.description('Параметризация для трех тестов: по очереди добавление соуса и разных двух начинок')
    @pytest.mark.parametrize('ingredients, added_ingredient', [
        [Data1.sauce_name, Data1.sauce_name],
        [Data1.filling_name, Data1.filling_name],
        [Data2.filling_name, Data2.filling_name]
    ])
    def test_add_ingredient(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @allure.title('Проверка метода, удаляющего ингредиенты из бургера remove_ingredient')
    @allure.description('Параметризация для двух тестов: удаление соуса, удаление начинки')
    @pytest.mark.parametrize('ingredients, removed_ingredient', [
        [Data1.sauce_name, Data1.sauce_name],
        [Data2.filling_name, Data2.filling_name]
    ])
    def test_remove_ingredient(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    @allure.title('Проверка меода перемещения ингредиентов в бургере move_ingredient')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce

    @allure.title('Провека метода, рассчитывающего конечную стоимость бургера get_price')
    def test_get_burger_price(self, mock_bun_2, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun_2)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_price() == Data2.burger_final_cost

    @allure.title('Проверка метода получения рецепта бургера и его стоимость get_receipt')
    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling, mock_filling_2):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling_2)
        assert burger.get_receipt() == ('(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '= sauce Соус Spicy-X =\n'
                                        '= filling Мясо бессмертных моллюсков Protostomia =\n'
                                        '= filling Хрустящие минеральные кольца =\n'
                                        '(==== Флюоресцентная булка R2-D3 ====)\n'
                                        '\n'
                                        f'Price: {burger.get_price()}')