from data import burger_price, burger_receipt


class TestBurger:
    def test_set_buns(self, bun, burger):
        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_one_ingridient(self, burger, ingredient):
        burger.ingredients = [ingredient]

        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_remove_one_from_two_ingredients(self, burger,
                                             ingredient, ingredient_2):
        burger.ingredients = [ingredient, ingredient_2]

        burger.remove_ingredient(0)

        assert ingredient_2 in burger.ingredients

    def test_move_ingredient(self, burger, ingredient, ingredient_2):
        burger.ingredients = [ingredient, ingredient_2]

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] is ingredient_2

    def test_get_price(self, burger_full):
        burger = burger_full

        assert burger.get_price() == burger_price

    def test_get_receipt(self, burger_full, bun, ingredient, ingredient_2):
        burger = burger_full

        assert burger_receipt == burger.get_receipt()
