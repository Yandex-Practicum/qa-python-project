import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@allure.epic("Система заказа бургеров")
@allure.feature("Базовый функционал бургера")
class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        mock = Mock(spec=Bun)
        mock.get_name.return_value = "test bun"
        mock.get_price.return_value = 100.0
        return mock

    @pytest.fixture
    def mock_ingredient(self):
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = "test ingredient"
        mock.get_price.return_value = 50.0
        mock.get_type.return_value = "SAUCE"
        return mock

    @allure.title("Инициализация пустого бургера")
    @allure.description("Проверяем, что при создании бургера булочка не установлена, а список ингредиентов пуст")
    def test_init_empty_burger(self, burger):
        """Тест инициализации пустого бургера."""
        assert burger.bun is None
        assert burger.ingredients == []

    @allure.title("Установка булочки")
    @allure.description("Убеждаемся, что метод set_buns корректно устанавливает булочку")
    def test_set_buns(self, burger, mock_bun):
        """Тест установки булочки."""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title("Добавление ингредиента")
    @allure.description("Проверяем, что метод add_ingredient корректно добавляет ингредиент в список")
    def test_add_ingredient(self, burger, mock_ingredient):
        """Тест добавления ингредиента."""
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @allure.title("Удаление ингредиента по индексу")
    @allure.description("Проверяем работу метода remove_ingredient: ингредиент удаляется, длина списка уменьшается")
    def test_remove_ingredient(self, burger, mock_ingredient):
        """Тест удаления ингредиента по индексу."""
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title("Обработка ошибки при удалении ингредиента с неверным индексом")
    @allure.description("Убеждаемся, что при попытке удалить ингредиент с несуществующим индексом возникает IndexError")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_ingredient_index_error(self, burger):
        """Тест удаления ингредиента с неверным индексом."""
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    @allure.title("Перемещение ингредиента в списке")
    @allure.description("Проверяем корректность работы метода move_ingredient с разными комбинациями индексов")
    @pytest.mark.parametrize("index,new_index,expected_order", [
        (0, 1, [1, 0]),  # переместить первый на второе место
        (1, 0, [1, 0]),  # переместить второй на первое место
        (0, 0, [0, 1]),  # перемещение на ту же позицию
    ])
    def test_move_ingredient(self, burger, mock_ingredient, index, new_index, expected_order):
        """Тест перемещения ингредиента с параметризацией."""
        # Создаём два разных мока ингредиента
        mock_ingredient1 = mock_ingredient
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = "second ingredient"
        mock_ingredient2.get_price.return_value = 60.0
        mock_ingredient2.get_type.return_value = "FILLING"

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(index, new_index)

        # Проверяем порядок ингредиентов
        actual_order = []
        for ingredient in burger.ingredients:
            if ingredient.get_name() == "test ingredient":
                actual_order.append(0)
            else:
                actual_order.append(1)

        assert actual_order == expected_order

    @allure.title("Ошибка расчёта цены без установленной булочки")
    @allure.description("Проверяем, что при вызове get_price без предварительно установленной булочки возникает AttributeError")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_price_no_bun(self, burger):
        """Тест расчёта цены без булочки."""
        with pytest.raises(AttributeError):
            burger.get_price()

    @allure.title("Расчёт цены только с булочкой")
    @allure.description("Убеждаемся, что цена рассчитывается корректно, когда в бургере только булочка (без ингредиентов)")
    def test_get_price_only_bun(self, burger, mock_bun):
        """Тест расчёта цены только с булочкой."""
        burger.set_buns(mock_bun)
        price = burger.get_price()
        assert price == 200.0  # 100 * 2

    @allure.title("Расчёт цены с разными наборами ингредиентов")
    @allure.description("Проверяем метод get_price с различными комбинациями ингредиентов: от пустого списка до нескольких начинок")
    @pytest.mark.parametrize("ingredient_prices,expected_price", [
        ([50], 250.0),      # одна начинка: 2*100 + 50
        ([50, 60], 310.0),  # две начинки: 2*100 + 50 + 60
        ([], 200.0),         # без начинок: 2*100
    ])
    def test_get_price_with_ingredients(self, burger, mock_bun, ingredient_prices, expected_price):
        """Тест расчёта цены с разными наборами ингредиентов (параметризация)."""
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        price = burger.get_price()
        assert price == expected_price

    @allure.title("Ошибка получения чека без установленной булочки")
    @allure.description("Убеждаемся, что при вызове get_receipt без предварительно установленной булочки возникает AttributeError")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_receipt_no_bun(self, burger):
        """Тест получения чека без булочки."""
        with pytest.raises(AttributeError):
            burger.get_receipt()

    @allure.title("Формирование чека только с булочкой")
    @allure.description("Проверяем структуру чека, когда в бургере есть только булочка и нет ингредиентов")
    def test_get_receipt_only_bun(self, burger, mock_bun):
        """Тест чека только с булочкой."""
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()

        expected_lines = [
            '(==== test bun ====)',
            '(==== test bun ====)',
            'Price: 200.0'
        ]

        lines = receipt.split('\n')
        # Убираем пустые строки в конце
        lines = [line for line in lines if line]

        assert lines == expected_lines

    @allure.title("Формирование чека с ингредиентами")
    @allure.description("Проверяем полную структуру чека: наличие булочек, всех типов ингредиентов и итоговой цены")
    def test_get_receipt_with_ingredients(self, burger, mock_bun):
        """Тест чека с ингредиентами."""
        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient1.get_price.return_value = 100.0
        mock_ingredient1.get_type.return_value = "SAUCE"

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = "cutlet"
        mock_ingredient2.get_price.return_value = 150.0
        mock_ingredient2.get_type.return_value = "FILLING"

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        # Убираем пустые строки
        lines = [line for line in lines if line.strip()]

        with allure.step("Проверяем наличие верхней булочки в чеке"):
            assert '(==== test bun ====)' in lines

        with allure.step("Проверяем наличие соуса в чеке"):
            assert '= sauce hot sauce =' in lines

        with allure.step("Проверяем наличие котлеты в чеке"):
            assert '= filling cutlet =' in lines

        with allure.step("Проверяем наличие нижней булочки в чеке"):
            # Булочка должна встречаться дважды — учитываем это
            bun_count = sum(1 for line in lines if '(==== test bun ====)' in line)
            assert bun_count == 2

        with allure.step("Проверяем итоговую цену в чеке"):
            assert 'Price: 450.0' in lines

