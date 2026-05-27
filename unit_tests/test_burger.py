import pytest
from unittest.mock import Mock


class TestBurger:

    def test_init_burger_has_empty_attributes(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []
        assert isinstance(burger.ingredients, list)

    def test_set_buns_successfully_sets_bun(self, burger):
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize(
        "index_to_remove, expected_remaining_indices",
        [
            (0, [1, 2]), 
            (1, [0, 2]),
            (2, [0, 1]),
        ]
    )
    def test_remove_ingredient_deletes_by_index(self, burger, index_to_remove, expected_remaining_indices):
        mocks = [Mock(name="ing_0"), Mock(name="ing_1"), Mock(name="ing_2")]
        burger.ingredients = mocks.copy()

        burger.remove_ingredient(index_to_remove)

        expected_mocks = [mocks[i] for i in expected_remaining_indices]
        assert burger.ingredients == expected_mocks

    @pytest.mark.parametrize(
        "from_index, to_index, expected_order",
        [
            (0, 2, [1, 2, 0]),
            (2, 0, [2, 0, 1]),
            (1, 0, [1, 0, 2]), 
        ]
    )
    def test_move_ingredient_changes_position(self, burger, from_index, to_index, expected_order):
        mocks = [Mock(name="ing_0"), Mock(name="ing_1"), Mock(name="ing_2")]
        burger.ingredients = mocks.copy()
        
        burger.move_ingredient(from_index, to_index)

        expected_mocks = [mocks[i] for i in expected_order]
        assert burger.ingredients == expected_mocks

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        [
            (100.0, [50.0, 30.0], 280.0),
            (0.0, [15.0], 15.0),
            (120.5, [], 241.0),
        ]
    )
    def test_get_price_calculates_correct_total(self, burger, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredients = []
        for price in ingredient_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            mock_ingredients.append(mock_ing)
            
        burger.ingredients = mock_ingredients

        assert burger.get_price() == expected_total

    @pytest.mark.parametrize(
        "ing_type, ing_name, ing_price, expected_middle_line, expected_price",
        [
            ("SAUCE", "chili", 50.0, "= sauce chili =", "250.0"),
            ("FILLING", "dinosaur back", 200.0, "= filling dinosaur back =", "400.0")
        ]
    )
    def test_get_receipt_returns_formatted_string(self, burger, ing_type, ing_name, ing_price, expected_middle_line, expected_price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ing_type
        mock_ingredient.get_name.return_value = ing_name
        mock_ingredient.get_price.return_value = ing_price
        burger.ingredients = [mock_ingredient]

        expected_receipt = (
            f"(==== black bun ====)\n"
            f"{expected_middle_line}\n"
            f"(==== black bun ====)\n\n"
            f"Price: {expected_price}"
        )

        assert burger.get_receipt() == expected_receipt