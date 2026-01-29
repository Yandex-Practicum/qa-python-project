class TestBurger:
    def test_burger_initialization(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger, mock_ingredient, mock_ingredient_next):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_next)

        burger.remove_ingredient(0)

        assert mock_ingredient not in burger.ingredients
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_next


    def test_move_ingredient(self, burger, mock_ingredient, mock_ingredient_next):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_next)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient_next, mock_ingredient]


    def test_get_price(self, burger, mock_bun, mock_ingredient, mock_ingredient_next):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_next)

        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price() + mock_ingredient_next.get_price()
        assert burger.get_price() == expected_price


    def test_get_receipt(self, burger, mock_bun, mock_ingredient, mock_ingredient_next):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_next)

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =\n"
            f"= {mock_ingredient_next.get_type().lower()} {mock_ingredient_next.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n\n"
            f"Price: {burger.get_price():.2f}"
        )

        assert burger.get_receipt() == expected_receipt




