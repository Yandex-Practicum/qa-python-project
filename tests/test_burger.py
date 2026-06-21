class TestBurger:

    # Проверка что бургер создается пустым
    def test_burger_creation(self, empty_burger):
        assert empty_burger.bun is None and empty_burger.ingredients == []

    #Проверка что булочка для бургера устанавливается корректно
    def test_set_buns_success(self, empty_burger, mock_bun):
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun and empty_burger.bun.get_name() == "fluorescent bun"

    #Проверка что ингридиент для бургера добавлется корректно
    def test_add_ingredient_success(self,empty_burger, mock_ingredient_filling):
        empty_burger.add_ingredient(mock_ingredient_filling)
        assert len(empty_burger.ingredients) == 1 and empty_burger.ingredients[0] == mock_ingredient_filling

    # Проверка что заданный ингридиент для бургера удаляется корректно
    def test_remove_ingredient_success(self, burger_with_one_ingredient):
        burger_with_one_ingredient.remove_ingredient(0)
        assert len(burger_with_one_ingredient.ingredients) == 0

    # Проверка что перемещение ингридиентов по списку работает корректно
    def test_move_ingredient_success(self,burger_full):
        burger_full.move_ingredient(1, 0)
        assert burger_full.ingredients[0].get_name() == "Beef meteorite"
        assert burger_full.ingredients[1].get_name() == "Sauce Spicy-X"


    # Проверка что цена бургера рассчитывается корректно
    def test_get_price_full_burger_success(self, burger_full):
        manual_price = burger_full.bun.price * 2
        manual_price += sum(ingredient.price for ingredient in burger_full.ingredients)
        price = burger_full.get_price()
        assert price == manual_price

    def test_get_receipt_full_burger(self, burger_full):
        expected_receipt = (
            "(==== fluorescent bun ====)\n"
            "= sauce Sauce Spicy-X =\n"
            "= filling Beef meteorite =\n"
            "(==== fluorescent bun ====)\n"
            "\n"
            "Price: 5066"
        )
        assert burger_full.get_receipt() == expected_receipt