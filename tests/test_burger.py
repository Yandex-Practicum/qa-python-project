from praktikum.burger import Burger


class TestBurger:

    def test_set_correct_bun_when_burger_is_created(self, get_fake_bun):
        burger = Burger()
        fake_bun, *_ = get_fake_bun()

        burger.set_buns(fake_bun)
        assert burger.bun.get_name() == fake_bun.get_name()

    def test_add_ingredient_to_burger(self, get_fake_ingredient):
        burger = Burger()
        ingredient, *_ = get_fake_ingredient()

        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_add_multiple_ingredients_to_burger(self, get_fake_ingredient):
        burger = Burger()
        ingredient, *_ = get_fake_ingredient()
        n = 5

        for _ in range(n):
            burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == n

    def test_remove_ingredient_from_burger(self, get_fake_ingredient):
        burger = Burger()
        ingredient, *_ = get_fake_ingredient()

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_swap_ingredient_in_burger(self, get_fake_ingredient):
        burger = Burger()
        n = 3

        first, second, third = get_fake_ingredient(n)

        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        burger.move_ingredient(1, 2)

        assert burger.ingredients == [first, third, second]

    def test_return_correct_price_when_burger_is_created(self, get_fake_bun, get_fake_ingredient):
        burger = Burger()
        n = 3
        price = 5
        fake_bun, *_ = get_fake_bun()

        burger.set_buns(fake_bun)
        first, second, third = get_fake_ingredient(n)

        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        assert burger.get_price() == price

    def test_return_correct_receipt_when_burger_is_created(self, get_fake_bun, get_fake_ingredient):
        burger = Burger()
        n = 3
        fake_bun, *_ = get_fake_bun()

        burger.set_buns(fake_bun)
        first, second, third = get_fake_ingredient(n)

        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        assert burger.get_receipt() == (
            f"(==== {fake_bun.get_name()} ====)\n"
            f"= {first.get_type()} {first.get_name()} =\n"
            f"= {second.get_type()} {second.get_name()} =\n"
            f"= {third.get_type()} {third.get_name()} =\n"
            f"(==== {fake_bun.get_name()} ====)\n\n"
            "Price: 5"
        )
