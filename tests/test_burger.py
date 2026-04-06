import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    @allure.title("Проверка установки булочки")
    def test_set_buns(self):
        burger = Burger()
        bun = Bun("test bun", 100.0)
        burger.set_buns(bun)

        assert burger.bun == bun

    @allure.title("Проверка добавления и удаления ингредиентов")
    def test_add_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 50.0)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    @allure.title("Проверка перемещения ингредиента")
    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce1", 50.0)
        ingredient2 = Ingredient(INGREDIENT_TYPE_SAUCE, "sauce2", 60.0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient2, ingredient1]

    @allure.title("Проверка расчёта цены бургера с использованием моков")
    def test_get_price_with_mocks(self):
        burger = Burger()

        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 150.0

        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 75.0

        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 125.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = (
        mock_bun.get_price() * 2 +  # 2 булочки + 2 ингредиента
        mock_ingredient1.get_price() +
        mock_ingredient2.get_price()
    )                        
        
        assert burger.get_price() == expected_price

    @allure.title("Проверка формирования чека с параметризацией")
    @pytest.mark.parametrize("bun_name,bun_price,ingredient_type,ingredient_name,ingredient_price,expected_price", [
        ("black bun", 100.0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0, 300.0),
        ("white bun", 200.0, INGREDIENT_TYPE_FILLING, "cutlet", 150.0, 550.0),
        ("red bun", 300.0, INGREDIENT_TYPE_SAUCE, "sour cream", 200.0, 800.0)
    ])
    def test_get_receipt_parametrized(self, bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price, expected_price):
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"= {ingredient_type.lower()} {ingredient_name} =\n"
            f"(==== {bun_name} ====)\n\n"               #
            f"Price: {expected_price}"
    )
        #print("Фактический чек:")
        #print(receipt)
        #print("Ожидаемый чек:")
        #print(expected_receipt)

        assert receipt == expected_receipt