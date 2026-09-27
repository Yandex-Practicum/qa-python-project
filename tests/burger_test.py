import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.burger = Burger()
        self.mock_bun = Mock()
        self.mock_bun.get_name.return_value = "White Bun"
        self.mock_bun.get_price.return_value = 2.5
        self.mock_ingredient1 = Mock()
        self.mock_ingredient1.get_name.return_value = "Ketchup"
        self.mock_ingredient1.get_price.return_value = 1.5
        self.mock_ingredient1.get_type.return_value = "SAUCE"
        self.mock_ingredient2 = Mock()
        self.mock_ingredient2.get_name.return_value = "Beef Patty"
        self.mock_ingredient2.get_price.return_value = 3.0
        self.mock_ingredient2.get_type.return_value = "FILLING"
        self.mock_ingredient3 = Mock()
        self.mock_ingredient3.get_name.return_value = "Cheese"
        self.mock_ingredient3.get_price.return_value = 1.75
        self.mock_ingredient3.get_type.return_value = "FILLING"

    def test_create_burger_initial_state(self):
        """Тест проверки начального состояния бургера"""
        assert self.burger.bun is None
        assert self.burger.ingredients == []

    def test_set_buns(self):
        """Тест задания булочки"""
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun

    @pytest.mark.parametrize("bun_name, bun_price", [
        ("White Bun", 2.5),
        ("Black Bun", 3.0),
        ("Sesame Bun", 1.75),
        ("Whole Wheat", 2.0),
    ])
    def test_set_buns_with_different_buns(self, bun_name, bun_price):
        """Тест задания разных булочек"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        self.burger.set_buns(mock_bun)

        assert self.burger.bun == mock_bun
        assert self.burger.bun.get_name() == bun_name
        assert self.burger.bun.get_price() == bun_price

    def test_add_ingredient(self):
        """Тест добавления одного ингредиента"""
        self.burger.add_ingredient(self.mock_ingredient1)

        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient1

    @pytest.mark.parametrize("ingredient_name, ingredient_price, ingredient_type", [
        ("Ketchup", 1.5, "SAUCE"),
        ("Beef Patty", 3.0, "FILLING"),
        ("Cheese", 1.75, "FILLING"),
        ("Mayonnaise", 1.0, "SAUCE"),
        ("Lettuce", 0.5, "FILLING"),
    ])
    def test_add_ingredient_with_different_ingredients(self, ingredient_name, ingredient_price, ingredient_type):
        """Тест добавления разных ингредиентов"""
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price
        mock_ingredient.get_type.return_value = ingredient_type

        self.burger.add_ingredient(mock_ingredient)

        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0].get_name() == ingredient_name
        assert self.burger.ingredients[0].get_price() == ingredient_price
        assert self.burger.ingredients[0].get_type() == ingredient_type

    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)

        assert len(self.burger.ingredients) == 3
        assert self.burger.ingredients[0].get_name() == "Ketchup"
        assert self.burger.ingredients[1].get_name() == "Beef Patty"
        assert self.burger.ingredients[2].get_name() == "Cheese"

    @pytest.mark.parametrize("remove_index, expected_remaining", [
        (0, ["Beef Patty", "Cheese"]),
        (1, ["Ketchup", "Cheese"]),
        (2, ["Ketchup", "Beef Patty"]),
    ])
    def test_remove_ingredient_from_different_positions(self, remove_index, expected_remaining):
        """Тест удаления ингредиентов из разных позиций"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)

        self.burger.remove_ingredient(remove_index)

        assert len(self.burger.ingredients) == 2
        remaining_names = [ing.get_name() for ing in self.burger.ingredients]
        assert remaining_names == expected_remaining

    def test_remove_ingredient_from_empty_list_raises_error(self):
        """Тест удаления ингредиента из пустого списка вызывает ошибку"""
        with pytest.raises(IndexError):
            self.burger.remove_ingredient(0)

    @pytest.mark.parametrize("invalid_index", [5, 10, -10])
    def test_remove_ingredient_with_invalid_index_raises_error(self, invalid_index):
        """Тест удаления ингредиента с невалидным индексом вызывает ошибку"""
        self.burger.add_ingredient(self.mock_ingredient1)

        with pytest.raises(IndexError):
            self.burger.remove_ingredient(invalid_index)

    @pytest.mark.parametrize("from_index, to_index, expected_order", [
        (0, 2, ["Beef Patty", "Cheese", "Ketchup"]),
        (2, 0, ["Cheese", "Ketchup", "Beef Patty"]),
        (1, 2, ["Ketchup", "Cheese", "Beef Patty"]),
        (1, 0, ["Beef Patty", "Ketchup", "Cheese"]),
    ])
    def test_move_ingredient_between_positions(self, from_index, to_index, expected_order):
        """Тест перемещения ингредиентов между позициями"""
        self.burger.add_ingredient(self.mock_ingredient1)  # Ketchup
        self.burger.add_ingredient(self.mock_ingredient2)  # Beef Patty
        self.burger.add_ingredient(self.mock_ingredient3)  # Cheese

        self.burger.move_ingredient(from_index, to_index)

        assert len(self.burger.ingredients) == 3
        actual_order = [ing.get_name() for ing in self.burger.ingredients]
        assert actual_order == expected_order

    def test_move_ingredient_to_same_position(self):
        """Тест перемещения ингредиента на ту же позицию"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)

        self.burger.move_ingredient(0, 0)

        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[0].get_name() == "Ketchup"
        assert self.burger.ingredients[1].get_name() == "Beef Patty"

    def test_get_price_without_bun_raises_error(self):
        """Тест получения цены без заданной булочки вызывает ошибку"""
        with pytest.raises(AttributeError):
            self.burger.get_price()

    @pytest.mark.parametrize("bun_price, expected_base_price", [
        (2.5, 5.0),
        (3.0, 6.0),
        (1.75, 3.5),
        (0.0, 0.0),
        (10.0, 20.0),
    ])
    def test_get_price_with_bun_only(self, bun_price, expected_base_price):
        """Тест получения цены только с булочкой"""
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price

        self.burger.set_buns(mock_bun)
        price = self.burger.get_price()

        assert price == expected_base_price

    @pytest.mark.parametrize("ingredients_data, expected_total", [
        ([], 5.0),  # Только булочка
        ([(1.5,)], 6.5),  # Булочка + 1 ингредиент
        ([(1.5,), (3.0,)], 9.5),  # Булочка + 2 ингредиента
        ([(1.5,), (3.0,), (1.75,)], 11.25),  # Булочка + 3 ингредиента
        ([(0.0,)], 5.0),  # Булочка + бесплатный ингредиент
    ])
    def test_get_price_with_various_ingredients(self, ingredients_data, expected_total):
        """Тест получения цены с различными комбинациями ингредиентов"""
        mock_bun = Mock()
        mock_bun.get_price.return_value = 2.5
        self.burger.set_buns(mock_bun)

        for price_data in ingredients_data:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price_data[0]
            self.burger.add_ingredient(mock_ing)

        price = self.burger.get_price()
        assert price == expected_total

    def test_get_price_after_removing_ingredient(self):
        """Тест получения цены после удаления ингредиента"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # 1.5
        self.burger.add_ingredient(self.mock_ingredient2)  # 3.0

        self.burger.remove_ingredient(0)  # Удаляем Ketchup

        price = self.burger.get_price()
        assert price == 8.0  # (2.5 * 2) + 3.0

    def test_get_price_after_moving_ingredient(self):
        """Тест получения цены после перемещения ингредиента"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)

        price_before = self.burger.get_price()
        self.burger.move_ingredient(0, 1)
        price_after = self.burger.get_price()

        assert price_before == price_after

    def test_get_receipt_without_bun_raises_error(self):
        """Тест получения чека без булочки вызывает ошибку"""
        with pytest.raises(AttributeError):
            self.burger.get_receipt()

    def test_get_receipt_with_bun_only(self):
        """Тест получения чека только с булочкой"""
        self.burger.set_buns(self.mock_bun)
        receipt = self.burger.get_receipt()

        expected_lines = [
            "(==== White Bun ====)",
            "(==== White Bun ====)",
            "",
            "Price: 5.0"
        ]
        expected = '\n'.join(expected_lines)

        assert receipt == expected

    @pytest.mark.parametrize("ingredients_info, expected_lines_in_receipt", [
        (
                [("SAUCE", "Ketchup")],
                ["= sauce Ketchup ="]
        ),
        (
                [("FILLING", "Beef Patty")],
                ["= filling Beef Patty ="]
        ),
        (
                [("SAUCE", "Ketchup"), ("FILLING", "Beef Patty")],
                ["= sauce Ketchup =", "= filling Beef Patty ="]
        ),
        (
                [("FILLING", "Cheese"), ("SAUCE", "Mayo"), ("FILLING", "Lettuce")],
                ["= filling Cheese =", "= sauce Mayo =", "= filling Lettuce ="]
        ),
    ])
    def test_get_receipt_with_different_ingredients(self, ingredients_info, expected_lines_in_receipt):
        """Тест получения чека с разными ингредиентами"""
        self.burger.set_buns(self.mock_bun)

        for ing_type, ing_name in ingredients_info:
            mock_ing = Mock()
            mock_ing.get_type.return_value = ing_type
            mock_ing.get_name.return_value = ing_name
            mock_ing.get_price.return_value = 1.0
            self.burger.add_ingredient(mock_ing)

        receipt = self.burger.get_receipt()

        for line in expected_lines_in_receipt:
            assert line in receipt

    def test_get_receipt_type_is_lowercase(self):
        """Тест проверки что тип ингредиента в чеке в нижнем регистре"""
        mock_ing = Mock()
        mock_ing.get_type.return_value = "SAUCE"
        mock_ing.get_name.return_value = "Test Sauce"
        mock_ing.get_price.return_value = 1.0

        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(mock_ing)

        receipt = self.burger.get_receipt()

        assert "= sauce Test Sauce =" in receipt
        assert "= SAUCE Test Sauce =" not in receipt

    def test_get_receipt_after_removing_ingredient(self):
        """Тест получения чека после удаления ингредиента"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)

        self.burger.remove_ingredient(0)

        receipt = self.burger.get_receipt()

        assert "Ketchup" not in receipt
        assert "Beef Patty" in receipt
        assert "Price: 8.0" in receipt

    def test_get_receipt_after_moving_ingredient(self):
        """Тест получения чека после перемещения ингредиента"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # Ketchup
        self.burger.add_ingredient(self.mock_ingredient2)  # Beef Patty

        self.burger.move_ingredient(0, 1)

        receipt = self.burger.get_receipt()

        lines = receipt.split('\n')
        assert "= filling Beef Patty =" in lines[1]
        assert "= sauce Ketchup =" in lines[2]

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
        (2.5, [1.5, 3.0, 1.75], 11.25),
        (3.0, [2.0, 2.5], 10.5),
        (1.0, [0.5], 2.5),
        (5.0, [], 10.0),
    ])
    def test_complete_burger_scenario(self, bun_price, ingredient_prices, expected_total):
        """Тест полного сценария создания бургера"""
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            mock_ing.get_name.return_value = f"Ingredient {price}"
            mock_ing.get_type.return_value = "FILLING"
            burger.add_ingredient(mock_ing)

        assert burger.get_price() == expected_total

        receipt = burger.get_receipt()
        assert "Test Bun" in receipt
        assert f"Price: {expected_total}" in receipt