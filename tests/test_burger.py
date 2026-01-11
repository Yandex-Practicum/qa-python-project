from data import Data


class TestBurger:
    def test_init_burger_bun_none(self, burger):
        assert burger.bun is None

    def test_init_burger_ingredients_empty(self, burger):
        assert burger.ingredients == []

    def test_set_buns_added_bun_in_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun.name == Data.bun_name

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price(self, burger, bun, ingredient, ingredient_1):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient_1)
        result = burger.get_price()
        assert result == 3010

    def test_get_receipt(self, burger, bun, ingredient, ingredient_1):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient_1)
        result = burger.get_receipt()
        receipt = [
            '(==== Краторная булка N-200i ====)',
            '= sauce dinosaur =',
            '= filling sausage =',
            '(==== Краторная булка N-200i ====)\n',
            'Price: 3010'
        ]
        assert '\n'.join(receipt) == result

    def test_move_ingredient_success_move(self, burger, bun, ingredient, ingredient_1):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient_1)

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient_1 and burger.ingredients[1] == ingredient
