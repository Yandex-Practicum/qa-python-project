from unittest.mock import Mock
import pytest

class TestBurger:
    def test_new_burger_has_no_bun_and_no_ingredients(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient(self, burger):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_2]

    @pytest.mark.parametrize("index, expected_left", [
    (0, [1, 2]),
    (1, [0, 2]),
    (2, [0, 1]),
    ])
    def test_remove_ingredient(self, burger, index, expected_left):
        ingredients = [Mock(), Mock(), Mock()]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(index)
        assert burger.ingredients == [ingredients[i] for i in expected_left]

    @pytest.mark.parametrize("start, new, expected_order", [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (1, 1, [0, 1, 2]),
    ])
    def test_move_ingredient(self, burger, start, new, expected_order):
        ingredients = [Mock(), Mock(), Mock()]
        
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        
        burger.move_ingredient(start, new)
        assert burger.ingredients == [ingredients[i] for i in expected_order]

    def test_get_price_calculates_total_price(self, burger, mock_bun, make_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(make_ingredient(price=50))
        burger.add_ingredient(make_ingredient(price=30))
        assert burger.get_price() == (100 * 2) + 50 + 30

    def test_get_receipt(self, burger, mock_bun, make_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(make_ingredient(name="dinosaur", price=50, ingredient_type="FILLING"))
        receipt = burger.get_receipt()
        assert receipt == (
            "(==== black_bun ====)\n"
            "= filling dinosaur =\n"
            "(==== black_bun ====)\n"
            "\n"
            "Price: 250"
        )