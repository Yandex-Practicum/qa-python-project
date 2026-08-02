import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    #Тесты для класса Burger
    def test_init(self):
        """Тест 1: Проверка инициализации бургера"""
        burger = Burger()
        assert burger.bun is None, "Булочка должна быть None при инициализации"
        assert burger.ingredients == [], "Список ингредиентов должен быть пустым"

    def test_set_buns(self):
        """Тест 2: Установка булочки"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 50.0

        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun, "Булочка должна сохраниться в объекте"
        assert burger.bun.get_name() == "Test Bun", "Название булочки должно совпадать"
        assert burger.bun.get_price() == 50.0, "Цена булочки должна совпадать"

    def test_add_ingredient(self):
        """Тест 3: Добавление одного ингредиента"""
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Test Ingredient"
        mock_ingredient.get_price.return_value = 30.0
        mock_ingredient.get_type.return_value = "sauce"

        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1, "Должен быть 1 ингредиент"
        assert burger.ingredients[0] == mock_ingredient, "Ингредиент должен сохраниться"
        assert burger.ingredients[0].get_name() == "Test Ingredient"

    def test_add_multiple_ingredients(self):
        """Тест 4: Добавление нескольких ингредиентов"""
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.add_ingredient(mock_ing3)

        assert len(burger.ingredients) == 3, "Должно быть 3 ингредиента"
        assert burger.ingredients == [mock_ing1, mock_ing2, mock_ing3], "Порядок должен сохраняться"

    def test_remove_ingredient(self):
        """Тест 5: Удаление ингредиента по индексу"""
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.add_ingredient(mock_ing3)

        burger.remove_ingredient(1)  # Удаляем второй ингредиент

        assert len(burger.ingredients) == 2, "Должно остаться 2 ингредиента"
        assert burger.ingredients == [mock_ing1, mock_ing3], "Порядок должен сохраниться"

    def test_remove_ingredient_first(self):
        """Тест 6: Удаление первого ингредиента"""
        mock_ing1 = Mock()
        mock_ing2 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing2

    def test_remove_ingredient_last(self):
        """Тест 7: Удаление последнего ингредиента"""
        mock_ing1 = Mock()
        mock_ing2 = Mock()

        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing1

    @pytest.mark.parametrize("from_idx,to_idx,expected_order", [
        # Перемещение первого на второе место
        (0, 1, [1, 0, 2]),
        # Перемещение второго на первое место
        (1, 0, [1, 0, 2]),
        # Перемещение первого в конец
        (0, 2, [1, 2, 0]),
        # Перемещение последнего на первое место
        (2, 0, [2, 0, 1]),
        # Перемещение в ту же позицию (ничего не меняется)
        (0, 0, [0, 1, 2]),
        (1, 1, [0, 1, 2]),
    ])

    def test_move_ingredient(self, from_idx, to_idx, expected_order):
        """Тест 8: Перемещение ингредиента с параметризацией"""
        # Создаем 3 разных мока
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        mock_ing3 = Mock()
        ingredients = [mock_ing1, mock_ing2, mock_ing3]

        burger = Burger()
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(from_idx, to_idx)

        # Проверяем порядок
        expected_ingredients = [ingredients[i] for i in expected_order]
        assert burger.ingredients == expected_ingredients, f"Неверный порядок при перемещении с {from_idx} на {to_idx}"

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_price", [
        # Только булочка
        (100.0, [], 200.0),
        # Булочка + один ингредиент
        (100.0, [50.0], 250.0),
        # Булочка + два ингредиента
        (100.0, [50.0, 30.0], 280.0),
        # Дешевая булочка
        (10.0, [5.0, 3.0], 28.0),
        # Бесплатная булочка
        (0.0, [50.0], 50.0),
        # Бесплатные ингредиенты
        (100.0, [0.0, 0.0], 200.0),
        # Только бесплатная булочка
        (0.0, [], 0.0),
        # Много ингредиентов
        (50.0, [10.0, 20.0, 30.0, 40.0], 200.0),
    ])

    def test_get_price(self, bun_price, ingredient_prices, expected_price):
        """Тест 9: Расчет цены бургера с параметризацией"""
        # Создаем мок для булочки
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        burger = Burger()
        burger.set_buns(mock_bun)

        # Добавляем ингредиенты с заданными ценами
        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_price, \
            f"Цена {burger.get_price()} не совпадает с ожидаемой {expected_price}"

        def test_get_receipt_without_ingredients(self):
            """Тест 10: Чек без ингредиентов (только булочка)"""
            mock_bun = Mock()
            mock_bun.get_name.return_value = "Black Bun"
            mock_bun.get_price.return_value = 100.0

            burger = Burger()
            burger.set_buns(mock_bun)

            expected_receipt = (
                "(==== Black Bun ====)\n"
                "(==== Black Bun ====)\n"
                "Price: 200.0"
        )

            assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_ingredients(self):
        """Тест 11: Чек с ингредиентами"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "White Bun"
        mock_bun.get_price.return_value = 80.0

        mock_ing1 = Mock()
        mock_ing1.get_type.return_value = "sauce"
        mock_ing1.get_name.return_value = "Spicy Sauce"
        mock_ing1.get_price.return_value = 40.0

        mock_ing2 = Mock()
        mock_ing2.get_type.return_value = "filling"
        mock_ing2.get_name.return_value = "Chicken Cutlet"
        mock_ing2.get_price.return_value = 120.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        expected_receipt = (
            "(==== White Bun ====)\n"
            "= sauce spicy sauce =\n"
            "= filling chicken cutlet =\n"
            "(==== White Bun ====)\n"
            "Price: 320.0"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_one_ingredient(self):
        """Тест 12: Чек с одним ингредиентом"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Rye Bun"
        mock_bun.get_price.return_value = 60.0

        mock_ing = Mock()
        mock_ing.get_type.return_value = "sauce"
        mock_ing.get_name.return_value = "BBQ Sauce"
        mock_ing.get_price.return_value = 30.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        expected_receipt = (
            "(==== Rye Bun ====)\n"
            "= sauce bbq sauce =\n"
            "(==== Rye Bun ====)\n"
            "Price: 150.0"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_mixed_case_types(self):
        """Тест 13: Чек с разным регистром типов ингредиентов"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Bun"
        mock_bun.get_price.return_value = 50.0

        mock_ing1 = Mock()
        mock_ing1.get_type.return_value = "SAUCE"  # Верхний регистр
        mock_ing1.get_name.return_value = "Ketchup"
        mock_ing1.get_price.return_value = 20.0

        mock_ing2 = Mock()
        mock_ing2.get_type.return_value = "FILLING"  # Верхний регистр
        mock_ing2.get_name.return_value = "Cheese"
        mock_ing2.get_price.return_value = 30.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        # Проверяем, что тип приводится к нижнему регистру
        expected_receipt = (
            "(==== Bun ====)\n"
            "= sauce ketchup =\n"
            "= filling cheese =\n"
            "(==== Bun ====)\n"
            "Price: 150.0"
        )

        assert burger.get_receipt() == expected_receipt
    
    def test_get_receipt_complex_scenario(self):
        """Тест 14: Сложный сценарий со многими ингредиентами"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Sesame Bun"
        mock_bun.get_price.return_value = 90.0

        ingredients_data = [
            ("sauce", "Mayo", 25.0),
            ("filling", "Beef Patty", 150.0),
            ("sauce", "Mustard", 15.0),
            ("filling", "Bacon", 80.0),
            ("sauce", "Garlic Sauce", 20.0),
        ]

        burger = Burger()
        burger.set_buns(mock_bun)

        for ing_type, ing_name, ing_price in ingredients_data:
            mock_ing = Mock()
            mock_ing.get_type.return_value = ing_type
            mock_ing.get_name.return_value = ing_name
            mock_ing.get_price.return_value = ing_price
            burger.add_ingredient(mock_ing)

        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= sauce mayo =\n"
            "= filling beef patty =\n"
            "= sauce mustard =\n"
            "= filling bacon =\n"
            "= sauce garlic sauce =\n"
            "(==== Sesame Bun ====)\n"
            "Price: 470.0"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_mock_price_calculation(self):
        """Тест 15: Проверка, что в чеке используется метод get_price()"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 70.0

        mock_ing = Mock()
        mock_ing.get_type.return_value = "sauce"
        mock_ing.get_name.return_value = "Test Sauce"
        mock_ing.get_price.return_value = 30.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()

        # Проверяем, что цена вычислена правильно
        assert "Price: 170.0" in receipt  # 70*2 + 30 = 170

    