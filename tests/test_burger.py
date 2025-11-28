import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.burger_data import get_burger_price_test_data, get_move_ingredient_test_data


class TestBurger:

    def test_burger_initialization_empty(self):
        """Проверяет, что новый бургер инициализируется пустым"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun_correctly(self, mock_bun):
        """Проверяет корректность установки булочки в бургер"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_single_ingredient(self, mock_ingredient_sauce):
        """Проверяет добавление одного ингредиента в бургер"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_add_multiple_ingredients(self, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяет добавление нескольких ингредиентов в бургер"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient_sauce
        assert burger.ingredients[1] == mock_ingredient_filling

    def test_remove_ingredient_removes_correctly(self, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяет корректное удаление ингредиента по индексу"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_move_ingredient_changes_order(self, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяет изменение порядка ингредиентов при перемещении"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        # Проверяем начальный порядок
        assert burger.ingredients[0] == mock_ingredient_sauce
        assert burger.ingredients[1] == mock_ingredient_filling

        # Перемещаем ингредиент
        burger.move_ingredient(0, 1)

        # Проверяем измененный порядок
        assert burger.ingredients[0] == mock_ingredient_filling
        assert burger.ingredients[1] == mock_ingredient_sauce

    def test_get_price_with_bun_and_ingredients(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяет расчет цены бургера с булочкой и ингредиентами"""
        burger = Burger()
        mock_bun.get_price.return_value = 100
        mock_ingredient_sauce.get_price.return_value = 50
        mock_ingredient_filling.get_price.return_value = 75

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        price = burger.get_price()
        expected_price = 100 * 2 + 50 + 75  # Булочка * 2 + ингредиенты
        assert price == expected_price

    def test_get_price_no_bun_returns_zero(self, mock_ingredient_sauce):
        """Проверяет, что цена возвращает 0 при отсутствии булочки"""
        burger = Burger()
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.get_price() == 0

    def test_get_price_only_bun_no_ingredients(self, mock_bun):
        """Проверяет расчет цены только с булочкой без ингредиентов"""
        burger = Burger()
        mock_bun.get_price.return_value = 150
        burger.set_buns(mock_bun)
        assert burger.get_price() == 300  # 150 * 2

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", get_burger_price_test_data())
    def test_get_price_parameterized(self, bun_price, ingredient_prices, expected_total):
        """Параметризованный тест расчета цены для различных комбинаций"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        # Добавляем ингредиенты с разными ценами
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total

    def test_get_receipt_with_bun_and_ingredients(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Проверяет генерацию чека с булочкой и ингредиентами"""
        burger = Burger()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100

        mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_sauce.get_name.return_value = "hot sauce"
        mock_ingredient_sauce.get_price.return_value = 100

        mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_filling.get_name.return_value = "cutlet"
        mock_ingredient_filling.get_price.return_value = 200

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)

        receipt = burger.get_receipt()

        # Проверяем полное соответствие чека ожидаемому формату
        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 500"
        )
        assert receipt == expected_receipt

    def test_get_receipt_no_bun_shows_none(self):
        """Проверяет генерацию чека при отсутствии булочки"""
        burger = Burger()
        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== None ====)\n"
            "(==== None ====)\n\n"
            "Price: 0"
        )
        assert receipt == expected_receipt

    def test_get_receipt_no_ingredients_only_bun(self, mock_bun):
        """Проверяет генерацию чека только с булочкой без ингредиентов"""
        burger = Burger()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200

        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== white bun ====)\n"
            "(==== white bun ====)\n\n"
            "Price: 400"
        )
        assert receipt == expected_receipt

    @pytest.mark.parametrize("index,new_index,expected_success", get_move_ingredient_test_data())
    def test_move_ingredient_parameterized(self, index, new_index, expected_success):
        """Параметризованный тест перемещения ингредиентов в различных позициях"""
        burger = Burger()

        # Создаем моки ингредиентов с уникальными именами для отслеживания порядка
        ingredients = []
        for i in range(3):
            mock_ingredient = Mock()
            mock_ingredient.get_name.return_value = f"ingredient_{i}"
            ingredients.append(mock_ingredient)
            burger.add_ingredient(mock_ingredient)

        # Запоминаем исходный порядок
        original_order = [ing.get_name() for ing in burger.ingredients]

        # Перемещаем ингредиент
        burger.move_ingredient(index, new_index)

        # Проверяем результат перемещения
        new_order = [ing.get_name() for ing in burger.ingredients]

        if index != new_index:
            # Проверяем, что порядок изменился
            assert new_order != original_order
            # Проверяем, что перемещенный ингредиент находится на новой позиции
            moved_ingredient_name = original_order[index]
            assert new_order[new_index] == moved_ingredient_name

    def test_remove_ingredient_from_empty_list_raises_error(self):
        """Проверяет выброс исключения при удалении из пустого списка ингредиентов"""
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_with_invalid_indexes_does_not_change_list(self):
        """Проверяет, что при неверных индексах список ингредиентов не изменяется"""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        original_ingredients = burger.ingredients.copy()

        # Пытаемся переместить с неверными индексами
        try:
            burger.move_ingredient(5, 0)  # Неверный исходный индекс
        except IndexError:
            pass  # Обрабатываем возможное исключение

        try:
            burger.move_ingredient(0, 5)  # Неверный целевой индекс
        except IndexError:
            pass  # Обрабатываем возможное исключение

        # Проверяем что список не изменился
        assert burger.ingredients == original_ingredients

    def test_move_ingredient_from_empty_burger_handled_gracefully(self):
        """Проверяет обработку попытки перемещения ингредиента из пустого бургера"""
        burger = Burger()

        # Пытаемся переместить из пустого списка
        try:
            burger.move_ingredient(0, 0)
            # Если не вызвало ошибку, проверяем что список остался пустым
            assert burger.ingredients == []
        except IndexError:
            # Если вызвало ошибку - это допустимое поведение
            pass

    def test_remove_ingredient_from_empty_burger_raises_error(self):
        """Проверяет выброс исключения при удалении ингредиента из пустого бургера"""
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
