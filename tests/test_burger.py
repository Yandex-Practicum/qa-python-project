import pytest
from unittest.mock import Mock, patch
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING



class TestBurger:

    # Тест для метода set_buns
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    # Тест для метода add_ingredient
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    # Тест для метода remove_ingredient
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient2

    # Тесты для метода move_ingredient
    @pytest.mark.parametrize("initial_index,new_index,expected_order", [
        (0, 1, [1, 0, 2]),  # Перемещение первого элемента на вторую позицию
        (1, 0, [1, 0, 2]),  # Перемещение второго элемента на первую позицию
        (2, 1, [0, 2, 1]),  # Перемещение последнего элемента на среднюю позицию
    ])
    def test_move_ingredient(self, initial_index, new_index, expected_order):
        burger = Burger()
        mock_ingredients = [Mock() for _ in range(3)]

        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)

        burger.move_ingredient(initial_index, new_index)

        # Проверяем, что порядок изменился как ожидалось
        for i, order_index in enumerate(expected_order):
            assert burger.ingredients[i] == mock_ingredients[order_index]

    # Тесты для метода get_price
    @patch('burger.Bun')
    def test_get_price_with_only_bun(self, mock_bun_class):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 25
        mock_bun_class.return_value = mock_bun

        burger.set_buns(mock_bun)

        assert burger.get_price() == 50  # Две булки

    @patch('burger.Bun')
    def test_get_price_with_bun_and_ingredients(self,mock_bun_class):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 25
        mock_bun_class.return_value = mock_bun

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 20
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 10

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert burger.get_price() == 80  # 2*25 + 20 + 10

    # Тесты для метода get_receipt
    @pytest.mark.parametrize("bun_name,ingredient_type,ingredient_name,expected_lines", [
        ("white bun", INGREDIENT_TYPE_SAUCE, "hot sauce", [
            "(==== white bun ====)",
            "= sauce hot sauce =",
            "(==== white bun ====)",
            "",
            "Price: 50"
        ]),
        ("black bun", INGREDIENT_TYPE_FILLING, "cutlet", [
            "(==== black bun ====)",
            "= filling cutlet =",
            "(==== black bun ====)",
            "",
            "Price: 50"
        ]),
        ("red bun", None, None, [
            "(==== red bun ====)",
            "(==== red bun ====)",
            "",
            "Price: 50"
        ]),
    ])
    @patch('burger.Bun')
    def test_get_receipt(self, bun_name, ingredient_type, ingredient_name, expected_lines,mock_bun_class):
        burger = Burger()

        # Создаём мок для булки
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 25
        mock_bun_class.return_value = mock_bun

        burger.set_buns(mock_bun)

        # Настраиваем мок для ингредиента, если он передан
        if ingredient_name is not None:
            mock_ingredient = Mock()
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_name.return_value = ingredient_name
            mock_ingredient.get_price.return_value = 0  # Для упрощения теста
            burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()
        assert receipt.split('\n') == expected_lines

    # Тест на проверку вызовов методов в get_price
    @patch('burger.Bun')
    def test_get_price_method_calls(self, mock_bun_class):
        burger = Burger()

        # Создаём мок для булки
        mock_bun = Mock()
        mock_bun.get_price.return_value = 25
        mock_bun_class.return_value = mock_bun

        # Создаём моки для ингредиентов
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 20
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 10

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.get_price()

        # Проверяем, что методы вызывались правильное количество раз
        assert mock_bun.get_price.call_count == 2  # Две булки
        mock_ingredient1.get_price.assert_called_once()
        mock_ingredient2.get_price.assert_called_once()