BUN_PRICE = 50
BUN_NAME_1 = "Test Bun 1"
BUN_NAME_2 = "Test Bun 2"
SAUCE_NAME = "Test Sauce"
FILLING_NAME = "Test Filling"
SAUCE_PRICE = 20
FILLING_PRICE = 40

def test_add_one_ingredient(burger, mock_sauce):
    burger.add_ingredient(mock_sauce)
    assert burger.ingredients[0].get_name() == SAUCE_NAME, "Ингредиент не был добавлен корректно"

def test_add_two_ingredients(burger, mock_sauce, mock_filling):
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    assert burger.ingredients[0].get_name() == SAUCE_NAME and burger.ingredients[
        1].get_name() == FILLING_NAME, "Ингредиенты не были добавлены корректно"

def test_remove_ingredient(burger, mock_sauce, mock_filling):
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    burger.remove_ingredient(1)
    assert burger.ingredients[0].get_name() == SAUCE_NAME and len(
        burger.ingredients) == 1, "Ингредиент не был удален корректно"

def test_move_ingredient(burger, mock_sauce, mock_filling):
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0].get_name() == FILLING_NAME and burger.ingredients[
        1].get_name() == SAUCE_NAME, "Ингредиент не был перемещен корректно"

def test_get_price(burger, mock_bun, mock_sauce, mock_filling):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    expected_price = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE
    assert burger.get_price() == expected_price, f"Общая цена бургера {burger.get_price()} не соответствует ожидаемой {expected_price}"

def test_get_receipt(burger, mock_bun, mock_sauce, mock_filling):
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    expected_price = BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE
    expected = (
        f'(==== {BUN_NAME_1} ====)\n'
        f'= sauce {SAUCE_NAME} =\n'
        f'= filling {FILLING_NAME} =\n'
        f'(==== {BUN_NAME_1} ====)\n'
        f'\n'
        f'Price: {expected_price}'
    )
    assert burger.get_receipt() == expected, 'Полный вывод чека не совпадает с ожидаемым'
