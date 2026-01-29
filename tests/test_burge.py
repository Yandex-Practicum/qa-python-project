import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun  # Импортируем класс Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:
    # Инициализация
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    # Добавление булочки
    def test_set_buns(self):
        burger = Burger()
        test_bun = Bun("white bun", 100)
        burger.set_buns(test_bun)
        assert burger.bun == test_bun

    # Добавление ингредиентов
    @pytest.mark.parametrize("ingredient_type,ingredient_name,ingredient_price", [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 50),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200)
    ])
    def test_add_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    # Удаление ингредиентов
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 30)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Перемещение ингредиентов
    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "mayo", 20)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cheese", 150)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    # Получение цены
    def test_get_price(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 150))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "mustard", 40))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "onion", 20))
        assert burger.get_price() == 150 * 2 + 40 + 20  # Булочка учитывается дважды

    # Получение рецепта
    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(Bun("red bun", 200))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 30))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "salad", 50))

        receipt = burger.get_receipt().split('\n')

        assert len(receipt) >= 5, "Рецепт должен содержать как минимум 5 строк"
        assert receipt[0] == "(==== red bun ====)", "Первая строка должна быть верхней булочкой"
        assert receipt[1] == "= sauce ketchup =", "Вторая строка должна содержать соус"
        assert receipt[2] == "= filling salad =", "Третья строка должна содержать начинку"
        assert receipt[3] == "(==== red bun ====)", "Четвертая строка должна быть нижней булочкой"
        assert "Price: 480" in receipt[-1], "Последняя строка должна содержать общую сумму"

    # Граничные случаи
    def test_remove_nonexistent_ingredient(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_nonexistent_ingredient(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)

    def test_empty_burger_price(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_empty_burger_receipt(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
