import pytest


class TestBurger:
    def test_set_buns_new_bun_assigned(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_new_ingredient_added(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_ingredient_removed(self, burger, mock_ingredient):
        sauce = mock_ingredient()
        meet = mock_ingredient()
        burger.ingredients = [sauce, meet]
        burger.remove_ingredient(0)
        assert burger.ingredients == [meet]

    def test_move_ingredient_ingredient_moved(self, burger, mock_ingredient):
        sauce = mock_ingredient()
        meet = mock_ingredient()
        onion = mock_ingredient()
        burger.ingredients = [sauce, meet, onion]
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [meet, onion, sauce]

    @pytest.mark.parametrize("price_bun, price_ingredient, expected_total_price",
                             [
                                 (30, 15, 90),
                                 (120, 17, 274)
                             ])
    def test_get_price_success(self, burger, mock_bun, price_bun,
                               mock_ingredient, price_ingredient, expected_total_price):
        mock_bun.get_price.return_value = price_bun
        burger.bun = mock_bun
        sauce = mock_ingredient()
        sauce.get_price.return_value = price_ingredient
        meet = mock_ingredient()
        meet.get_price.return_value = price_ingredient
        burger.ingredients = [sauce, meet]
        assert burger.get_price() == expected_total_price

    def test_get_receipt_success(self, burger, mock_bun, mock_ingredient):
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        receipt = burger.get_receipt()
        assert f'(==== {mock_bun.get_name.return_value} ====)' in receipt
        assert f'= sauce {mock_ingredient.get_name.return_value} =' in receipt
        assert f'Price: {mock_bun.get_price.return_value * 2 + mock_ingredient.get_price.return_value}' in receipt
