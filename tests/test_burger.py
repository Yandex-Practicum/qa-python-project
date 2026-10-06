import pytest
from unittest.mock import Mock
from inspect import cleandoc

import tests.constants as c


class TestBurger:

    def test_set_buns(self, burger):
        mock_bun = Mock()
        # ВЫЗОВ ТЕСТИРУЕМОГО МЕТОДА
        burger.set_buns(mock_bun)
        # ПРОВЕРКА РЕЗУЛЬТАТА
        assert burger.bun == mock_bun


    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        # ВЫЗОВ ТЕСТИРУЕМОГО МЕТОДА
        burger.add_ingredient(mock_ingredient)
        # ПРОВЕРКА РЕЗУЛЬТАТА
        assert mock_ingredient in burger.ingredients


    @pytest.mark.parametrize("test_index", [0, 1])
    def test_remove_ingredient(self, burger, test_index):
        mock_ingredient_0 = Mock()
        burger.add_ingredient(mock_ingredient_0)
        mock_ingredient_1 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        mock_ingredients = [mock_ingredient_0, mock_ingredient_1]
        # ВЫЗОВ ТЕСТИРУЕМОГО МЕТОДА
        burger.remove_ingredient(test_index)
        # ПРОВЕРКА РЕЗУЛЬТАТА
        assert mock_ingredients[test_index] not in burger.ingredients


    def test_move_ingredient(self, burger):
        mock_ingredient_0 = Mock()
        burger.add_ingredient(mock_ingredient_0)

        mock_ingredient_1 = Mock()
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_2)

        # ВЫЗОВ ТЕСТИРУЕМОГО МЕТОДА
        burger.move_ingredient(0, 2)
        # ПРОВЕРКА РЕЗУЛЬТАТА
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2, mock_ingredient_0]


    def test_get_price(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = c.TEST_BUN_PRICE
        burger.bun = mock_bun

        mock_ingredient_0 = Mock()
        mock_ingredient_0.get_price.return_value = c.TEST_INGR_0_PRICE
        burger.add_ingredient(mock_ingredient_0)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = c.TEST_INGR_1_PRICE
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = c.TEST_INGR_2_PRICE
        burger.add_ingredient(mock_ingredient_2)

        # ВЫЗОВ ТЕСТИРУЕМОГО МЕТОДА
        price = burger.get_price()
        # ПРОВЕРКА РЕЗУЛЬТАТА
        assert price == c.TEST_BUN_PRICE * 2 + c.TEST_INGR_0_PRICE + c.TEST_INGR_1_PRICE + c.TEST_INGR_2_PRICE


    def test_get_receipt(self, burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = c.TEST_BUN_PRICE
        mock_bun.get_name.return_value = c.TEST_BUN_NAME
        burger.bun = mock_bun

        mock_ingredient_0 = Mock()
        mock_ingredient_0.get_price.return_value = c.TEST_INGR_0_PRICE
        mock_ingredient_0.get_name.return_value = c.TEST_INGR_0_NAME
        mock_ingredient_0.get_type.return_value = c.TEST_INGR_0_TYPE
        burger.add_ingredient(mock_ingredient_0)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = c.TEST_INGR_1_PRICE
        mock_ingredient_1.get_name.return_value = c.TEST_INGR_1_NAME
        mock_ingredient_1.get_type.return_value = c.TEST_INGR_1_TYPE
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = c.TEST_INGR_2_PRICE
        mock_ingredient_2.get_name.return_value = c.TEST_INGR_2_NAME
        mock_ingredient_2.get_type.return_value = c.TEST_INGR_2_TYPE
        burger.add_ingredient(mock_ingredient_2)

        # вычисление ожидаемого значения
        except_price = c.TEST_BUN_PRICE * 2 + c.TEST_INGR_0_PRICE + c.TEST_INGR_1_PRICE + c.TEST_INGR_2_PRICE
        expected_receipt = cleandoc(f"""
            (==== {c.TEST_BUN_NAME} ====)
            = {c.TEST_INGR_0_TYPE} {c.TEST_INGR_0_NAME} =
            = {c.TEST_INGR_1_TYPE} {c.TEST_INGR_1_NAME} =
            = {c.TEST_INGR_2_TYPE} {c.TEST_INGR_2_NAME} =
            (==== {c.TEST_BUN_NAME} ====)

            Price: {except_price}
        """)

        # ВЫЗОВ ТЕСТИРУЕМОГО МЕТОДА
        actual_receipt = burger.get_receipt()
        # ПРОВЕРКА РЕЗУЛЬТАТА
        assert expected_receipt == actual_receipt
