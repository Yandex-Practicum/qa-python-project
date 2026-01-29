class TestBurger:

    """Тестируем создание бургера"""
    def test_create_burger(self, burger, bun):
        assert burger.bun is None
        assert burger.ingredients == []

    """Тестируем метод set_bun"""
    def test_set_buns_positive(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    """Тестируем добавление ингредиентов"""
    def test_add_ingredient_positive(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients == [mock_sauce]

    """Тестируем удаление ингредиентов"""
    def test_remove_ingredient_positive(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        index = burger.ingredients.index(mock_filling)
        burger.remove_ingredient(index)
        assert burger.ingredients == [mock_sauce]

    """Тестируем перемещение ингредиентов"""
    def test_move_ingredient_positive(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [mock_filling, mock_sauce]

    """Тестируем получение цены бургера"""
    def test_get_price_positive(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == 600

    """Тестируем получение чека"""
    def test_get_receipt_positive(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        price = burger.get_price()
        receipt = f"(==== black bun ====)\n= sauce sour cream =\n= filling dinosaur =\n(==== black bun ====)\n\nPrice: {price}"
        assert burger.get_receipt() == receipt
