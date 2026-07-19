import pytest
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from testdata.data_burger import BURGER_PRICE_DATA


class TestBurgerSetBuns:
    """Тесты установки булочек."""

    @pytest.mark.unit
    def test_set_buns_valid_bun_assigns_bun(self):
        """
        Given: бургер и булочка
        When: вызываем set_buns
        Then: булочка сохраняется в атрибуте bun
        """
        burger = Burger()
        bun = Bun("black bun", 100)

        burger.set_buns(bun)

        assert burger.bun is bun

    @pytest.mark.unit
    def test_set_buns_second_bun_replaces_first(self):
        """
        Given: бургер с установленной булочкой
        When: устанавливаем другую булочку
        Then: булочка заменяется
        """
        burger = Burger()
        bun1 = Bun("black bun", 100)
        bun2 = Bun("white bun", 200)

        burger.set_buns(bun1)
        burger.set_buns(bun2)

        assert burger.bun is bun2


class TestBurgerAddIngredient:
    """Тесты добавления ингредиентов."""

    @pytest.mark.unit
    def test_add_ingredient_valid_ingredient_appends_to_list(self):
        """
        Given: пустой бургер
        When: добавляем ингредиент
        Then: ингредиент появляется в списке
        """
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ingredient

    @pytest.mark.unit
    def test_add_ingredient_multiple_ingredients_appends_all(self):
        """
        Given: бургер
        When: добавляем несколько ингредиентов
        Then: все ингредиенты в списке в правильном порядке
        """
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] is ing1
        assert burger.ingredients[1] is ing2


class TestBurgerRemoveIngredient:
    """Тесты удаления ингредиентов."""

    @pytest.mark.unit
    def test_remove_ingredient_valid_index_removes_ingredient(self):
        """
        Given: бургер с двумя ингредиентами
        When: удаляем первый ингредиент
        Then: остаётся только второй
        """
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ing2


class TestBurgerMoveIngredient:
    """Тесты перемещения ингредиентов."""

    @pytest.mark.unit
    def test_move_ingredient_valid_indices_changes_position(self):
        """
        Given: бургер с тремя ингредиентами
        When: перемещаем третий ингредиент на первую позицию
        Then: порядок ингредиентов изменяется
        """
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)
        ing2 = Ingredient(INGREDIENT_TYPE_SAUCE, "mustard", 30)
        ing3 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(2, 0)

        assert burger.ingredients[0] is ing3
        assert burger.ingredients[1] is ing1
        assert burger.ingredients[2] is ing2


class TestBurgerGetPrice:
    """Тесты подсчёта цены."""

    @pytest.mark.unit
    @pytest.mark.parametrize("bun_price, ingredient_prices, expected", BURGER_PRICE_DATA)
    def test_get_price_with_ingredients_returns_sum(self, bun_price, ingredient_prices, expected):
        """
        Given: бургер с булочкой и ингредиентами
        When: вызываем get_price
        Then: цена = 2 * bun_price + sum(ingredient_prices)
        """
        burger = Burger()
        burger.set_buns(Bun("test bun", bun_price))
        for i, price in enumerate(ingredient_prices):
            burger.add_ingredient(Ingredient("sauce", f"ing{i}", price))

        result = burger.get_price()

        assert result == expected

    @pytest.mark.unit
    def test_get_price_no_ingredients_returns_double_bun_price(self):
        """
        Given: бургер без ингредиентов
        When: вызываем get_price
        Then: цена = 2 * bun_price
        """
        burger = Burger()
        burger.set_buns(Bun("test bun", 150))

        assert burger.get_price() == 300


class TestBurgerGetReceipt:
    """Тесты формирования чека."""

    @pytest.mark.unit
    def test_get_receipt_with_bun_contains_bun_name(self):
        """
        Given: бургер с булочкой
        When: вызываем get_receipt
        Then: чек содержит имя булочки
        """
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))

        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt

    @pytest.mark.unit
    def test_get_receipt_with_ingredient_contains_ingredient(self):
        """
        Given: бургер с ингредиентом
        When: вызываем get_receipt
        Then: чек содержит тип и имя ингредиента
        """
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50))

        receipt = burger.get_receipt()

        assert "= sauce ketchup =" in receipt

    @pytest.mark.unit
    def test_get_receipt_with_ingredient_contains_price(self):
        """
        Given: бургер с булочкой и ингредиентом
        When: вызываем get_receipt
        Then: чек содержит строку Price
        """
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50))

        receipt = burger.get_receipt()

        assert "Price: 250" in receipt

    @pytest.mark.unit
    def test_get_receipt_no_ingredients_returns_buns_and_price(self):
        """
        Given: бургер без ингредиентов
        When: вызываем get_receipt
        Then: чек содержит только булочки и цену
        """
        burger = Burger()
        burger.set_buns(Bun("white bun", 200))

        receipt = burger.get_receipt()

        assert receipt.count("(==== white bun ====)") == 2
        assert "Price: 400" in receipt

    @pytest.mark.unit
    def test_get_receipt_sauce_type_contains_lowercase(self):
        """
        Given: бургер с ингредиентом типа SAUCE
        When: вызываем get_receipt
        Then: тип ингредиента в чеке в нижнем регистре
        """
        burger = Burger()
        burger.set_buns(Bun("black bun", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50))

        receipt = burger.get_receipt()

        assert "= sauce ketchup =" in receipt
        assert "= SAUCE ketchup =" not in receipt
