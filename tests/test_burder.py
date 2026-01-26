import pytest
from unittest.mock import Mock
from Diplom_1.burger import Burger
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient


class TestBurger:
    @pytest.fixture
    def setup(self):
        burger = Burger()
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 1.0
        bun.get_name.return_value = "Test Bun"

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 0.5
        ingredient1.get_name.return_value = "Test Ingredient 1"
        ingredient1.get_type.return_value = "FILLING"

        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 0.75
        ingredient2.get_name.return_value = "Test Ingredient 2"
        ingredient2.get_type.return_value = "SAUCE"

        burger.set_buns(bun)

        return burger, bun, ingredient1, ingredient2

    def test_set_buns(self, setup):
        burger, bun, _, _ = setup
        assert burger.bun == bun

    def test_add_ingredient(self, setup):
        burger, _, ingredient1, _ = setup
        burger.add_ingredient(ingredient1)
        assert ingredient1 in burger.ingredients

    def test_remove_ingredient(self, setup):
        burger, _, ingredient1, ingredient2 = setup
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert ingredient1 not in burger.ingredients and ingredient2 in burger.ingredients


    def test_move_ingredient(self, setup):
        burger, _, ingredient1, ingredient2 = setup
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]

    def test_get_price(self, setup):
        burger, _, ingredient1, ingredient2 = setup
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 3.25

    def test_get_receipt(self, setup):
        burger, _, ingredient1, ingredient2 = setup
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt = (
            "(==== Test Bun ====)\n"
            "= filling Test Ingredient 1 =\n"
            "= sauce Test Ingredient 2 =\n"
            "(==== Test Bun ====)\n\n"
            "Price: 3.25"
        )
        assert burger.get_receipt() == expected_receipt