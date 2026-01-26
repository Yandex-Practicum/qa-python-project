from unittest.mock import Mock


class TestBurger:
    def test_set_buns_success(self, buns, burgers):
        burgers.set_buns(buns)
        assert burgers.bun == buns

    def test_add_ingredient_success(self, ingredient1, burgers):
        burgers.add_ingredient(ingredient1)
        assert burgers.ingredients == [ingredient1]

    def test_remove_ingredient_success(self, ingredient1, burgers):
        burgers.add_ingredient(ingredient1)
        burgers.remove_ingredient(0)
        assert len(burgers.ingredients) == 0

    def test_move_ingredient_success(self, ingredient1, ingredient2, ingredient3, burgers):
        burgers.add_ingredient(ingredient1)
        burgers.add_ingredient(ingredient2)
        burgers.add_ingredient(ingredient3)
        burgers.move_ingredient(1, 2)

        assert burgers.ingredients[0].name == 'chili sauce'
        assert burgers.ingredients[1].name == 'sour cream'
        assert burgers.ingredients[2].name == 'cutlet'

    def test_get_price_success(self, ingredient1, ingredient2, buns, burgers):
        burgers.set_buns(buns)
        burgers.add_ingredient(ingredient1)
        burgers.add_ingredient(ingredient2)
        total_price = burgers.get_price()

        assert total_price == 600

    def test_get_price_with_mock_bun(self, ingredient1, ingredient2, buns, burgers):
        buns.get_price = Mock(return_value=50)

        burgers.set_buns(buns)
        burgers.add_ingredient(ingredient1)
        burgers.add_ingredient(ingredient2)

        total_price = burgers.get_price()

        assert total_price == 50 * 2 + ingredient1.get_price() + ingredient2.get_price()

    def test_get_receipt_success(self, ingredient1, ingredient2, buns, burgers):
        burgers.set_buns(buns)
        burgers.add_ingredient(ingredient1)
        burgers.add_ingredient(ingredient2)
        receipt = burgers.get_receipt()

        expected_receipt = (
            f'(==== {buns.get_name()} ====)\n'
            f'= {ingredient1.get_type().lower()} {ingredient1.get_name()} =\n'
            f'= {ingredient2.get_type().lower()} {ingredient2.get_name()} =\n'
            f'(==== {buns.get_name()} ====)\n'
            f'\n'
            f'Price: {burgers.get_price()}'
        )

        assert expected_receipt == receipt






