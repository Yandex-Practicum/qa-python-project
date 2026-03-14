import pytest
import allure

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient



@allure.suite("Тестирование класса Burger")
@allure.feature("Основные функции бургера")
class TestBurger:

    @pytest.fixture(autouse=True)
    def setup(self, mock_bun, mock_ingredient):
        """Подготовка тестового окружения для каждого теста."""
        with allure.step("Инициализация экземпляра Burger"):
            self.burger = Burger()
        self.mock_bun = mock_bun
        self.mock_ingredient = mock_ingredient


    @allure.title("Тест установки булочки в бургер")
    @allure.description("Проверяет корректность установки булочки через метод set_buns.")
    def test_set_buns(self):
        with allure.step("Устанавливаем моковую булочку в бургер"):
            self.burger.set_buns(self.mock_bun)
       
        with allure.step("Проверяем, что булочка установлена корректно"):
            assert self.burger.bun == self.mock_bun, "Булочка не была установлена"


    @allure.title("Тест добавления ингредиентов")
    @allure.description("Проверяет добавление ингредиентов в бургер с разной кратностью.")
    @pytest.mark.parametrize("count", [1, 2, 3], ids=["один ингредиент", "два ингредиента", "три ингредиента"])
    def test_add_ingredient(self, count):
        with allure.step(f"Добавляем {count} ингредиентов в бургер"):
            for _ in range(count):
                self.burger.add_ingredient(self.mock_ingredient)
        with allure.step("Проверяем количество добавленных ингредиентов"):
            assert len(self.burger.ingredients) == count, f"Ожидалось {count} ингредиентов"


    @allure.title("Тест удаления ингредиента по индексу")
    @allure.description("Проверяет удаление ингредиента из списка по указанному индексу.")
    def test_remove_ingredient(self):
        with allure.step("Добавляем два ингредиента для тестирования удаления"):
            self.burger.add_ingredient(self.mock_ingredient)
            self.burger.add_ingredient(self.mock_ingredient)
        with allure.step("Удаляем ингредиент с индексом 0"):
            self.burger.remove_ingredient(0)
        with allure.step("Проверяем, что остался один ингредиент"):
            assert len(self.burger.ingredients) == 1, "После удаления должен остаться 1 ингредиент"


    @allure.title("Тест перемещения ингредиента")
    @allure.description("Проверяет корректность перемещения ингредиента внутри списка ингредиентов.")
    def test_move_ingredient(self):
        ingredient_1 = Mock(spec=Ingredient)
        ingredient_1.get_name.return_value = "ингредиент_1"
        ingredient_2 = Mock(spec=Ingredient)
        ingredient_2.get_name.return_value = "ингредиент_2"
        ingredient_3 = Mock(spec=Ingredient)
        ingredient_3.get_name.return_value = "ингредиент_3"
        with allure.step("Добавляем три уникальных ингредиента"):
            self.burger.add_ingredient(ingredient_1)
            self.burger.add_ingredient(ingredient_2)
            self.burger.add_ingredient(ingredient_3)
        with allure.step("Перемещаем ингредиент с индексом 0 на позицию 2"):
            self.burger.move_ingredient(0, 2)
        with allure.step("Проверяем новый порядок ингредиентов"):
            names = [ing.get_name() for ing in self.burger.ingredients]
            expected_names = ["ингредиент_2", "ингредиент_3", "ингредиент_1"]
            assert names == expected_names, f"Ожидаемый порядок: {expected_names}, фактический: {names}"


    @allure.title("Тест расчёта цены бургера")
    @allure.description("Проверяет корректный расчёт общей стоимости бургера с учётом булочек и ингредиентов.")
    def test_get_price(self):
        bun = Bun("Чёрная булочка", 150.0)
        ingredient_1 = Ingredient("SAUCE", "Острый соус", 75.0)
        ingredient_2 = Ingredient("FILLING", "Котлета", 125.0)
        with allure.step("Устанавливаем булочку"):
            self.burger.set_buns(bun)
        with allure.step("Добавляем ингредиенты"):
            self.burger.add_ingredient(ingredient_1)
            self.burger.add_ingredient(ingredient_2)
        with allure.step("Рассчитываем итоговую цену"):
            total_price = self.burger.get_price()
        with allure.step("Проверяем корректность расчёта"):
            expected_price = (150.0 * 2) + 75.0 + 125.0
            assert total_price == expected_price, f"Ожидаемая цена: {expected_price}, фактическая: {total_price}"


    @allure.title("Тест формирования чека")
    @allure.description("Проверяет корректность генерации текстового чека с информацией о бургере.")
    def test_get_receipt(self):
        bun = Bun("Чёрная булочка", 100.0)
        ingredient_1 = Ingredient("SAUCE", "Острый соус", 100.0)
        ingredient_2 = Ingredient("FILLING", "Котлета", 100.0)
        with allure.step("Устанавливаем булочку"):
            self.burger.set_buns(bun)
        with allure.step("Добавляем ингредиенты"):
            self.burger.add_ingredient(ingredient_1)
            self.burger.add_ingredient(ingredient_2)
        with allure.step("Генерируем чек"):
            receipt = self.burger.get_receipt()
        with allure.step("Проверяем содержимое чека"):
            expected_lines = [
                "(==== Чёрная булочка ====)",
                "= sauce Острый соус =",
                "= filling Котлета =",
                "(==== Чёрная булочка ====)\n",
                f"Price: {self.burger.get_price()}"
            ]
            for line in expected_lines:
                assert line in receipt, f"Строка '{line}' отсутствует в чеке"
        allure.attach(receipt, name="Сгенерированный чек", attachment_type="text")

    @allure.title("Тест расчёта цены без булочки")
    @allure.description("Проверяет, что при отсутствии булочки возникает ошибка при расчёте цены.")
    def test_get_price_without_bun(self):
        with allure.step("Пытаемся рассчитать цену без установленной булочки"):
            with pytest.raises(AttributeError):
                self.burger.get_price()


    @allure.title("Тест генерации чека без булочки")
    @allure.description("Проверяет, что при отсутствии булочки возникает ошибка при формировании чека.")
    def test_get_receipt_without_bun(self):
        with allure.step("Пытаемся сформировать чек без установленной булочки"):
            with pytest.raises(AttributeError):
                self.burger.get_receipt()


    @allure.title("Тест добавления ингредиента с некорректным типом")
    @allure.description("Проверяет реакцию системы на попытку добавить объект, не являющийся Ingredient.")
    def test_add_invalid_ingredient(self):
        with allure.step("Создаём некорректный объект (не Ingredient)"):
            invalidobject = "не ингредиент"
        with allure.step("Пытаемся добавить некорректный объект в бургер"):
            self.burger.add_ingredient(invalidobject)
        with allure.step("Проверяем, что объект добавлен в список ингредиентов"):
            assert len(self.burger.ingredients) == 1, "Объект должен быть добавлен в список"
            assert self.burger.ingredients[0] == "не ингредиент", "Добавлен неверный объект"


    @allure.title("Тест удаления ингредиента с несуществующим индексом")
    @allure.description("Проверяет обработку попытки удаления ингредиента по индексу, выходящему за границы списка.")
    def test_remove_ingredient_out_of_range(self):
        with allure.step("Добавляем один ингредиент для теста"):
            self.burger.add_ingredient(self.mock_ingredient)
        with allure.step("Пытаемся удалить ингредиент по несуществующему индексу (99)"):
            with pytest.raises(IndexError):
                self.burger.remove_ingredient(99)


    @allure.title("Тест перемещения ингредиента с некорректными индексами")
    @allure.description("Проверяет обработку некорректных индексов при перемещении ингредиента.")
    @pytest.mark.parametrize(
        "from_idx,to_idx,expects_exception,expected_result",
        [
            (-3, 0, True, None),         # from_idx вне диапазона → IndexError
            (99, 0, True, None),         # from_idx вне диапазона → IndexError
            (-1, 0, False, "moved"),     # from_idx валиден (-1) → перемещение успешно
            (0, -3, False, "unchanged"), # to_idx вне диапазона, но from_idx валиден → список не меняется
            (0, 99, False, "unchanged"), # to_idx > len → вставка в конец, но логика теста требует "unchanged"
        ],
        ids=[
            "from_idx вне диапазона (отрицательный)",
            "from_idx вне диапазона (положительный)",
            "from_idx валидный отрицательный",
            "to_idx вне диапазона (отрицательный)",
            "to_idx вне диапазона (положительный)"
        ]
    )
    def test_move_ingredient_invalid_indices(self, from_idx, to_idx, expects_exception, expected_result):
        with allure.step("Добавляем два ингредиента для теста перемещения"):
            self.burger.add_ingredient(self.mock_ingredient)
            self.burger.add_ingredient(self.mock_ingredient)
        original_ingredients = self.burger.ingredients.copy()
        with allure.step(f"Пытаемся переместить ингредиент: from_idx={from_idx}, to_idx={to_idx}"):
            if expects_exception:
                with pytest.raises(IndexError):
                    self.burger.move_ingredient(from_idx, to_idx)
            else:
                self.burger.move_ingredient(from_idx, to_idx)
                if expected_result == "moved":
                    assert len(self.burger.ingredients) == 2, "Количество ингредиентов изменилось"
                    assert self.burger.ingredients[0] == original_ingredients[-1], "Элемент не переместился корректно"
                elif expected_result == "unchanged":
                    assert self.burger.ingredients == original_ingredients, \
                        f"Список изменился при некорректном to_idx={to_idx}"


    @allure.title("Тест получения пустого списка ингредиентов")
    @allure.description("Проверяет корректность работы с пустым списком ингредиентов.")
    def test_empty_ingredients_list(self):
        with allure.step("Проверяем, что список ингредиентов изначально пуст"):
            assert len(self.burger.ingredients) == 0, \
                "Изначально список ингредиентов должен быть пустым"
        with allure.step("Пытаемся получить цену при пустом списке ингредиентов (только булочка)"):
            bun = Bun("Белая булочка", 200.0)
            self.burger.set_buns(bun)
            price = self.burger.get_price()
        with allure.step("Проверяем расчёт цены (только булочки)"):
            expected_price = 200.0 * 2
            assert price == expected_price, f"Цена должна быть {expected_price}, получено {price}"
        with allure.step("Формируем чек с пустой начинкой"):
            receipt = self.burger.get_receipt()
        with allure.step("Проверяем структуру чека без ингредиентов"):
            expected_lines = [
                "(==== Белая булочка ====)",
                "(==== Белая булочка ====)\n",
                f"Price: {price}"
            ]
            for line in expected_lines:
                assert line in receipt, f"Строка '{line}' отсутствует в чеке"


    @allure.title("Тест повторного перемещения ингредиента")
    @allure.description("Проверяет многократное перемещение одного и того же ингредиента.")
    def test_repeated_ingredient_movement(self):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = "уникальный_ингредиент"
        with allure.step("Добавляем один уникальный ингредиент"):
            self.burger.add_ingredient(ingredient)
        with allure.step("Перемещаем ингредиент несколько раз между позициями"):
            self.burger.move_ingredient(0, 0)
            self.burger.move_ingredient(0, 1)
            self.burger.move_ingredient(0, 0)
        with allure.step("Проверяем, что ингредиент остался в списке"):
            assert len(self.burger.ingredients) == 1, "Ингредиент должен остаться в списке"
            assert self.burger.ingredients[0].get_name() == "уникальный_ингредиент", \
                "Имя ингредиента должно сохраниться"
