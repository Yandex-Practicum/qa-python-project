import data


class TestBurger:

    def test_set_bun(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_set_bun_1(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger_with_bun_and_ingredients):
        ingredient_for_move = burger_with_bun_and_ingredients.ingredients[0]
        burger_with_bun_and_ingredients.move_ingredient(0, 1)
        assert burger_with_bun_and_ingredients.ingredients.index(
            ingredient_for_move) == 1

    def test_get_price_burger(self, burger_with_bun_and_ingredients):
        price = burger_with_bun_and_ingredients.get_price()
        price_must_be = sum(n[2] for n in data.ingredients) + data.bun[1] * 2
        assert price == price_must_be

    def test_get_receipt(self, burger_with_bun_and_ingredients):
        receipt = burger_with_bun_and_ingredients.get_receipt()
        assert len(receipt) > 20
