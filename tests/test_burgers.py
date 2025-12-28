import pytest
from Diplom_1.burger import Burger
from helpers import get_ingredient_indexes

class TestBurger:
    def test_set_buns(self, mock_bun):
        burger_for_test = Burger()
        burger_for_test.set_buns(mock_bun)
        assert burger_for_test.bun == mock_bun

    @pytest.mark.parametrize(
        'ingredient_fixture', [
            'mock_sauce',
            'mock_filling'
        ]
    )
    def test_add_ingredient(self, ingredient_fixture, request):
        ingredient = request.getfixturevalue(ingredient_fixture)
        burger_for_test = Burger()
        burger_for_test.add_ingredient(ingredient)
        assert ingredient in burger_for_test.ingredients
    def test_remove_ingredient(self,mock_sauce):
        burger_for_test = Burger()
        burger_for_test.add_ingredient(mock_sauce)
        burger_for_test.remove_ingredient(0)
        assert len(burger_for_test.ingredients) == 0
    def test_move_ingredient(self, mock_sauce, mock_filling):
       burger_for_test = Burger()
       burger_for_test.add_ingredient(mock_sauce)
       burger_for_test.add_ingredient(mock_filling)
       burger_for_test.move_ingredient(0,1)
       indexes = get_ingredient_indexes(burger_for_test)
       assert burger_for_test.ingredients[0] == mock_filling
       assert burger_for_test.ingredients[1] == mock_sauce

    def test_get_price(self, create_sauce, create_filling, create_bun):
        burger_for_test = Burger()
        burger_for_test.add_ingredient(create_sauce)
        burger_for_test.add_ingredient(create_filling)
        bun_for_test = create_bun
        burger_for_test.set_buns(bun_for_test)
        price = burger_for_test.get_price()
        assert price == 2772
    def test_get_receipt(self, create_sauce, create_filling, create_bun, capsys):
        burger_for_test = Burger()
        burger_for_test.add_ingredient(create_sauce)
        burger_for_test.add_ingredient(create_filling)
        bun_for_test = create_bun
        burger_for_test.set_buns(bun_for_test)
        receipt = burger_for_test.get_receipt()
        expected_receipt = (
            "(==== Краторная булка N-200i ====)\n"
            "= sauce Соус Spicy-X =\n"
            "= filling Мясо бессмертных моллюсков Protostomia =\n"
            "(==== Краторная булка N-200i ====)\n"
            f"Price: {burger_for_test.get_price()}"
        )
        assert receipt == expected_receipt