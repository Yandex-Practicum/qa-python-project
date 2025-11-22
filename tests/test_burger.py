import pytest
from data import Data
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_burger_init_bun_check(self):
        burger = Burger()
        assert burger.bun is None

    def test_burger_init_ingredients_check(self):
        burger = Burger()
        assert burger.ingredients == []

    @pytest.mark.parametrize("bun_data", Data.DB_BUNS)
    def test_burger_set_buns_check(self, bun_data):
        burger = Burger()
        bun = Bun(name=bun_data[0], price=bun_data[1])
        burger.set_buns(bun)
        assert (burger.bun.name == bun_data[0]) and (burger.bun.price == bun_data[1])

    @pytest.mark.parametrize("ingredient_data", Data.DB_INGREDIENTS)
    def test_burger_add_ingredient_check(self, ingredient_data):
        burger = Burger()
        ingredient = Ingredient(ingredient_type=ingredient_data[0], name=ingredient_data[1], price=ingredient_data[2])
        burger.add_ingredient(ingredient)
        assert burger.ingredients[-1] == ingredient

    @pytest.mark.parametrize("index", list(range(len(Data.DB_INGREDIENTS))))
    def test_burger_remove_ingredient_check(self, index):
        burger = Burger()
        for data in Data.DB_INGREDIENTS:
            ingredient = Ingredient(ingredient_type=data[0], name=data[1], price=data[2])
            burger.ingredients.append(ingredient)
        removed = burger.ingredients[index]
        burger.remove_ingredient(index=index)
        assert removed not in burger.ingredients

    def test_burger_move_ingredient_check(self):
        burger = Burger()
        ingredient_1 = Ingredient(ingredient_type="SAUCE", name="hot sauce", price=100)
        ingredient_2 = Ingredient(ingredient_type="FILLING", name="dinosaur", price=200)
        ingredient_3 = Ingredient(ingredient_type="FILLING", name="sausage", price=300)
        burger.ingredients = [ingredient_1, ingredient_2, ingredient_3]
        burger.move_ingredient(index=1, new_index=2)
        assert burger.ingredients == [ingredient_1, ingredient_3, ingredient_2]

    def test_burger_get_price_check(self, mock_bun, mock_ingredients):
        burger_price = mock_bun.get_price() * 2
        for ingredient in mock_ingredients:
            burger_price += ingredient.get_price()

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = mock_ingredients
        assert burger.get_price() == burger_price

    def test_burger_get_receipt_check(self, mock_bun, mock_ingredients):
        burger_price = mock_bun.get_price() * 2
        burger_receipt = f"(==== {mock_bun.get_name()} ====)\n"
        for ingredient in mock_ingredients:
            burger_price += ingredient.get_price()
            burger_receipt += f"= {ingredient.get_type().lower()} {ingredient.get_name()} =\n"
        burger_receipt += f"(==== {mock_bun.get_name()} ====)\n\n"
        burger_receipt += f"Price: {burger_price}"

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = mock_ingredients
        assert burger.get_receipt() == burger_receipt
