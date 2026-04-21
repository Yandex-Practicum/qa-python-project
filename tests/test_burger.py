import pytest
from unittest.mock import Mock


class TestBurger:
    
    def test_set_buns_sets_bun_correctly(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun
    
    def test_add_ingredient_adds_ingredient_to_list(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient_sauce
    
    def test_remove_ingredient_removes_ingredient_by_index(self, burger_with_ingredients):
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(0)
        
        assert len(burger_with_ingredients.ingredients) == initial_count - 1
    
    def test_move_ingredient_moves_ingredient_to_new_position(self, burger_with_ingredients):
        first_ingredient_before = burger_with_ingredients.ingredients[0]
        burger_with_ingredients.move_ingredient(0, 1)  

        assert burger_with_ingredients.ingredients[1] == first_ingredient_before
    
    def test_get_price_calculates_correct_price(self, burger_with_ingredients, mock_bun, 
                                                mock_ingredient_sauce, mock_ingredient_filling):

        mock_bun.get_price.return_value = 100.0
        mock_ingredient_sauce.get_price.return_value = 90.0
        mock_ingredient_filling.get_price.return_value = 200.0
        
        expected_price = 100.0 * 2 + 90.0 + 200.0 
        price = burger_with_ingredients.get_price()

        assert price == expected_price

    
    def test_get_receipt_returns_correct_format(self, burger_with_ingredients, mock_bun,
                                                mock_ingredient_sauce, mock_ingredient_filling):

        mock_bun.get_name.return_value = "Краторная булка N-200i"
        mock_ingredient_sauce.get_type.return_value = "SAUCE"
        mock_ingredient_sauce.get_name.return_value = "Соус Spicy-X"
        mock_ingredient_filling.get_type.return_value = "FILLING"
        mock_ingredient_filling.get_name.return_value = "Мясо бессмертных моллюсков Protostomia"
        
        mock_bun.get_price.return_value = 100.0
        mock_ingredient_sauce.get_price.return_value = 90.0
        mock_ingredient_filling.get_price.return_value = 200.0
        
        receipt = burger_with_ingredients.get_receipt()
        
        expected_receipt = (
            "(==== Краторная булка N-200i ====)\n"
            "= sauce Соус Spicy-X =\n"
            "= filling Мясо бессмертных моллюсков Protostomia =\n"
            "(==== Краторная булка N-200i ====)\n\n"
            "Price: 490.0"
        )
        assert receipt == expected_receipt
    
    def test_remove_ingredient_with_invalid_index_raises_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
    
    def test_move_ingredient_with_invalid_index_raises_error(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 0)
    
    def test_get_price_without_bun_raises_attribute_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()