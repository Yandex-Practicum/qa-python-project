import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient


class TestBurger:

    def test_burger_initial_state(self):
         "Проверка начального состояния бургера"
         burger = Burger()
         assert burger.bun is None
         assert burger.ingredients == []
         assert len(burger.ingredients) == 0

    def test_set_buns(self):
        "Проверка установки булочки"
        burger = Burger()
        bun = Bun("Sesame Bun", 50)
        burger.set_buns(bun)
        assert burger.bun is bun
        assert burger.bun.get_name() == "Sesame Bun"
        assert burger.bun.get_price() == 50

    def test_set_buns_with_mock(self):
        "Проверка установки булочки с моком"
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Mock Bun"
        mock_bun.get_price.return_value = 175
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    @pytest.mark.parametrize("bun_name,bun_price", [
        ("Sesame Bun", 50),
        ("Black Bun", 100),
        ("Red Bun", 300),
        ("White Bun", 200),
    ])
    def test_set_installing_different_buns(self, bun_name, bun_price):
        "Установка различных булочек"
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    def test_set_buns_replace(self):
        "Проверка замены булочки"
        burger = Burger()
        bun1 = Bun("White Bun", 200)
        bun2 = Bun("Black Bun", 100)
        burger.set_buns(bun1)
        assert burger.bun.get_name() == "White Bun"
        burger.set_buns(bun2)
        assert burger.bun.get_name() == "Black Bun"
        assert burger.bun.get_price() == 100

    def test_add_ingredient(self):
        "Проверка добавления ингредиента"
        burger = Burger()
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        ingredient = Ingredient("FILLING", "dinosaur", 200)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ingredient
        assert burger.ingredients[0].get_name() == "dinosaur"

    def test_add_ingredient_with_mock(self):
        "Проверка добавления ингредиента с моком"
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_type.return_value = "FILLING"
        mock_ingredient.get_name.return_value = "Mock Ingredient"
        mock_ingredient.get_price.return_value = 275
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is mock_ingredient

    def test_add_multiple_ingredients(self):
        "Проверка добавления нескольких ингредиентов"
        burger = Burger()
        ingredients = [
            Ingredient("FILLING", "cutlet", 100),
            Ingredient("SAUCE", "sour cream", 200),
            Ingredient("FILLING", "sausage", 300),
            Ingredient("SAUCE", "chili sauce", 300),
        ]
        for ing in ingredients:
            burger.add_ingredient(ing)       
        assert len(burger.ingredients) == 4
        assert burger.ingredients == ingredients
    
    def test_remove_ingredient(self):
        "Проверка удаления ингредиента"
        burger = Burger()
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        ingredient1 = Ingredient("FILLING", "dinosaur", 200)
        ingredient2 = Ingredient("SAUCE", "hot sauce", 100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] is ingredient2
        assert burger.ingredients[0].get_name() == "hot sauce"

    def test_move_ingredient(self):
        "Проверка перемещения ингредиента"
        burger = Burger()
        bun = Bun("white bun", 200)
        burger.set_buns(bun)
        ingredient1 = Ingredient("FILLING", "dinosaur", 200)
        ingredient2 = Ingredient("FILLING", "cutlet", 100)
        ingredient3 = Ingredient("SAUCE", "hot sauce", 100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        assert burger.ingredients == [ingredient1, ingredient2, ingredient3]
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_get_price_only_bun(self):
        "Проверка цены только булочек"
        burger = Burger()
        bun = Bun("White Bun", 200)
        burger.set_buns(bun)
        assert burger.get_price() == 400


    @pytest.mark.parametrize(
        "bun_name,bun_price,ingredients_data,expected_total",
        [
            ("black bun", 100, [], 200),
            ("white bun", 200, [("FILLING", "cutlet", 100)], 500),
            ("red bun", 300, [("FILLING", "cutlet", 100), ("SAUCE", "hot sauce", 100)], 800),
            ("black bun", 100, [("FILLING", "dinosaur", 200), ("FILLING", "sausage", 300), ("SAUCE", "chili sauce", 300)], 1000),
        ]
    ) 
    def test_get_price_with_different_combinations(self, bun_name, bun_price, ingredients_data, expected_total):
        "Проверка цены с различными комбинациями ингредиентов"
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        for ing_type, ing_name, ing_price in ingredients_data:
            ingredient = Ingredient(ing_type, ing_name, ing_price)
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_total

    def test_get_price_with_mock_ingredients(self):
        "Проверка ингредиентов с моками"
        burger = Burger()
        bun = Bun("Test Bun", 100)
        burger.set_buns(bun)
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 150
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 200
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        assert burger.get_price() == 550

    def test_get_receipt(self):
        "Проверка формирования рецепта"
        burger = Burger()
        bun = Bun("Sesame Bun", 50)
        burger.set_buns(bun)
        ingredient1 = Ingredient("FILLING", "dinosaur", 200)
        ingredient2 = Ingredient("SAUCE", "hot sauce", 100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        assert ("(==== Sesame Bun ====)") in receipt
        assert "= filling dinosaur =" in receipt
        assert "= sauce hot sauce =" in receipt
        assert "Price: 400" in receipt
        assert receipt.count("(==== Sesame Bun ====)") == 2

    def test_get_receipt_no_ingredients(self):
        "Проверка рецепта без ингредиентов"
        burger = Burger()
        bun = Bun("White Bun", 200)
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert "(==== White Bun ====)" in receipt
        assert receipt.count("(==== White Bun ====") == 2
        assert "Price: 400" in receipt


    @pytest.mark.parametrize(
        "ingredient_type,ingredient_name,ingredient_price",
        [
            ("FILLING", "cutlet", 100),
            ("SAUCE", "sour cream", 200),
            ("FILLING", "sausage", 300),
            ("SAUCE", "chili sauce", 300),
        ]
    )
    def test_receipt_with_different_ingredients(self, ingredient_type, ingredient_name, ingredient_price):
        "Проверка рецепта с различными ингредиентами"
        burger = Burger()
        bun = Bun("White Bun", 100)
        burger.set_buns(bun)
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        expected_type_lower = ingredient_type.lower()
        assert f"= {expected_type_lower} {ingredient_name} =" in receipt
        assert f"Price: {100 * 2 + ingredient_price}" in receipt

    def test_get_receipt_format(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        burger.set_buns(bun)
        ingredient1 = Ingredient("FILLING", "cutlet", 100)
        ingredient2 = Ingredient("SAUCE", "hot sauce", 100)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        receipt = burger.get_receipt()
        lines = receipt.split('\n') 
        assert lines[0] == "(==== black bun ====)"
        assert "= filling cutlet =" in lines[1]
        assert "= sauce hot sauce =" in lines[2]
        assert "(==== black bun ====)" in lines[3]
        assert "" in lines[4]
        assert "Price: 400" in lines[5]
