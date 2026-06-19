import pytest
from unittest.mock import Mock
from praktikum.burger import Burger  as test_class


class TestBurgerSetBuns:
    def test_set_buns_saves_bun(self):
        burger = test_class()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


class TestBurgerAddIngredient:
    def test_add_ingredient_increases_list(self):
        burger = test_class()
        mock_ing = Mock()
        burger.add_ingredient(mock_ing)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ing

    def test_add_multiple_ingredients(self):
        burger = test_class()
        mock_ing1, mock_ing2 = Mock(), Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        assert len(burger.ingredients) == 2


class TestBurgerRemoveIngredient:
    def test_remove_ingredient_deletes_correct_one(self):
        burger = test_class()
        mock_ing1, mock_ing2 = Mock(), Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == mock_ing2
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize("index", [-1, -2])
    def test_remove_ingredient_negative_index(self, index):
        burger = test_class()
        mock_ing1, mock_ing2 = Mock(), Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_out_of_range_raises_error(self):
        burger = test_class()
        mock_ing = Mock()
        burger.add_ingredient(mock_ing)
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)


class TestBurgerMoveIngredient:
    def test_move_ingredient_changes_position(self):
        burger = test_class()
        mock_ing1, mock_ing2 = Mock(), Mock()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ing2
        assert burger.ingredients[1] == mock_ing1


class TestBurgerGetPrice:
    @pytest.mark.parametrize("bun_price, ing_prices, expected", [
        (100, [], 200),
        (100, [50], 250),
        (100, [50, 70], 320),
        (50, [30, 40, 20], 190),
        (0, [], 0),
        (0, [50], 50),
    ])
    def test_get_price_calculates_correctly(self, bun_price, ing_prices, expected):
        burger = test_class()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ing_prices:
            mock_ing = Mock()
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)
        assert burger.get_price() == expected


class TestBurgerGetReceipt:
    @pytest.mark.parametrize("bun_name, ing_data, expected_parts", [
        (
            "Белая булка",
            [],
            ["(==== Белая булка ====)", "(==== Белая булка ====)"]
        ),
        (
            "Чёрная булка",
            [("Чили соус", "sauce", 50)],
            ["(==== Чёрная булка ====)", "= sauce Чили соус =", "(==== Чёрная булка ====)"]
        ),
        (
            "Белая булка",
            [("Котлета", "filling", 100), ("Соус спайси", "sauce", 70)],
            ["(==== Белая булка ====)", "= filling Котлета =", "= sauce Соус спайси =", "(==== Белая булка ====)"]
        ),
    ])
    def test_get_receipt_format(self, bun_name, ing_data, expected_parts):
        burger = test_class()
        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        for name, ing_type, price in ing_data:
            mock_ing = Mock()
            mock_ing.get_name.return_value = name
            mock_ing.get_type.return_value = ing_type
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)
        receipt = burger.get_receipt()
        for part in expected_parts:
            assert part in receipt

    def test_get_receipt_correct_order(self):
        burger = test_class()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        for name, ing_type, price in [("Инг1", "filling", 10), ("Инг2", "sauce", 20)]:
            mock_ing = Mock()
            mock_ing.get_name.return_value = name
            mock_ing.get_type.return_value = ing_type
            mock_ing.get_price.return_value = price
            burger.add_ingredient(mock_ing)
        lines = burger.get_receipt().split('\n')
        assert lines[0] == "(==== Булка ====)"
        assert lines[1] == "= filling Инг1 ="
        assert lines[2] == "= sauce Инг2 ="
        assert lines[3] == "(==== Булка ====)"
        assert lines[4] == ""
        assert lines[5] == "Price: 230"