from typing import List

import allure
import pytest

from praktikum.burger import Burger


class TestBurger:
    @allure.title('Создание класса бургер - пустая булочка')
    def test_create_burger_empty_bun(self):
        burger = Burger()
        assert burger.bun is None, f'Элемент {burger.bun} не пустой'

    @allure.title('Создание класса бургер - пустой список ингридиентов')
    def test_create_burger_empty_list(self):
        burger = Burger()
        assert len(burger.ingredients) == 0, f'Список {burger.ingredients} не пустой'
        assert isinstance(burger.ingredients, list), f'Элемент {burger.ingredients} не является списком'

    @allure.title('Проверка установки булочки')
    @pytest.mark.parametrize('new_bun', ('Булочка с кокосовой стружкой', '', None, 2312))
    def test_set_buns(self, new_bun):
        burger = Burger()
        burger.set_buns(new_bun)
        assert burger.bun == new_bun, f'{burger.bun} не соответствует {new_bun}'

    @allure.title('Проверка добавления ингридиентов')
    @pytest.mark.parametrize('new_ingredient', ('Лосось', '', None, 7771))
    def test_add_ingredient(self, new_ingredient):
        burger = Burger()
        new_ingredient = 'Лосось'
        burger.add_ingredient(new_ingredient)
        assert len(burger.ingredients) == 1, f'Список {burger.ingredients} не равен 1'
        assert burger.ingredients == [new_ingredient], f'Список {burger.ingredients} не соответствует {[new_ingredient]}'

    @allure.title('Проверка удаления ингридиентов')
    def test_remove_ingredient(self):
        burger = Burger()
        new_ingredient = 'Лосось'
        burger.add_ingredient(new_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) != 1, f'В списке {burger.ingredients} не удалён ингридиент'

    @allure.title('Проверка перемещения ингридиентов')
    def test_move_ingredient(self):
        burger = Burger()
        new_ingredient = 'Лосось'
        for i in range(0,4):
            if i == 0:
                burger.add_ingredient(new_ingredient)
            else:
                burger.add_ingredient(new_ingredient + f'{i}')
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2] == new_ingredient, f'В списке {burger.ingredients} элемент не перемещен'

    @allure.title('Проверка получения стоимости')
    @pytest.mark.parametrize('expect_price', (1300, 800))
    def test_get_price(self, mock_bun, mock_ingredient, expect_price):
        burger = Burger()
        burger.set_buns(mock_bun)
        if expect_price == 1300:
            burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == expect_price

    @allure.title('Проверка вывода чека')
    def test_get_receipt(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        bun_name = bun.get_name()
        price = burger.get_price()
        type_ingredient = str(ingredient.get_type()).lower()
        name_ingredient = ingredient.get_name()
        receipt: List[str] = [f'(==== {bun_name} ====)']
        receipt.append(f'= {type_ingredient} {name_ingredient} =')
        receipt.append(f'(==== {bun_name} ====)\n')
        receipt.append(f'Price: {price}')

        assert receipt == burger.get_receipt()


