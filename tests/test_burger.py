import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        mock_ing_1 = Mock()
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ing_1)
        burger.add_ingredient(mock_ing_2)
        
        # Перемещаем первый элемент на место второго
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ing_2, mock_ing_1]

    @pytest.mark.parametrize(
        "bun_price, ingredient_price, expected_total",
        [
            (100.0, 50.0, 250.0),   # (100 * 2) + 50 = 250
            (0.0, 75.0, 75.0),      # (0 * 2) + 75 = 75
            (250.0, 0.0, 500.0),    # (250 * 2) + 0 = 500
        ]
    )
    def test_get_price(self, bun_price, ingredient_price, expected_total):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_total

    def test_get_receipt(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 50.0
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        # Строгая сверка вёрстки чека по вашей заготовке
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "Price: 250.0" in receipt
