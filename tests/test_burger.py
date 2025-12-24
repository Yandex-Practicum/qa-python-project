import pytest
from praktikum.burger import Burger

class TestBurger:

    def test_new_burger_has_no_bun(self, empty_burger):
        assert empty_burger.bun is None

    def test_new_burger_has_no_ingredients(self, empty_burger):
        assert empty_burger.ingredients == []

    def test_bun_assignment_works(self, empty_burger, fake_bun):
        empty_burger.set_buns(fake_bun)
        assert empty_burger.bun == fake_bun

    def test_adding_ingredient_changes_list(self, empty_burger, fake_ingredient):
        old = len(empty_burger.ingredients)
        empty_burger.add_ingredient(fake_ingredient)
        assert len(empty_burger.ingredients) == old + 1

    def test_removing_ingredient_shrinks_list(self, empty_burger, fake_ingredient):
        empty_burger.add_ingredient(fake_ingredient)
        empty_burger.remove_ingredient(0)
        assert empty_burger.ingredients == []

    def test_can_reorder_ingredients(self, empty_burger):
        from unittest.mock import Mock
        first = Mock()
        second = Mock()
        empty_burger.add_ingredient(first)
        empty_burger.add_ingredient(second)
        empty_burger.move_ingredient(0, 1)
        assert empty_burger.ingredients == [second, first]

    @pytest.mark.parametrize("bun_price", [100.0, 200.0])
    def test_price_counts_buns_twice(self, empty_burger, fake_bun, bun_price):
        fake_bun.get_price.return_value = bun_price
        empty_burger.set_buns(fake_bun)
        assert empty_burger.get_price() == bun_price * 2

    @pytest.mark.parametrize("bun_price, ingr_price", [(100.0, 50.0), (250.0, 125.0)])
    def test_price_with_ingredient(self, empty_burger, fake_bun, fake_ingredient, bun_price, ingr_price):
        fake_bun.get_price.return_value = bun_price
        fake_ingredient.get_price.return_value = ingr_price
        empty_burger.set_buns(fake_bun)
        empty_burger.add_ingredient(fake_ingredient)
        assert empty_burger.get_price() == bun_price * 2 + ingr_price

    def test_receipt_content_is_reasonable(self, empty_burger, fake_bun, fake_ingredient):
        fake_bun.get_name.return_value = "parmesan bun"
        fake_bun.get_price.return_value = 100.0
        fake_ingredient.get_type.return_value = "SAUCE"
        fake_ingredient.get_name.return_value = "spicy ketchup"
        fake_ingredient.get_price.return_value = 35.0

        empty_burger.set_buns(fake_bun)
        empty_burger.add_ingredient(fake_ingredient)

        expected_receipt = (
            "(==== parmesan bun ====)\n"
            "= sauce spicy ketchup =\n"
            "(==== parmesan bun ====)\n"
            "\n"
            "Price: 235.0"
)
        receipt = empty_burger.get_receipt()
        # Вывести строку для отладки:
        print("receipt:", repr(receipt))
        print("expected:", repr(expected_receipt))
        assert receipt.strip() == expected_receipt.strip()
