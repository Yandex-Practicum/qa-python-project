import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Краторная булка"
        mock_bun.get_price.return_value = 200

        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "Соус Spicy-X"
        mock_ingredient.get_price.return_value = 90

        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize("ingredient_count", [1, 3, 5])
    def test_add_multiple_ingredients(self, ingredient_count):
        burger = Burger()

        for i in range(ingredient_count):
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
            mock_ingredient.get_name.return_value = f"Ингредиент {i}"
            mock_ingredient.get_price.return_value = 100 + i
            burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == ingredient_count

    def test_remove_ingredient(self):
        burger = Burger()

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        assert len(burger.ingredients) == 3

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_ingredient1
        assert burger.ingredients[1] == mock_ingredient3

    @pytest.mark.parametrize("index_to_remove,expected_remaining", [
        (0, 2),
        (1, 2),
        (2, 2),
    ])
    def test_remove_ingredient_parameterized(self, index_to_remove, expected_remaining):
        """Параметризованный тест удаления ингредиентов"""
        burger = Burger()

        # Добавляем 3 mock ингредиента
        for i in range(3):
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_name.return_value = f"Ингредиент {i}"
            burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(index_to_remove)
        assert len(burger.ingredients) == expected_remaining

    def test_move_ingredient(self):
        burger = Burger()

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_name.return_value = "Первый"
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = "Второй"
        mock_ingredient3 = Mock(spec=Ingredient)
        mock_ingredient3.get_name.return_value = "Третий"

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient3
        assert burger.ingredients[2] == mock_ingredient1

    @pytest.mark.parametrize("from_index,to_index,expected_order", [
        (0, 2, ["Второй", "Третий", "Первый"]),
        (2, 0, ["Третий", "Первый", "Второй"]),
        (1, 1, ["Первый", "Второй", "Третий"]),
    ])
    def test_move_ingredient_parameterized(self, from_index, to_index, expected_order):
        """Параметризованный тест перемещения ингредиентов"""
        burger = Burger()

        ingredients_data = [
            ("Первый", Mock(spec=Ingredient)),
            ("Второй", Mock(spec=Ingredient)),
            ("Третий", Mock(spec=Ingredient))
        ]

        for name, mock in ingredients_data:
            mock.get_name.return_value = name
            burger.add_ingredient(mock)

        burger.move_ingredient(from_index, to_index)
        actual_order = [ing.get_name() for ing in burger.ingredients]
        assert actual_order == expected_order

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [50, 75], 325),
        (150, [30, 45, 60], 435),
        (200, [], 400),
        (50, [10], 110),
    ])
    def test_get_price_parameterized(self, bun_price, ingredient_prices, expected_total):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_total

    def test_get_receipt_with_bun_and_ingredients(self):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Сезонная булка"
        mock_bun.get_price.return_value = 45
        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "Сыр"
        mock_ingredient1.get_price.return_value = 25

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "Котлета"
        mock_ingredient2.get_price.return_value = 35

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        receipt = burger.get_receipt()

        assert "Сезонная булка" in receipt
        assert "sauce Сыр" in receipt
        assert "filling Котлета" in receipt
        assert "150" in receipt

    def test_get_receipt_without_bun_raises_error(self):
        """Тестируем, что get_receipt() падает с ошибкой при отсутствии булки"""
        burger = Burger()

        # Не добавляем булку специально
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "Салат"
        mock_ingredient.get_price.return_value = 15
        burger.add_ingredient(mock_ingredient)

        # Проверяем, что метод действительно падает с AttributeError
        with pytest.raises(AttributeError) as exc_info:
            burger.get_receipt()

        # Проверяем, что ошибка связана с отсутствием get_name у None
        assert "'NoneType' object has no attribute 'get_name'" in str(exc_info.value)

    def test_get_receipt_only_bun(self):
        """Тестируем чек для бургера только с булкой"""
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        assert "Булка" in receipt
        assert "Price:" in receipt

    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt_calls_get_price(self, mock_get_price):
        mock_get_price.return_value = 999

        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Булка"
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        mock_get_price.assert_called_once()
        assert "Price: 999" in receipt