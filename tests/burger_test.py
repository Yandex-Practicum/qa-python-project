import pytest
from data import test_data
from data.test_data import BURGER_INGREDIENT1


class TestBurger:
    def test_set_bun(self, burger):
        burger.set_buns(test_data.TEST_BUN)
        assert burger.bun == test_data.TEST_BUN


    @pytest.mark.parametrize("ingredients", [
        [],
        [test_data.BURGER_INGREDIENT1],
        [test_data.BURGER_INGREDIENT1, test_data.BURGER_INGREDIENT2]
    ])
    def test_add_ingredient(self, burger, ingredients):
        for i in ingredients:
            burger.add_ingredient(i)
        assert burger.ingredients == ingredients

    def test_remove_ingredient(self, burger):
        burger.add_ingredient(test_data.BURGER_INGREDIENT1)
        burger.add_ingredient(test_data.BURGER_INGREDIENT2)

        burger.remove_ingredient(1)
        assert burger.ingredients == [BURGER_INGREDIENT1]

    def test_move_ingredient(self, burger):
        burger.add_ingredient(test_data.BURGER_INGREDIENT1)
        burger.add_ingredient(test_data.BURGER_INGREDIENT2)

        burger.move_ingredient(1, 0)
        assert burger.ingredients == [test_data.BURGER_INGREDIENT2, test_data.BURGER_INGREDIENT1]

    def test_get_price(self, burger):
        burger.set_buns(test_data.TEST_BUN)
        burger.add_ingredient(test_data.BURGER_INGREDIENT1)
        burger.add_ingredient(test_data.BURGER_INGREDIENT2)

        assert burger.get_price() == burger.bun.get_price() * 2 + sum([i.get_price() for i in burger.ingredients])

    def test_get_receipt(self, burger):
        burger.set_buns(test_data.TEST_BUN)
        burger.add_ingredient(test_data.BURGER_INGREDIENT1)

        result = f"""(==== {burger.bun.get_name()} ====)
= {str(test_data.BURGER_INGREDIENT1.get_type()).lower()} {test_data.BURGER_INGREDIENT1.get_name()} =
(==== {burger.bun.get_name()} ====)

Price: {burger.get_price()}"""

        assert burger.get_receipt() == result
