# version: v1.2


from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты класса Burger."""

    # Тесты set_buns.
    # - test_set_buns_sets_bun: проверяет базовый сценарий первого вызова метода.
    # - test_set_buns_uses_latest_bun: проверяет сценарий повторного вызова метода (обновление состояния)

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

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 250"
        )

        assert receipt == expected_receipt
