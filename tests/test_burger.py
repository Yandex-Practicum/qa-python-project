import pytest  # импортируем pytest для параметризации тестов
from unittest.mock import Mock  # импортируем мок
from praktikum.burger import Burger  # импортируем класс бургер


class TestBurger:  # Набор тестов для проверки функционала класса бургер

    def test_set_buns(self, burger, bun):  # Тест проверяет успешное добавление и сохранение булки в объекте бургера
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):  # Тест проверяет успешное добавление ингредиента в список ингредиентов бургера
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, ingredient):  # Тест проверяет успешное удаление ингредиента из списка ингредиентов бургера
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_invalid_index(self, burger):  # Тест проверяет ошибку при удалении ингредиента по несуществующему индексу
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self, burger):  # Тест проверяет успешное перемещение ингредиентов в списке ингредиентов бургера
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_move_ingredient_invalid_index(self, burger):  # Тест проверяет ошибку при перемещении ингредиента по несуществующему исходному индексу
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)

    @pytest.mark.parametrize(  # Параметризация теста для проверки расчёта стоимости с разными ценами
        "bun_price, ingredient_price, expected_price",
        [
            (100, 50, 250),  # Проверяем обычную стоимость булочки и ингредиента
            (200, 100, 500),  # Проверяем более высокую стоимость булочки и ингредиента
            (300, 200, 800),  # Проверяем ещё один вариант расчёта стоимости
            (50, 0, 100),  # Проверяем расчёт стоимости с бесплатным ингредиентом
        ]
    )
    def test_get_price(self, burger, bun, ingredient, bun_price, ingredient_price, expected_price):  # Тест проверяет корректность расчёта общей стоимости бургера
        bun.get_price.return_value = bun_price
        ingredient.get_price.return_value = ingredient_price
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient):  # Тест проверяет корректность формирования чека бургера
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        ingredient.get_type.return_value = "SAUCE"
        ingredient.get_name.return_value = "hot sauce"
        ingredient.get_price.return_value = 50
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = "(==== black bun ====)\n= sauce hot sauce =\n(==== black bun ====)\n\nPrice: 250"
        assert burger.get_receipt() == receipt
