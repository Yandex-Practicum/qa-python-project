import data
from praktikum.burger import Burger


class TestBurger:

    # Проверка возможности создать объект класса Burger с замокированной черной булкой методом set_buns
    def test_set_buns_all_types(self, mock_bun):
        burger_test = Burger()
        start_bun = burger_test.bun
        expected_end_bun = mock_bun.get_name()
        burger_test.set_buns(mock_bun)
        end_bun = burger_test.bun.get_name()
        # проверим, что она добавилась
        assert start_bun is None and end_bun == expected_end_bun, f'start_bun == {start_bun} and end_bun == {end_bun}'

    # Проверка возможности создать объект класса Burger с 2 замокированными ингредиентами методом add_ingredient
    def test_add_ingredient_add_2_ingredients(self, mock_ingredient_1, mock_ingredient_2):
        burger_test = Burger()
        count_ingredients_start = len(burger_test.ingredients)
        burger_test.add_ingredient(mock_ingredient_1)
        burger_test.add_ingredient(mock_ingredient_2)
        count_ingredients_end = len(burger_test.ingredients)
        # проверим, что они добавилась
        assert count_ingredients_start == 0 and count_ingredients_end == 2, f'burger_test.ingredients == {burger_test.ingredients}'

    # Проверка возможности создать объект класса Burger с 2 ингредиентами и поменять их местами методом move_ingredient
    def test_move_ingredient_1_of_2_ingredients(self, mock_ingredient_1, mock_ingredient_2):
        burger_test = Burger()
        burger_test.add_ingredient(mock_ingredient_1)
        burger_test.add_ingredient(mock_ingredient_2)
        ingredients_name_start = [burger_test.ingredients[0].get_name(), burger_test.ingredients[1].get_name()]
        burger_test.move_ingredient(1, 0)
        ingredients_name_end = [burger_test.ingredients[0].get_name(), burger_test.ingredients[1].get_name()]
        # убедимся, что ингредиенты поменялись местами
        assert ingredients_name_start[0] == ingredients_name_end[1] and ingredients_name_start[1] == \
               ingredients_name_end[0], f'burger_test.ingredients == {burger_test.ingredients}'

    # Проверка возможности создать объект класса Burger с 2 ингредиентами и удалить один из них методом remove_ingredient
    def test_remove_ingredient_1_of_2_ingredients(self, mock_ingredient_1, mock_ingredient_2):
        burger_test = Burger()
        burger_test.add_ingredient(mock_ingredient_1)
        burger_test.add_ingredient(mock_ingredient_2)
        ingredients_start = len(burger_test.ingredients)
        burger_test.remove_ingredient(0)
        ingredients_end = len(burger_test.ingredients)
        # убедимся, что второй ингредиент удалился
        assert ingredients_start == 2 and ingredients_end == 1 and burger_test.ingredients[0].get_name() == mock_ingredient_2.name, f'burger_test.ingredients == {burger_test.ingredients}'

    # Проверка возможности создать объект класса Burger с булкой и 2 ингредиентами и сформировать его стоимость методом get_price
    def test_get_price_bun_and_2_ingredients(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger_test = Burger()
        burger_test.set_buns(mock_bun)
        burger_test.add_ingredient(mock_ingredient_1)
        burger_test.add_ingredient(mock_ingredient_2)
        # убедимся, что стоимость бургера правильно формируется
        assert burger_test.get_price() == data.price_test(), f'burger_test.get_price() == {burger_test.get_price()}'

    # Проверка возможности создать объект класса Burger с булкой и 2 ингредиентами и сформировать его рецепт методом get_receipt
    def test_get_receipt_bun_and_2_ingredients(self, mock_bun, mock_ingredient_1, mock_ingredient_2):
        burger_test = Burger()
        burger_test.set_buns(mock_bun)
        burger_test.add_ingredient(mock_ingredient_1)
        burger_test.add_ingredient(mock_ingredient_2)
        # убедимся, что рецепт бургера правильно формируется
        assert burger_test.get_receipt() == data.receipt_test(), f'burger_test.get_receipt() =={burger_test.get_receipt()}, data.receipt_test == {data.receipt_test}'
