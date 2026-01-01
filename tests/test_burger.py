import pytest


class TestBurger:

    def test_initial_state(self, burger):
        """Тестирование начального состояния нового бургера."""
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, mock_bun):
        """Проверяем установку булочки в бургер."""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    @pytest.mark.parametrize("ingredient_fixture", ["mock_sauce", "mock_filling"])
    def test_add_ingredient(self, burger, ingredient_fixture, request):
        """Тестирование метода добавления ингредиентов в бургер."""
        ingredient = request.getfixturevalue(ingredient_fixture)
        assert burger.ingredients == []
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger, mock_sauce, mock_filling):
        """Тестирование метода удаления ингредиента из бургера."""
        burger.ingredients = [mock_sauce, mock_filling]
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling
        
    def test_get_price(self, burger, mock_bun, mock_filling, mock_sauce):
        """Тестирование метода получения цены."""
        burger.bun = mock_bun
        burger.ingredients = [mock_filling, mock_sauce]
        expected_price = (
                mock_bun.get_price() * 2
                + mock_filling.get_price()
                + mock_sauce.get_price()
        )
        assert burger.get_price() == expected_price
        
    def test_get_receipt(self, burger, mock_bun, mock_filling, mock_sauce):
        """Тестирование метода получения чека."""
        burger.bun = mock_bun
        burger.ingredients = [mock_filling, mock_sauce]
        expected_price = (
                mock_bun.get_price() * 2
                + mock_filling.get_price()
                + mock_sauce.get_price()
        )
        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_filling.get_type().lower()} {mock_filling.get_name()} =\n"
            f"= {mock_sauce.get_type().lower()} {mock_sauce.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            f"\n"
            f"Price: {expected_price}"
        )
        assert burger.get_receipt() == expected_receipt
        
    def test_move_ingredient(self, burger, mock_sauce, mock_filling):
            """Тестирование метода перемещения ингредиентов в бургере."""
            burger.ingredients = [mock_sauce, mock_filling]
            burger.move_ingredient(0, 1)
            assert burger.ingredients == [mock_filling, mock_sauce]