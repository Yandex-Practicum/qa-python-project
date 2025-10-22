import pytest
from unittest.mock import Mock


class TestBurgerParametrized:
    
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [50], 250),  
        (200, [80, 70], 550),  
        (150, [40, 30, 60], 430),  
        (100, [], 200),  
        (50, [10, 20, 30, 40], 200),  
        (300, [150], 750),  
    ])
    def test_get_price_parametrized(self, burger, bun_price, ingredient_prices, expected_total):
        bun_mock = Mock()
        bun_mock.get_name.return_value = "test bun"
        bun_mock.get_price.return_value = bun_price
        
        ingredient_mocks = []
        for i, price in enumerate(ingredient_prices):
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = "SAUCE"
            ingredient_mock.get_name.return_value = f"ingredient_{i}"
            ingredient_mock.get_price.return_value = price
            ingredient_mocks.append(ingredient_mock)
        
        burger.set_buns(bun_mock)
        for ingredient_mock in ingredient_mocks:
            burger.add_ingredient(ingredient_mock)
        
        assert burger.get_price() == expected_total

    @pytest.mark.parametrize("bun_name,ingredient_types,ingredient_names", [
        ("black bun", ["SAUCE"], ["hot sauce"]),
        ("white bun", ["FILLING", "SAUCE"], ["cutlet", "chili sauce"]),
        ("red bun", ["FILLING", "FILLING", "SAUCE"], ["cheese", "salad", "sour cream"]),
    ])
    def test_get_receipt_contains_all_names_parametrized(self, burger, bun_name, ingredient_types, ingredient_names):
        bun_mock = Mock()
        bun_mock.get_name.return_value = bun_name
        bun_mock.get_price.return_value = 100
        
        burger.set_buns(bun_mock)
        
        for i, (ing_type, ing_name) in enumerate(zip(ingredient_types, ingredient_names)):
            ingredient_mock = Mock()
            ingredient_mock.get_type.return_value = ing_type
            ingredient_mock.get_name.return_value = ing_name
            ingredient_mock.get_price.return_value = 50
            burger.add_ingredient(ingredient_mock)
        
        receipt = burger.get_receipt()
        
        assert receipt.count(f"(==== {bun_name} ====)") == 2
        
        for ing_name in ingredient_names:
            assert ing_name in receipt
        
        assert "Price:" in receipt

    @pytest.mark.parametrize("ingredient_count", [0, 1, 3, 5])
    def test_ingredient_count_affects_price(self, burger, ingredient_count):
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = "test bun"
        
        burger.set_buns(bun_mock)
        
        expected_price = 200 
        
        for i in range(ingredient_count):
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = 50
            ingredient_mock.get_name.return_value = f"ingredient_{i}"
            ingredient_mock.get_type.return_value = "FILLING"
            burger.add_ingredient(ingredient_mock)
            expected_price += 50
        
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("bun_price1,bun_price2,expected_total", [
        (100, 100, 200),  
        (100, 200, 400), 
    ])
    def test_set_buns_replaces_previous_bun(self, burger, bun_price1, bun_price2, expected_total):
        bun_mock1 = Mock()
        bun_mock1.get_price.return_value = bun_price1
        bun_mock1.get_name.return_value = "first bun"
        burger.set_buns(bun_mock1)
        
        bun_mock2 = Mock()
        bun_mock2.get_price.return_value = bun_price2
        bun_mock2.get_name.return_value = "second bun"
        burger.set_buns(bun_mock2)
        
        assert burger.get_price() == expected_total

    @pytest.mark.parametrize("initial_count,remove_index,final_count", [
        (3, 0, 2),  
        (3, 1, 2),  
        (3, 2, 2),  
        (1, 0, 0),  
    ])
    def test_remove_ingredient_parametrized(self, burger, initial_count, remove_index, final_count):
        for i in range(initial_count):
            ingredient_mock = Mock()
            ingredient_mock.get_name.return_value = f"ingredient_{i}"
            ingredient_mock.get_type.return_value = "FILLING"
            ingredient_mock.get_price.return_value = 50
            burger.add_ingredient(ingredient_mock)
        
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = "test bun"
        burger.set_buns(bun_mock)
        
        price_before = burger.get_price()
        
        burger.remove_ingredient(remove_index)
        
        assert len(burger.ingredients) == final_count
        
        if initial_count > 0:
            assert burger.get_price() == price_before - 50

    @pytest.mark.parametrize("from_index,to_index,expected_order", [
        (0, 2, [1, 2, 0]),  
        (2, 0, [2, 0, 1]),  
        (1, 1, [0, 1, 2]),  
    ])
    def test_move_ingredient_parametrized(self, burger, from_index, to_index, expected_order):
        ingredients = []
        for i in range(3):
            ingredient_mock = Mock()
            ingredient_mock.get_name.return_value = f"ingredient_{i}"
            ingredient_mock.get_type.return_value = "FILLING"
            ingredient_mock.get_price.return_value = 50
            ingredients.append(ingredient_mock)
            burger.add_ingredient(ingredient_mock)
        
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = "test bun"
        burger.set_buns(bun_mock)
        
        burger.move_ingredient(from_index, to_index)
        
        for i, expected_idx in enumerate(expected_order):
            assert burger.ingredients[i].get_name() == f"ingredient_{expected_idx}"

    @pytest.mark.parametrize("ingredient_prices,expected_total_price", [
        ([], 200),           
        ([50], 250),         
        ([50, 80], 330),     
        ([50, 80, 40], 370), 
    ])
    def test_receipt_price_matches_calculation(self, burger, ingredient_prices, expected_total_price):
        bun_mock = Mock()
        bun_mock.get_price.return_value = 100
        bun_mock.get_name.return_value = "test bun"
        
        burger.set_buns(bun_mock)
        
        for i, price in enumerate(ingredient_prices):
            ingredient_mock = Mock()
            ingredient_mock.get_price.return_value = price
            ingredient_mock.get_name.return_value = f"ingredient_{i}"
            ingredient_mock.get_type.return_value = "FILLING"
            burger.add_ingredient(ingredient_mock)
        
        receipt = burger.get_receipt()
        
        assert f"Price: {expected_total_price}" in receipt
        assert burger.get_price() == expected_total_price