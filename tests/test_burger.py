
class TestBurger:

    def test_set_buns_adds_buns_to_burger(self, burger, mock_create_buns):
        burger.set_buns(mock_create_buns)

        assert mock_create_buns.get_name() == burger.bun.get_name()

    def test_add_ingredient_adds_ingredients_to_burger(self, burger, mock_create_ingredient):
        burger.add_ingredient(mock_create_ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_create_ingredient


    def test_remove_ingredient_deletes_ingredient_from_burger(self, burger, mock_create_ingredient):
        burger.add_ingredient(mock_create_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0
        assert mock_create_ingredient not in burger.ingredients

    def test_move_ingredient_replaces_ingredients(self, burger, mock_create_ingredient, mock_create_additional_ingredient):
        burger.add_ingredient(mock_create_ingredient)
        burger.add_ingredient(mock_create_additional_ingredient)

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0].get_name() == mock_create_additional_ingredient.get_name()
        assert burger.ingredients[1].get_name() == mock_create_ingredient.get_name()


    def  test_get_price_returns_burger_price(self, burger, mock_create_buns, mock_create_ingredient):
        burger.set_buns(mock_create_buns)
        burger.add_ingredient(mock_create_ingredient)

        expected_price = mock_create_buns.get_price.return_value * 2 + \
                         mock_create_ingredient.get_price.return_value

        actual_price = burger.get_price()

        assert actual_price == expected_price


    def test_get_receipt_returns_receipt_of_order(self, burger, mock_create_buns, mock_create_ingredient, mock_create_additional_ingredient):
        burger.set_buns(mock_create_buns)
        burger.add_ingredient(mock_create_ingredient)
        burger.add_ingredient(mock_create_additional_ingredient)

        expected_receipt_lines = [
            f'(==== {mock_create_buns.get_name()} ====)',
            f'= {mock_create_ingredient.get_type().lower()} {mock_create_ingredient.get_name()} =',
            f'= {mock_create_additional_ingredient.get_type().lower()} {mock_create_additional_ingredient.get_name()} =',
            f'(==== {mock_create_buns.get_name()} ====)\n',
            f'Price: {burger.get_price()}'
        ]

        expected_receipt = '\n'.join(expected_receipt_lines)
        true_receipt = burger.get_receipt()

        assert true_receipt == expected_receipt


















