import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger:
    
    def test_set_buns_sets_bun_reference(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient_increases_count(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_works(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_order(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        
        # Проверяем начальный порядок
        assert burger.ingredients[0] is mock_sauce
        assert burger.ingredients[1] is mock_filling
        
        # Перемещаем
        burger.move_ingredient(0, 1)
        
        # Проверяем измененный порядок
        assert burger.ingredients[0] is mock_filling
        assert burger.ingredients[1] is mock_sauce

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [100, 150], 450),  # 2 булки + 2 ингредиента
        (200, [], 400),  # только булки
        (150, [50, 75, 100], 525),  # булки + 3 ингредиента
    ])
    def test_get_price_with_different_combinations(self, mock_bun, mock_ingredient, 
                                                 bun_price, ingredient_prices, expected_total):
        burger = Burger()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        # Создаем и добавляем ингредиенты
        for i, price in enumerate(ingredient_prices):
            ingredient = mock_ingredient(INGREDIENT_TYPE_SAUCE, f"sauce_{i}", price)
            burger.add_ingredient(ingredient)
        
        assert burger.get_price() == expected_total

    def test_get_receipt_contains_bun_name(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert "black bun" in receipt

    def test_get_receipt_contains_ingredient_info(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert "hot sauce" in receipt
        assert "sauce" in receipt.lower()

    def test_get_receipt_contains_total_price(self, mock_bun, mock_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert "Price:" in receipt
        assert str(burger.get_price()) in receipt