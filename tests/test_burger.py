from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:
    def test_set_buns_sets_correct_bun(self):
        burger = Burger()
        mock_bun = Mock()
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        
        burger.add_ingredient(mock_ingredient)
        
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_removes_ingredient_from_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.ingredients.append(mock_ingredient)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_ingredient_index(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients.extend([mock_ingredient_1, mock_ingredient_2])
        
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price_calculates_correct_total_price(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == 250

    def test_get_receipt_returns_correct_string(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Белая булка"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "Острый соус"
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        assert "Белая булка" in receipt
        assert "Острый соус" in receipt
        assert "250" in receipt