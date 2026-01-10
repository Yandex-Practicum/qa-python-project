class TestBurger:


    def test_initial_state(self, burger):
        assert isinstance(burger.ingredients, list) and len(burger.ingredients) == 0

    def test_set_buns(self, burger, fake_bun):
        burger.set_buns(fake_bun)
        assert burger.bun == fake_bun,  f"Ошибка: ожидали {fake_bun}, получили {burger.bun}"

    def test_add_ingredient(self, burger, fake_ingredient):
        ingredient_sum = len(burger.ingredients)
        burger.add_ingredient(fake_ingredient)
        assert len(burger.ingredients) == ingredient_sum + 1,  \
        f"Ошибка: количество ингредиентов должно увеличиться на 1. Было {ingredient_sum}, стало {len(burger.ingredients)}"

    def test_remove_ingredient(self, burger, fake_ingredient):
        burger.add_ingredient(fake_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0,  \
        f"Ошибка: после удаления ингредиентов список должен быть пустым, сейчас {len(burger.ingredients)} "

    def test_move_ingredient(self, burger, fake_ingredient, fake_sauce):
        first_ingredient = fake_ingredient
        second_ingredient = fake_sauce
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        initial_count = len(burger.ingredients)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, first_ingredient] and len(burger.ingredients) == initial_count, \
        f"Ошибка: порядок ингредиентов неправильный или изменилось количество. Сейчас: {burger.ingredients}"

    def test_get_price_with_ingredients(self, burger, fake_bun, fake_ingredient, fake_sauce):
        burger.set_buns(fake_bun)
        burger.add_ingredient(fake_ingredient)
        burger.add_ingredient(fake_sauce)
        expected_price = (28 * 2) + 12 + 5
        actual_price = burger.get_price()
        assert actual_price == expected_price, \
        f"Ошибка: ожидали цену {expected_price}, получили {actual_price}"

    def test_get_receipt(self, burger, fake_bun, fake_ingredient, fake_sauce):
        burger.set_buns(fake_bun)
        burger.add_ingredient(fake_ingredient)
        burger.add_ingredient(fake_sauce)
        receipt = (
        "(==== Булочка с мОком ахахах ====)\n"
        "= filling Фейковая начинка =\n"
        "= sauce Соус со вкусом фейкоа =\n"
        "(==== Булочка с мОком ахахах ====)\n\n"
        "Price: 73"
    )
        assert burger.get_receipt() == receipt



