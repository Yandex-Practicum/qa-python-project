from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

from unittest.mock import Mock
import pytest



class TestBurgerInitialization:

    # Тест 1: Добавление булки
    def test_set_bun_sets_correctly(self, burger_instance, mock_bun):
        burger_instance.set_buns(mock_bun)
        assert burger_instance.bun == mock_bun
        assert burger_instance.bun.get_name() == 'Test Bun Name'

    # Тест 2: Добавление ингридиентов в конец списка
    def test_add_ingredient_appends_to_list(self, burger_instance, mock_ingredient):
        assert len(burger_instance.ingredients) == 0
        burger_instance.add_ingredient(mock_ingredient)
        assert len(burger_instance.ingredients) == 1
        assert burger_instance.ingredients[0] == mock_ingredient
    
    
class TestBurgerManipulation:


    # Тест 1: Удаление (Позитивный)
    def test_remove_ingredient_removes_correctly(self, burger_instance, mock_ingredient, mock_two_ingredient):
        burger_instance.add_ingredient(mock_ingredient)
        burger_instance.add_ingredient(mock_two_ingredient)
        assert len(burger_instance.ingredients) == 2
        burger_instance.remove_ingredient(0)
        assert len(burger_instance.ingredients) == 1
        assert burger_instance.ingredients[0] == mock_two_ingredient


    # Тест 2: Удаление (Негативный / Ошибка)
    def test_remove_ingredient_raises_error_on_invalid_index(self, burger_instance, mock_ingredient):
        burger_instance.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
           burger_instance.remove_ingredient(99)

    # Тест 3: Перемещение (Позитивный) ---
    def test_move_ingredient_changes_order(self, burger_instance, mock_ingredient_a, mock_ingredient_b, mock_ingredient_c):
        burger_instance.add_ingredient(mock_ingredient_a)
        burger_instance.add_ingredient(mock_ingredient_b)
        burger_instance.add_ingredient(mock_ingredient_c)
        burger_instance.move_ingredient(0, 2)
        assert burger_instance.ingredients[0] == mock_ingredient_b
        assert burger_instance.ingredients[1] == mock_ingredient_c
        assert burger_instance.ingredients[2] == mock_ingredient_a


    # Тест 4: Перемещение (Негативный / Ошибка)
    def test_move_ingredient_raises_error_on_invalid_index(self, burger_instance, mock_ingredient):
        burger_instance.add_ingredient(mock_ingredient)
        with pytest.raises(IndexError):
            burger_instance.move_ingredient(5, 0)


class TestBurgerPrice:

    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_total", [
    (100, [], 200),
    (150, [50], 350),
    (200, [10, 20], 430),])

    def test_get_price_calculation(self, burger_instance, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = "Test Bun" 
        burger_instance.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            mock_ingredient.get_type.return_value = "FILLING"
            mock_ingredient.get_name.return_value = "Test Ingredient"
            burger_instance.add_ingredient(mock_ingredient)
        actual_price = burger_instance.get_price()
        assert actual_price == expected_total


class TestBurgerReceipt:


    @pytest.mark.parametrize("bun_name, ing_type, ing_name, expected_ing_type_lower",[
    ('White Bun', "FILLING", "Meat Ball", "filling" ),
    ("Black Bun", "SAUCE", "Hot Sauce", "sauce"),
    ("Red Bun", "SaUcE", "Ketchup","sauce"),
    ])
    def test_get_receipt_format(self, burger_instance, bun_name, ing_name, ing_type, expected_ing_type_lower):
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 1500

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ing_type
        mock_ingredient.get_name.return_value =  ing_name
        mock_ingredient.get_price.return_value = 420

        expected_price = (1500*2) + 420

        burger_instance.set_buns(mock_bun)
        burger_instance.add_ingredient(mock_ingredient)
        expected_receipt = f"(==== {bun_name} ====)\n= {expected_ing_type_lower} {ing_name} =\n(==== {bun_name} ====)\n\nPrice: {expected_price}"
        actual_receipt = burger_instance.get_receipt()
        assert actual_receipt == expected_receipt
