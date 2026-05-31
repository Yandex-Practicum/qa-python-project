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
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2

    @pytest.mark.parametrize("index, new_index, expected_order", [
        (0, 1, [1, 0, 2]),
        (2, 0, [2, 0, 1]),
        (1, 1, [0, 1, 2])
    ])
    def test_move_ingredient(self, index, new_index, expected_order):
        burger = Burger()
        ingredients = [Mock(), Mock(), Mock()]
        for ing in ingredients:
            burger.add_ingredient(ing)
        burger.move_ingredient(index, new_index)
        moved_order = [burger.ingredients[i] for i in range(3)]
        expected_list = [ingredients[i] for i in expected_order]
        assert moved_order == expected_list

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)
        ing1 = Mock()
        ing1.get_price.return_value = 30
        ing2 = Mock()
        ing2.get_price.return_value = 20
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        assert burger.get_price() == 50 * 2 + 30 + 20

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "sesame bun"
        mock_bun.get_price.return_value = 50
        burger.set_buns(mock_bun)

        mock_ing1 = Mock()
        mock_ing1.get_type.return_value = "SAUCE"
        mock_ing1.get_name.return_value = "ketchup"
        mock_ing1.get_price.return_value = 10
        mock_ing2 = Mock()
        mock_ing2.get_type.return_value = "FILLING"
        mock_ing2.get_name.return_value = "cheese"
        mock_ing2.get_price.return_value = 20

        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        expected_price = 50 * 2 + 10 + 20
        expected_receipt = (
            "(==== sesame bun ====)\n"
            "= sauce ketchup =\n"
            "= filling cheese =\n"
            "(==== sesame bun ====)\n"
            "\n"  # пустая строка из-за лишнего \n в конце предпоследней строки чека
            f"Price: {expected_price}"
        )
        assert burger.get_receipt() == expected_receipt