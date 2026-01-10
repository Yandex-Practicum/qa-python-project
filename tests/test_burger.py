import pytest
import allure
from Stellar_Burgers.bun import Bun
from Stellar_Burgers.ingredient import Ingredient
from Stellar_Burgers.burger import Burger

@allure.feature('Проверка класса Burger')
class TestBurger:
    @allure.title('Проверка установки булочки')
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    @allure.title('Проверка добавления ингредиента')
    @pytest.mark.parametrize("ingredient_name", ["beef", "ketchup", "cheese"])
    def test_add_ingredient(self, ingredient_name):
        burger = Burger()
        ingredient = Ingredient("FILLING", ingredient_name, 100)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[-1] == ingredient

    @allure.title('Проверка удаления ингредиента')
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "beef", 100)
        ingredient2 = Ingredient("SAUCE", "ketchup", 50)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient2]

    @allure.title('Проверка перемещения ингредиента')
    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("FILLING", "beef", 100)
        ingredient2 = Ingredient("SAUCE", "ketchup", 50)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient2

    @allure.title('Проверка расчёта стоимости бургера')
    def test_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient1 = Ingredient("FILLING", "beef", 100)
        ingredient2 = Ingredient("SAUCE", "ketchup", 50)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_price = bun.get_price() * 2 + ingredient1.get_price() + ingredient2.get_price()
        assert burger.get_price() == expected_price

    @allure.title('Проверка генерации чека бургера')
    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        ingredient1 = Ingredient("FILLING", "beef", 100)
        ingredient2 = Ingredient("SAUCE", "ketchup", 50)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {ingredient1.get_type().lower()} {ingredient1.get_name()} =\n"
            f"= {ingredient2.get_type().lower()} {ingredient2.get_name()} =\n"
            f"(==== {bun.get_name()} ====)\n"
            "\n"  
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt

