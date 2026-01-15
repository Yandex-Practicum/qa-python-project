def test_burger_get_receipt_returns_right_answer(burger, ingredient_mock, bun_mock):
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    receipt = burger.get_receipt()
    assert "Булка" in receipt
    assert "Котлета" in receipt
    assert str(burger.get_receipt()) in receipt
