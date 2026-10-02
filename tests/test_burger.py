class TestBurger:

    # проверка установки булочек
    def test_set_buns_sets_bun(self, bun, burger):
        burger.set_buns(bun)

        assert burger.bun == bun

    # проверка добавления ингредиента
    def test_add_ingredient_adds_ingredient(self, burger, sauce_1):
        burger.add_ingredient(sauce_1)

        assert burger.ingredients == [sauce_1]

    # проверка удаления ингредиента
    def test_remove_ingredient_removes_ingredient(self, burger, sauce_2):
        burger.add_ingredient(sauce_2)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    # проверка перемещения ингредиента
    def test_move_ingredient_moves_ingredient(
            self, burger, sauce_3, filling_1, filling_3):

        burger.add_ingredient(sauce_3)
        burger.add_ingredient(filling_1)
        burger.add_ingredient(filling_3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [
            filling_1,
            filling_3,
            sauce_3
        ]

    # проверка расчёта стоимости бургера
    def test_get_price_returns_correct_price(self, bun, burger, sauce_1):
        burger.set_buns(bun)
        burger.add_ingredient(sauce_1)

        burger_price = bun.get_price() * 2 + sauce_1.get_price()

        assert burger.get_price() == burger_price

    # проверка формирования чека
    def test_get_receipt_returns_correct_receipt(self, bun, burger, sauce_2):
        burger.set_buns(bun)
        burger.add_ingredient(sauce_2)

        expected_receipt = (
            f'(==== {bun.get_name()} ====)\n'
            f'= {str(sauce_2.get_type()).lower()} {sauce_2.get_name()} =\n'
            f'(==== {bun.get_name()} ====)\n\n'
            f'Price: {burger.get_price()}'
        )

        assert burger.get_receipt() == expected_receipt
