import pytest

from unittest.mock import Mock


class TestBurger:

    def test_init_sets_correct_defaults(self, burger):
        assert burger.bun is None
        assert isinstance(burger.ingredients, list)
        assert len(burger.ingredients) == 0

    def test_set_buns(self, burger):
        mock_bun = Mock() 
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun
        assert burger.bun.get_name() == "black bun"
        assert burger.bun.get_price() == 100.0   

    def test_add_ingredients(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'FILLING'
        mock_ingredient.get_name.return_value = 'dinosaur'
        mock_ingredient.get_price.return_value = 200.0
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_type() == 'FILLING'   
        assert burger.ingredients[0].get_name() == 'dinosaur'
        assert burger.ingredients[0].get_price() == 200.0

    @pytest.mark.parametrize("index_to_remove", [0, 1, 2])
    def test_remove_ingredient (self, burger_with_three_ingredients, index_to_remove):
        burger = burger_with_three_ingredients
        original_list = burger.ingredients
        removed_ingredient = original_list[index_to_remove]
        burger.remove_ingredient(index_to_remove)
        new_list = burger.ingredients
        assert len(new_list) == 2
        assert removed_ingredient not in new_list

    @pytest.mark.parametrize(
        "from_index, to_index",
        [
            (0, 2),
            (2, 0),
            (1, 0),
            (1, 2),
        ],
    )
    def test_move_ingredient_shifts_correctly(self, burger_with_three_ingredients, from_index, to_index):
        burger = burger_with_three_ingredients
        original_list = burger.ingredients
        moved_ingredient = original_list[from_index]

        burger.move_ingredient(from_index, to_index)
        new_list = burger.ingredients

        assert len(new_list) == 3
        assert new_list[to_index] is moved_ingredient

    @pytest.mark.parametrize(
        "bun_price, ing_prices, expected_total",
        [
            (100.0, [50.0, 70.0], 320.0),           
            (0.0,   [10.0, 20.0], 30.0),            
            (200.0, [0.0, 0.0],   400.0),            
            (99.4, [49.5, 30.5], 278.8),         
        ]
    )
    def test_get_price(self, burger_with_mocked_bun_and_ingredients, bun_price, ing_prices, expected_total):
        burger = burger_with_mocked_bun_and_ingredients
        bun = burger.bun
        ingredients = burger.ingredients

        bun.get_price.return_value = bun_price
        for ing, price in zip(ingredients, ing_prices):
            ing.get_price.return_value = price

        actual_price = burger.get_price()

        assert actual_price == pytest.approx(expected_total, rel=1e-9)

    def test_get_receipt_with_bun_and_ingredients(self, burger_with_mocked_bun_and_ingredients):
        
        burger = burger_with_mocked_bun_and_ingredients
        mock_bun = burger.bun
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0

        mock_ingredient_1 = burger.ingredients[0]
        mock_ingredient_1.get_type.return_value = 'FILLING'
        mock_ingredient_1.get_name.return_value = 'dinosaur'
        mock_ingredient_1.get_price.return_value = 200.0

        mock_ingredient_2 = burger.ingredients[1]
        mock_ingredient_2.get_type.return_value = 'SAUCE'
        mock_ingredient_2.get_name.return_value = "hot sauce"
        mock_ingredient_2.get_price.return_value = 100.0
        
        result = burger.get_receipt()
        
        expected_result = (
            "(==== black bun ====)\n"
            "= filling dinosaur =\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 500.0"
        )
        assert result == expected_result

    def test_get_receipt_with_bun_and_no_ingredients(self, burger):
        mock_bun = Mock() 
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        result = burger.get_receipt()
        expected_result = (
            "(==== black bun ====)\n"
            "(==== black bun ====)\n\n"
            "Price: 200.0"
        )
        assert result == expected_result
