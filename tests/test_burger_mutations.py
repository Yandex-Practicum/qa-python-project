from praktikum.burger import Burger


class TestBurgerMutations:
    def test_add_ingredient_appends_to_list(self, mk_ing):
        burger = Burger()
        ingredient = mk_ing("A")

        burger.add_ingredient(ingredient)

        assert [item.get_name() for item in burger.ingredients] == ["A"]

    def test_remove_ingredient_by_index(self, mk_ing):
        burger = Burger()
        burger.add_ingredient(mk_ing("A"))
        burger.add_ingredient(mk_ing("C"))
        burger.add_ingredient(mk_ing("D"))

        burger.remove_ingredient(1)

        assert [item.get_name() for item in burger.ingredients] == ["A", "D"]

    def test_move_ingredient_changes_positions(self, mk_ing):
        burger = Burger()
        burger.add_ingredient(mk_ing("A"))
        burger.add_ingredient(mk_ing("C"))
        burger.add_ingredient(mk_ing("D"))

        burger.move_ingredient(0, 2)

        assert [item.get_name() for item in burger.ingredients] == ["C", "D", "A"]

    def test_set_buns_assigns_bun(self, mk_ing):
        burger = Burger()
        bun = mk_ing("Black Bun", price=100, type_="BUN")

        burger.set_buns(bun)

        assert burger.bun is bun
        assert burger.bun.get_type() == "BUN"
