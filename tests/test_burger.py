from data import TestData


class TestBurger:

    def test_set_bun(self, burger, mock_bun):

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, ingredients_mock, ingredients_mock_add):
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock_add)
        assert burger.ingredients[0] == ingredients_mock
        assert len(burger.ingredients) == 2

    def test_remove_ingredient(self, burger, ingredients_mock):
        burger.add_ingredient(ingredients_mock)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self, burger, ingredients_mock, ingredients_mock_add):
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock_add)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0] == ingredients_mock_add
        assert burger.ingredients[1] == ingredients_mock

    def test_get_price_full_data(self, burger, mock_bun,ingredients_mock, ingredients_mock_add):
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock_add)
        expected_price = mock_bun.get_price() * 2 + ingredients_mock.price + ingredients_mock_add.price
        assert burger.get_price() == expected_price


    def test_get_price_with_no_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        expected_price = mock_bun.get_price() * 2
        assert burger.get_price() == expected_price


    def test_get_receipt_full_data(self, burger, mock_bun, ingredients_mock, ingredients_mock_add):
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredients_mock)
        burger.add_ingredient(ingredients_mock_add)
        assert burger.get_receipt() == TestData.EXPECTED_CHECK

    def test_get_receipt_no_ingredient(self,burger,mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_receipt() == TestData.EXPECTED_CHECK_NO_INGREDIENT

