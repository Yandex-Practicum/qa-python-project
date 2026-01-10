import pytest

class TestBurger:

    def test_set_buns(self, burger):
        assert burger.bun == burger.set_buns('black bun')

    @pytest.mark.parametrize('ing', ['hot sauce', 'cutlet'])
    def test_add_ingredient(self, burger, ing):
        burger.add_ingredient(ing)
        assert burger.ingredients == [ing]

    @pytest.mark.parametrize('ing_1, ing_2', [['hot sauce', 'cutlet'], ['chili sauce', 'sausage']])
    def test_remove_ingredient(self, burger, ing_1, ing_2):
        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing_2]

    @pytest.mark.parametrize('ing_1, ing_2', [['hot sauce', 'cutlet'], ['chili sauce', 'sausage']])
    def test_move_ingredient(self, burger, ing_1, ing_2):
        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ing_2

    def test_get_price(self, bun, ingredient, burger):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 210

    def test_get_receipt(self, bun, ingredient, burger):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = ('(==== black bun ====)\n'
                   '= sauce hot sauce =\n'
                   '(==== black bun ====)\n'
                   '\n'
                   'Price: 210')

        assert burger.get_receipt() == receipt