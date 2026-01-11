import allure
from praktikum.burger import Burger
import pytest
from unittest.mock import Mock


class TestBurger:
    @allure.title('Проверка верного значения аттрибута булки')
    def test_set_buns_correct_creation(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    @allure.title('Проверка верного значения аттрибута ингредиента')
    def test_add_ingredient_one_ingredient_correct_add(self, mock_ingredient1):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)

        assert mock_ingredient1 in burger.ingredients

    @allure.title('Проверка, что ингредиент удаляется верно')
    def test_remove_ingredient_correct_index_success_remove(self, burger):
        ingredient1 = burger.ingredients[0]
        ingredient2 = burger.ingredients[1]
        burger.remove_ingredient(0)

        assert ingredient2 in burger.ingredients and ingredient1 not in burger.ingredients

    @allure.title('Проверка, что ингредиент корректно перемещается вниз и вверх')
    @pytest.mark.parametrize(
        'index, index_new',
        [
            (0, 1),
            (1, 1),
            (2, 0)
        ])
    def test_move_ingredient_correct_replace_ingredient(self, index, index_new):
        mock_1 = Mock()
        mock_2 = Mock()
        mock_3 = Mock()
        exp_res = [[mock_2, mock_1, mock_3], [mock_1, mock_2, mock_3], [mock_3, mock_1, mock_2]]
        burger = Burger()
        burger.ingredients = [mock_1, mock_2, mock_3]
        burger.move_ingredient(index, index_new)

        assert burger.ingredients == exp_res[index]

    @allure.title('Проверка на получение корректной цены')
    def test_get_price_success(self, mock_bun, mock_ingredient1, mock_ingredient2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.set_buns(mock_bun)

        mock_bun.get_price.return_value = 100
        mock_ingredient1.get_price.return_value = 100
        mock_ingredient2.get_price.return_value = 100

        assert burger.get_price() == 400


    @allure.title("Проверка, что чек верно печатается")
    def test_get_receipt_return_correct_value(self):
        mock_bun = Mock()
        mock_ingredient = Mock()
        mock_bun.get_name.return_value = "Булочка"
        mock_bun.get_price.return_value = 100.0
        mock_ingredient.get_name.return_value = "Острый"
        mock_ingredient.get_type.return_value = "соус"
        mock_ingredient.get_price.return_value = 100.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        return_receipt = burger.get_receipt()

        assert return_receipt == "(==== Булочка ====)\n= соус Острый =\n(==== Булочка ====)\n\nPrice: 300.0"