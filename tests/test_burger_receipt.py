from praktikum.burger import Burger


class TestBurgerReceipt:
    def test_receipt_text_full_match(self, mk_ing):
        burger = Burger()
        bun = mk_ing("Black Bun", price=100, type_="BUN")
        sauce = mk_ing("spicy", price=30, type_="SAUCE")
        filling = mk_ing("beef", price=70, type_="FILLING")

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected = (
            f"(==== {bun.get_name()} ====)\n"
            f"= sauce {sauce.get_name()} =\n"
            f"= filling {filling.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n"
            f"\nPrice: {2 * bun.get_price() + sauce.get_price() + filling.get_price()}\n"
        )

        assert burger.get_receipt() == expected
