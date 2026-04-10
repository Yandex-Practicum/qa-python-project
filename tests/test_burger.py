import pytest
from unittest.mock import Mock

class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_first(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2

    def test_remove_ingredient_last(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing1

    def test_remove_ingredient_single(self, burger):
        ing = Mock()
        burger.add_ingredient(ing)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_invalid_index(self, burger):
        ing = Mock()
        burger.add_ingredient(ing)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    def test_move_ingredient_same_index(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == ing1
        assert burger.ingredients[1] == ing2

    def test_move_ingredient(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    def test_move_ingredient_from_end_to_start(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing1

    def test_get_price_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        expected_price = mock_bun.get_price() * 2
        assert burger.get_price() == expected_price

    def test_get_price_no_bun(self, burger):
        ing = Mock()
        burger.add_ingredient(ing)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_no_bun(self, burger):
        ing = Mock()
        burger.add_ingredient(ing)
        with pytest.raises(AttributeError):
            burger.get_receipt()

    @pytest.mark.parametrize("sauce_count, filling_count", [
        (0, 0),
        (1, 0),
        (1, 1)
    ])
    def test_get_receipt(self, burger, mock_bun, mock_sauce, mock_filling, sauce_count, filling_count):
        burger.set_buns(mock_bun)
        ingredients = []

        for _ in range(sauce_count):
            burger.add_ingredient(mock_sauce)
            ingredients.append(mock_sauce)
        for _ in range(filling_count):
            burger.add_ingredient(mock_filling)
            ingredients.append(mock_filling)

        bun_price = mock_bun.get_price()
        total_price = bun_price * 2 + sum(ing.get_price() for ing in ingredients)

        lines = [f"(==== {mock_bun.get_name()} ====)"]
        for ing in burger.ingredients:
            lines.append(f"= {ing.get_type()} {ing.get_name()} =")
        lines.append(f"(==== {mock_bun.get_name()} ====)")
        lines.append("")
        lines.append(f"Price: {total_price}")
        expected = "\n".join(lines)

        assert burger.get_receipt() == expected

    def test_get_price_without_bun_and_ingredients(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_move_ingredient_invalid_index(self, burger):
        ing = Mock()
        burger.add_ingredient(ing)
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)
        with pytest.raises(IndexError):
            burger.move_ingredient(-2, 0)
        burger.move_ingredient(0, 5)
        