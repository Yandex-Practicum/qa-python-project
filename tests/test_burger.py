import pytest

class TestBurger:

    # изначальное состояние (без ингредиентов)
    def test_burger_initialization(self, new_burger):
        assert new_burger.bun is None
        assert new_burger.ingredients == []

    # проверяем добав. одной булки
    def test_set_buns_single_bun_added_in_burger(self, new_burger, bun_in_burger):
        new_burger.set_buns(bun_in_burger)
        assert new_burger.bun == bun_in_burger

    # Проверка добавления 2-ух ингрдтв. в бугрере
    def test_add_ingredient_two_ingridients_added_in_burger(self, new_burger, ingredients_in_burger):
        new_burger.add_ingredient(ingredients_in_burger[0])
        new_burger.add_ingredient(ingredients_in_burger[1])
        assert ingredients_in_burger[0] and ingredients_in_burger[1] in new_burger.ingredients

    # удаляем первый ингредиент 
    def test_remove_ingredient_first_ingredient_delete_from_burger(self, new_burger, ingredients_in_burger):
        new_burger.ingredients = ingredients_in_burger.copy()
        new_burger.remove_ingredient(0)
        expected_ingredients = ingredients_in_burger[1:]
        assert new_burger.ingredients == expected_ingredients

    # ингредиенты внутри списка
    def test_move_ingredient_moves_two_ingredient_in_burger_changed(self, new_burger, ingredients_in_burger):
        new_burger.ingredients = ingredients_in_burger.copy()
        new_burger.move_ingredient(0, 1)
        assert new_burger.ingredients[0] == ingredients_in_burger[1] and new_burger.ingredients[1] == ingredients_in_burger[0]

    # расчет цены
    @pytest.mark.parametrize("ingredients", [[0, 1], [1, 2], [0, 2], [0, 1, 2]])
    def test_get_price_various_ingredients_correct_price(self, mocked_burger, bun_in_burger, ingredients_in_burger, ingredients):
        selected_ingredients = [ingredients_in_burger[i] for i in ingredients]
        mocked_burger.ingredients = selected_ingredients
        expected_price = bun_in_burger.get_price.return_value * 2 + sum(i.get_price.return_value for i in selected_ingredients)
        price = mocked_burger.get_price()
        assert price == expected_price

    # чек
    @pytest.mark.parametrize("ingredients", [[0, 1], [1, 2], [0, 2], [0, 1, 2]])
    def test_get_receipt_various_ingredients_expected_price(self, mocked_burger, bun_in_burger, ingredients_in_burger, ingredients):
        selected_ingredients = [ingredients_in_burger[i] for i in ingredients]
        mocked_burger.ingredients = selected_ingredients
        receipt = mocked_burger.get_receipt()
        expected_lines = [f'(==== {bun_in_burger.get_name.return_value} ====)']
        expected_lines += [f'= {ing.get_type.return_value.lower()} {ing.get_name.return_value} =' for ing in selected_ingredients]
        expected_lines.append(f'(==== {bun_in_burger.get_name.return_value} ====)\n')
        expected_lines.append(f'Price: {mocked_burger.get_price()}')
        expected_receipt = '\n'.join(expected_lines)
        assert receipt == expected_receipt