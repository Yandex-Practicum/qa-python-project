from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_with_mock_bun_sets_bun_attribute(self, mock_bun,
                                                       real_burger):  # тестирует set_buns: при передаче мок-булочки она сохраняется в атрибуте bun

        real_burger.set_buns(mock_bun)

        assert real_burger.bun is mock_bun, (f'Объект булочки в памяти/атрибуте класса {real_burger.bun}'
                                             f'не совпадает с переданным моком булочки {mock_bun} ')

    def test_add_ingredient_with_mock_ingredient_appends_to_ingredients_list(self, mock_filling_ingredient,
                                                                             real_burger):  # тестирует add_ingredient: мок-ингредиент добавляется в список ингредиентов

        real_burger.add_ingredient(mock_filling_ingredient)

        assert real_burger.ingredients[-1] is mock_filling_ingredient, (
            f'Объект ингредиента в памяти/списке ингредиентов'
            f' {real_burger.ingredients}'f'не совпадает с переданным\
                                                       моком ингредиента {mock_filling_ingredient} ')

    def test_remove_ingredient_with_valid_index_removes_ingredient_from_list(self, mock_sauce_ingredient,
                                                                             real_burger):  # тестирует remove_ingredient: при удалении по  индексу ингредиент исчезает из списка

        real_burger.add_ingredient(mock_sauce_ingredient)
        real_burger.remove_ingredient(0)

        assert mock_sauce_ingredient not in real_burger.ingredients, (f' Удаленный ингредиент  {mock_sauce_ingredient}'
                                                                      f' содержится в списке ингредиентов  {real_burger.ingredients} ')

    def test_move_ingredient_changes_ingredient_order_in_list(self, mock_filling_ingredient, mock_sauce_ingredient,
                                                              real_burger):  # тестирует move_ingredient: меняет порядок ингредиентов в списке

        real_burger.add_ingredient(mock_filling_ingredient)
        real_burger.add_ingredient(mock_sauce_ingredient)

        real_burger.move_ingredient(1, 0)  # меняем местами

        assert real_burger.ingredients == [mock_sauce_ingredient,
                                           mock_filling_ingredient], f' Порядок ингредиентов не изменился  {real_burger.ingredients}'

    def test_get_price_with_bun_and_ingredient_returns_correct_total_price(
            self, mock_bun, mock_filling_ingredient, real_burger):  # тестирует get_price: возвращает корректную сумму — цена булки × 2 + ингредиенты

        real_burger.set_buns(mock_bun)
        real_burger.add_ingredient(mock_filling_ingredient)

        assert real_burger.get_price() == 478.5, f' Ожидаемая общая цена {478.5}, получили {real_burger.get_price()}'

    def test_get_receipt_with_bun_and_ingredient_returns_formatted_receipt(
            self, mock_filling_ingredient, mock_bun, real_burger ):  # тестирует get_receipt: возвращает чек в правильном отформатированном виде

        # собираем наш моковый бургер
        real_burger.set_buns(mock_bun)
        real_burger.add_ingredient(mock_filling_ingredient)

        # Проверка с прямым сравнением строк
        assert real_burger.get_receipt() == (f"(==== Розовая булочка ====)\n"
                                        f"= filling Котлетка =\n"
                                        f"(==== Розовая булочка ====)\n"
                                        f"\n"
                                        f"Price: 478.5")