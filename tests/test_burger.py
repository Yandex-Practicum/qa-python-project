class TestBurger:
    def test_burger_initialization(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_burger_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient(self, burger, ingredient_filling):
        burger.add_ingredient(ingredient_filling)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling

    def test_burger_remove_ingredient(self, burger, ingredient_filling):
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self, burger, ingredient_filling, ingredient_sauce):
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_sauce, ingredient_filling]

    def test_burger_get_price(self,burger, bun, ingredient_filling, ingredient_sauce):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)
        assert burger.get_price() == 600

    def test_get_receipt(self,burger, bun, ingredient_filling, ingredient_sauce):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "= sauce chili sauce =\n"
            "(==== black bun ====)\n"
            "Price: 600"
        )
        assert receipt.replace("\n\n", "\n") == expected_receipt