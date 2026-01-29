import pytest
from Diplom_1.burger import Burger
from Diplom_1.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient


class TestBurger:

    def test_bun_get_name(self):
        bun = Bun("Булочка", 100)
        assert bun.get_name() == "Булочка"

    def test_bun_get_price(self):
        bun = Bun("Булочка", 100)
        assert bun.get_price() == 100

    def test_ingredient_get_type(self):
        ing = Ingredient("sauce", "Кетчуп", 50)
        assert ing.get_type() == "sauce"

    def test_ingredient_get_name(self):
        ing = Ingredient("sauce", "Кетчуп", 50)
        assert ing.get_name() == "Кетчуп"

    def test_ingredient_get_price(self):
        ing = Ingredient("sauce", "Кетчуп", 50)
        assert ing.get_price() == 50

    def test_set_buns_sets_bun_correctly(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    @pytest.mark.parametrize("ingredients_data", [
        [(INGREDIENT_TYPE_SAUCE, "Sauce A", 1.5), (INGREDIENT_TYPE_FILLING, "Meat", 3.0)],
        [(INGREDIENT_TYPE_FILLING, "Cheese", 2.0)],
    ])
    def test_add_ingredient_adds_to_list(self, ingredient_mock, ingredients_data):
        burger = Burger()
        for data in ingredients_data:
            burger.add_ingredient(ingredient_mock(*data))
        assert len(burger.ingredients) == len(ingredients_data)

    def test_remove_ingredient_removes_correct(self, ingredient_mock):
        burger = Burger()
        ing1 = ingredient_mock(INGREDIENT_TYPE_FILLING, "A", 1.0)
        ing2 = ingredient_mock(INGREDIENT_TYPE_FILLING, "B", 2.0)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ing2
        assert len(burger.ingredients) == 1

    def test_move_ingredient_moves(self, ingredient_mock):
        burger = Burger()
        ing1 = ingredient_mock(INGREDIENT_TYPE_FILLING, "A", 1.0)
        ing2 = ingredient_mock(INGREDIENT_TYPE_FILLING, "B", 2.0)
        ing3 = ingredient_mock(INGREDIENT_TYPE_FILLING, "C", 3.0)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(2, 0)

        assert burger.ingredients[0] == ing3
        assert burger.ingredients[1] == ing1
        assert burger.ingredients[2] == ing2

    def test_get_price_calculates_correctly(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        ing1 = ingredient_mock(INGREDIENT_TYPE_FILLING, "A", 1.0)
        ing2 = ingredient_mock(INGREDIENT_TYPE_SAUCE, "B", 2.0)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        expected_price = bun_mock.get_price() * 2 + ing1.get_price() + ing2.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun_mock, ingredient_mock_filling, ingredient_mock_sauce):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock_filling)
        burger.add_ingredient(ingredient_mock_sauce)

        receipt = burger.get_receipt()

        expected_lines = [
            f"(==== {bun_mock.get_name()} ====)",
            f"= {ingredient_mock_filling.get_type().lower()} {ingredient_mock_filling.get_name()} =",
            f"= {ingredient_mock_sauce.get_type().lower()} {ingredient_mock_sauce.get_name()} =",
            f"(==== {bun_mock.get_name()} ====)",
            "",
            f"Price: {burger.get_price()}"
        ]

        expected_receipt = "\n".join(expected_lines)

        assert receipt == expected_receipt

    def test_get_price_raises_if_bun_not_set(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_raises_if_bun_not_set(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()

