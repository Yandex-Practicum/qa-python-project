from praktikum.burger import Burger


class TestBurger:
    def test_burger_init_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None

    def test_burger_init_ingredients_is_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []

    def test_burger_set_buns_bun_is_set(self, create_bun_mock):
        burger = Burger()
        bun = create_bun_mock
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient_ingredient_is_added(self, create_bun_mock, create_ingredient_mock):
        burger = Burger()
        bun = create_bun_mock
        ingredient = create_ingredient_mock
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_burger_remove_ingredient_ingredient_is_removed(self, create_test_burger):
        burger = create_test_burger[0]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_burger_move_ingredient_ingredient_is_moved(self, create_test_burger):
        burger, bun, ingredient_1, ingredient_2 = create_test_burger
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_burger_get_price_price_is_correct(self, create_test_burger):
        burger = create_test_burger[0]
        price = (burger.bun.price * 2) + burger.ingredients[0].price + burger.ingredients[1].price
        assert burger.get_price() == price

    def test_burger_receipt_is_correct(self, create_test_burger):
        burger = create_test_burger[0]
        expected_receipt = (f'(==== {burger.bun.name} ====)\n'
                            f'= sauce {burger.ingredients[0].name} =\n'
                            f'= filling {burger.ingredients[1].name} =\n'
                            f'(==== {burger.bun.name} ====)\n\n'
                            f'Price: {burger.get_price()}')
        assert expected_receipt == burger.get_receipt()
