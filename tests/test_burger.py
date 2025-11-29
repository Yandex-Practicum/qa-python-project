# version: v1.4

from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты класса Burger."""

    def test_set_buns_sets_bun(self, burger):
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_set_buns_uses_latest_bun(self, burger):
        first_bun = Mock()
        second_bun = Mock()

        burger.set_buns(first_bun)
        burger.set_buns(second_bun)

        assert burger.bun == second_bun

    def test_get_receipt_returns_correct_value(self, burger):
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100

        ing = Mock()
        ing.get_name.return_value = "hot sauce"
        ing.get_price.return_value = 50
        ing.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.set_buns(bun)
        burger.add_ingredient(ing)

        receipt = burger.get_receipt()

        expected_price = bun.get_price() * 2 + ing.get_price()

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            f"Price: {expected_price}"
        )

        assert receipt == expected_receipt

    def test_remove_ingredient_removes_by_index(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        ing3 = Mock()

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.remove_ingredient(1)

        assert burger.ingredients == [ing1, ing3]

    def test_move_ingredient_moves_to_new_index(self, burger):
        ing1 = Mock()
        ing2 = Mock()
        ing3 = Mock()

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]
