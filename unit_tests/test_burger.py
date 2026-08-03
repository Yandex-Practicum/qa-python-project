import sys
import os
from pathlib import Path

# Добавляем корневую директорию в PYTHONPATH
root_dir = str(Path(__file__).parent.parent)
sys.path.insert(0, root_dir)

import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:
    """Тесты для класса Burger"""

    def test_burger_initialization(self, burger):
        """Тест инициализации бургера"""
        assert burger.bun is None

    def test_burger_ingredients_initialization(self, burger):
        """Тест инициализации списка ингредиентов"""
        assert len(burger.ingredients) == 0

    def test_set_buns_with_real_bun(self, burger):
        """Тест установки булочки с реальными данными"""
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize("bun_name, bun_price", [
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_set_buns_with_different_buns(self, burger, bun_name, bun_price):
        """Тест установки разных булочек"""
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == bun_name

    def test_set_buns_with_mock(self, burger, mock_bun):
        """Тест установки булочки с использованием мока"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_with_real_ingredient(self, burger):
        """Тест добавления ингредиента с реальными данными"""
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", [
        ("FILLING", "cutlet", 150),
        ("SAUCE", "chili sauce", 200),
    ])
    def test_add_different_ingredients(self, burger, ingredient_type, ingredient_name, ingredient_price):
        """Тест добавления разных ингредиентов"""
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].get_name() == ingredient_name

    def test_add_ingredient_with_mock(self, burger, mock_ingredient_sauce):
        """Тест добавления ингредиента с использованием мока"""
        burger.add_ingredient(mock_ingredient_sauce)
        assert burger.ingredients[0] == mock_ingredient_sauce

    def test_add_multiple_ingredients(self, burger, mock_ingredient_sauce):
        """Тест добавления нескольких ингредиентов"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 3

    def test_remove_ingredient_first(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест удаления первого ингредиента"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_remove_ingredient_last(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест удаления последнего ингредиента"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.remove_ingredient(1)
        assert burger.ingredients[0] == mock_ingredient_sauce

    @pytest.mark.parametrize("remove_index", [0, 1, 2])
    def test_remove_ingredient_by_index(self, burger, mock_ingredient_sauce, 
                                        mock_ingredient_filling, mock_ingredient_extra, remove_index):
        """Тест удаления ингредиента по индексу"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_extra)
        burger.remove_ingredient(remove_index)
        assert len(burger.ingredients) == 2

    def test_move_ingredient_forward(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест перемещения ингредиента вперед"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_move_ingredient_backward(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест перемещения ингредиента назад"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_move_ingredient_to_same_position(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест перемещения ингредиента на ту же позицию"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == mock_ingredient_sauce

    @pytest.mark.parametrize("from_index, to_index", [(0, 2), (2, 0), (1, 3)])
    def test_move_ingredient_different_positions(self, burger, mock_ingredient_sauce, 
                                                  mock_ingredient_filling, mock_ingredient_extra,
                                                  from_index, to_index):
        """Тест перемещения ингредиента на разные позиции"""
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_extra)
        burger.add_ingredient(mock_ingredient_sauce)
        original_length = len(burger.ingredients)
        burger.move_ingredient(from_index, to_index)
        assert len(burger.ingredients) == original_length

    def test_get_price_without_bun(self, burger, mock_ingredient_sauce):
        """Тест получения цены без булочки - должно вызвать ошибку"""
        burger.add_ingredient(mock_ingredient_sauce)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_price_with_bun_only(self, burger):
        """Тест получения цены только с булочкой"""
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200

    @pytest.mark.parametrize("bun_price, expected_price", [(150, 300), (200, 400)])
    def test_get_price_with_different_bun_prices(self, burger, bun_price, expected_price):
        """Тест получения цены с разными ценами булочки"""
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        assert burger.get_price() == expected_price

    def test_get_price_with_one_ingredient(self, burger):
        """Тест получения цены с булочкой и одним ингредиентом"""
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250

    def test_get_price_with_multiple_ingredients(self, burger):
        """Тест получения цены с булочкой и несколькими ингредиентами"""
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 75
        mock_ingredient3 = Mock()
        mock_ingredient3.get_price.return_value = 30
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        
        assert burger.get_price() == 355

    def test_get_receipt_without_bun(self, burger, mock_ingredient_sauce):
        """Тест получения чека без булочки - должно вызвать ошибку"""
        burger.add_ingredient(mock_ingredient_sauce)
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_with_bun_only(self, burger):
        """Тест получения чека только с булочкой"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        expected_receipt = """(==== black bun ====)
(==== black bun ====)

Price: 200"""
        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize("bun_name", [("white bun"), ("red bun")])
    def test_get_receipt_with_different_bun_names(self, burger, bun_name):
        """Тест получения чека с разными названиями булочек"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        expected_receipt = f"""(==== {bun_name} ====)
(==== {bun_name} ====)

Price: 200"""
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_one_ingredient(self, burger):
        """Тест получения чека с булочкой и одним ингредиентом"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        
        expected_receipt = """(==== test bun ====)
= sauce hot sauce =
(==== test bun ====)

Price: 250"""
        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize("ingredient_type, ingredient_name", [
        ("FILLING", "cutlet"),
        ("SAUCE", "chili sauce"),
    ])
    def test_get_receipt_with_different_ingredients(self, burger, ingredient_type, ingredient_name):
        """Тест получения чека с разными ингредиентами"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        
        expected_receipt = f"""(==== test bun ====)
= {ingredient_type.lower()} {ingredient_name} =
(==== test bun ====)

Price: 250"""
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_multiple_ingredients(self, burger):
        """Тест получения чека с несколькими ингредиентами"""
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = "SAUCE"
        mock_ingredient1.get_name.return_value = "sauce1"
        mock_ingredient1.get_price.return_value = 50
        
        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = "FILLING"
        mock_ingredient2.get_name.return_value = "filling1"
        mock_ingredient2.get_price.return_value = 75
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        expected_receipt = """(==== test bun ====)
= sauce sauce1 =
= filling filling1 =
(==== test bun ====)

Price: 325"""
        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_mock_verification(self, burger, mock_bun, mock_ingredient_sauce):
        """Тест проверки вызовов моков при получении чека"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.get_receipt()
        
        mock_bun.get_name.assert_called()

    def test_get_receipt_mock_ingredient_verification(self, burger, mock_bun, mock_ingredient_sauce):
        """Тест проверки вызова метода get_type у ингредиента"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.get_receipt()
        
        mock_ingredient_sauce.get_type.assert_called_once()

    def test_complex_operations_add_ingredients(self, burger, mock_bun, mock_ingredient_sauce,
                                                 mock_ingredient_filling, mock_ingredient_extra):
        """Тест добавления нескольких ингредиентов в сложной операции"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_extra)
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 4

    def test_complex_operations_move_ingredients(self, burger, mock_bun, mock_ingredient_sauce,
                                                  mock_ingredient_filling, mock_ingredient_extra):
        """Тест перемещения ингредиентов в сложной операции"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_extra)
        burger.add_ingredient(mock_ingredient_sauce)
        
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == mock_ingredient_filling

    def test_complex_operations_remove_ingredients(self, burger, mock_bun, mock_ingredient_sauce,
                                                    mock_ingredient_filling, mock_ingredient_extra):
        """Тест удаления ингредиентов в сложной операции"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_extra)
        burger.add_ingredient(mock_ingredient_sauce)
        
        burger.remove_ingredient(2)
        assert len(burger.ingredients) == 3

    def test_complex_operations_calculate_price(self, burger, mock_bun, mock_ingredient_sauce):
        """Тест расчета цены в сложной операции"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_sauce)
        
        mock_bun.get_price.return_value = 100
        mock_ingredient_sauce.get_price.return_value = 50
        assert burger.get_price() == 300

    @pytest.mark.parametrize("operation", ["add", "remove", "move"])
    def test_operations_with_mocks(self, burger, mock_ingredient_sauce, operation):
        """Тест различных операций с использованием моков"""
        if operation == "add":
            burger.add_ingredient(mock_ingredient_sauce)
            assert len(burger.ingredients) == 1
        elif operation == "remove":
            burger.add_ingredient(mock_ingredient_sauce)
            burger.remove_ingredient(0)
            assert len(burger.ingredients) == 0
        elif operation == "move":
            burger.add_ingredient(mock_ingredient_sauce)
            burger.add_ingredient(mock_ingredient_sauce)
            burger.move_ingredient(0, 1)
            assert len(burger.ingredients) == 2