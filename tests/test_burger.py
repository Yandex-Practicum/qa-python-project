import pytest
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_sauce

    def test_remove_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling

    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_filling
        assert burger.ingredients[1] == ingredient_sauce

    def test_get_price(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        expected_price = bun.get_price() * 2 + ingredient_sauce.get_price() + ingredient_filling.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        
        receipt = burger.get_receipt()
        
        assert bun.get_name() in receipt
        assert ingredient_sauce.get_name() in receipt
        assert ingredient_filling.get_name() in receipt
        assert str(burger.get_price()) in receipt