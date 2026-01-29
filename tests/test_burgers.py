from helpers import BUN_NAME_1, BUN_PRICE, SAUCE_NAME, FILLING_NAME, SAUCE_PRICE, FILLING_PRICE


class TestBurger:
    def test_add_one_ingredient(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients[0].get_name() == SAUCE_NAME, "Ингредиент не был добавлен корректно"

    def test_add_two_ingredients(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.ingredients[0].get_name() == SAUCE_NAME and burger.ingredients[
            1].get_name() == FILLING_NAME, "Ингредиенты не были добавлены корректно"

    def test_remove_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(1)
        assert burger.ingredients[0].get_name() == SAUCE_NAME and len(
            burger.ingredients) == 1, "Ингредиент не был удален корректно"

    def test_move_ingredient(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == FILLING_NAME and burger.ingredients[
            1].get_name() == SAUCE_NAME, "Ингредиент не был перемещен корректно"

    def test_get_price(self, burger, mock_bun, mock_sauce, mock_filling):
        mock_bun.get_price.return_value = BUN_PRICE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE
        assert burger.get_price() == expected_price, f"Общая цена бургера {burger.get_price()} не соответствует ожидаемой {expected_price}"

    def test_get_receipt(self, burger, mock_bun, mock_sauce):
        mock_bun.get_name.return_value = BUN_NAME_1
        mock_bun.get_price.return_value = BUN_PRICE
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        expected_price = BUN_PRICE * 2 + SAUCE_PRICE
        receipt = burger.get_receipt()
        assert all([
            BUN_NAME_1 in receipt,
            SAUCE_NAME in receipt,
            f"Price: {expected_price}" in receipt
        ]), "Чек сформирован неверно"
