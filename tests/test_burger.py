from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger"""

    # Тесты инициализации
    def test_burger_initialization(self):
        """Тест: бургер инициализируется с пустыми булочкой и ингредиентами"""
        empty_burger = Burger()
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    # Тесты установки булочки
    def test_set_buns(self, empty_burger, mock_bun):
        """Тест: установка булочки в бургер"""
        empty_burger.set_buns(mock_bun)

        assert empty_burger.bun == mock_bun

    # Тесты добавления ингредиентов
    def test_add_ingredient_to_empty_burger(self, empty_burger, mock_ingredient_sauce):
        """Тест: добавление первого ингредиента в пустой бургер"""
        empty_burger.add_ingredient(mock_ingredient_sauce)

        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == mock_ingredient_sauce

    def test_add_multiple_ingredients(self, burger_with_bun, mock_ingredient_sauce, mock_ingredient_filling):
        """Тест: добавление нескольких ингредиентов"""
        burger_with_bun.add_ingredient(mock_ingredient_sauce)
        burger_with_bun.add_ingredient(mock_ingredient_filling)

        assert len(burger_with_bun.ingredients) == 2
        assert burger_with_bun.ingredients[0] == mock_ingredient_sauce
        assert burger_with_bun.ingredients[1] == mock_ingredient_filling

    # Тесты удаления ингредиентов
    def test_remove_ingredient(self, burger_with_ingredients):
        """Тест: удаление ингредиента по индексу"""
        initial_count = len(burger_with_ingredients.ingredients)
        first_ingredient = burger_with_ingredients.ingredients[0]

        burger_with_ingredients.remove_ingredient(0)

        assert len(burger_with_ingredients.ingredients) == initial_count - 1
        assert first_ingredient not in burger_with_ingredients.ingredients

    # Тесты перемещения ингредиентов
    def test_move_ingredient(self, burger_with_ingredients):
        """Тест: перемещение ингредиента на новую позицию"""
        first_ingredient_before = burger_with_ingredients.ingredients[0]
        second_ingredient_before = burger_with_ingredients.ingredients[1]

        burger_with_ingredients.move_ingredient(0, 1)

        assert burger_with_ingredients.ingredients[0] == second_ingredient_before
        assert burger_with_ingredients.ingredients[1] == first_ingredient_before

    # Тесты расчета цены
    def test_get_price_with_ingredients(self, burger_with_ingredients, mock_bun, mock_ingredient_sauce,
                                        mock_ingredient_filling):
        """Тест: цена бургера с булочкой и ингредиентами"""
        expected_price = (mock_bun.get_price() * 2 +
                          mock_ingredient_sauce.get_price() +
                          mock_ingredient_filling.get_price())

        assert burger_with_ingredients.get_price() == expected_price

    # Тесты генерации чека
    def test_get_receipt_with_ingredients(self, burger_with_ingredients, mock_bun, mock_ingredient_sauce,
                                          mock_ingredient_filling):
        """Тест: чек бургера с ингредиентами"""
        receipt = burger_with_ingredients.get_receipt()

        expected_price = mock_bun.get_price() * 2 + mock_ingredient_sauce.get_price() + mock_ingredient_filling.get_price()
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =\n"
            f"= {mock_ingredient_filling.get_type().lower()} {mock_ingredient_filling.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            f"\n"
            f"Price: {expected_price}"
        )

        assert receipt == expected_receipt