import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Класс с юнит-тестами для модели бургера Burger."""

    def test_init_default_values(self):
        """Проверяем, что при инициализации булочка пустая, а список ингредиентов пуст."""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        """Проверяем корректность установки булочки в бургер."""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        """Проверяем добавление ингредиента в бургер."""
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient)
        
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        """Проверяем удаление ингредиента по индексу."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        burger.remove_ingredient(0)
        
        assert mock_ingredient1 not in burger.ingredients
        assert burger.ingredients == [mock_ingredient2]

    def test_move_ingredient(self):
        """Проверяем перемещение ингредиента с одной позиции на другую."""
        burger = Burger()
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient3 = Mock(spec=Ingredient)
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        # Перемещаем ингредиент с индекса 2 на индекс 0
        burger.move_ingredient(2, 0)
        
        assert burger.ingredients == [mock_ingredient3, mock_ingredient1, mock_ingredient2]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_price",
        [
            (100, [50, 75], 325),   # Булочка (100*2) + два ингредиента
            (200, [], 400),         # Только булочка (200*2), без ингредиентов
            (50, [10, 20, 30], 160) # Булочка (50*2) + три ингредиента
        ]
    )
    def test_get_price(self, bun_price, ingredient_prices, expected_price):
        """Проверяем корректность подсчета стоимости бургера (с параметризацией)."""
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ing = Mock(spec=Ingredient)
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)
            
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("ing_type, expected_type_str", [
        (INGREDIENT_TYPE_SAUCE, "sauce"),
        (INGREDIENT_TYPE_FILLING, "filling")
    ])
    def test_get_receipt_with_one_ingredient(self, ing_type, expected_type_str):
        """Проверяем генерацию чека с одним ингредиентом (параметризация типов)."""
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        
        mock_ing = Mock(spec=Ingredient)
        mock_ing.get_type.return_value = ing_type
        mock_ing.get_name.return_value = "test ingredient"
        mock_ing.get_price.return_value = 50
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)
        
        # Ожидаемая строка чека (обрати внимание на переносы строк \n)
        expected_receipt = (
            "(==== black bun ====)\n"
            f"= {expected_type_str} test ingredient =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 250"
        )
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_without_ingredients(self):
        """Проверяем генерацию чека без ингредиентов (покрываем пустой цикл for)."""
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200
        
        burger.set_buns(mock_bun)
        
        expected_receipt = (
            "(==== white bun ====)\n"
            "(==== white bun ====)\n"
            "\n"
            "Price: 400"
        )
        assert burger.get_receipt() == expected_receipt