import pytest
from unittest.mock import Mock, patch
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("Краторная булка N-200i", 1255)
        burger.set_buns(bun)
        
        assert burger.bun == bun
        assert burger.bun.get_name() == "Краторная булка N-200i"
        assert burger.bun.get_price() == 1255

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        burger.add_ingredient(ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_add_multiple_ingredients(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ing1
        assert burger.ingredients[1] == ing2

    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing2

    def test_move_ingredient(self):
        burger = Burger()
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988)
        ing3 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        
        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[0] == ing2
        assert burger.ingredients[1] == ing3
        assert burger.ingredients[2] == ing1

    def test_get_price_with_mocks(self):
        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1255
        
        mock_ing1 = Mock()
        mock_ing1.get_price.return_value = 80
        mock_ing2 = Mock()
        mock_ing2.get_price.return_value = 988
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        
        assert burger.get_price() == 3578

    def test_get_price_with_real_objects(self):
        burger = Burger()
        bun = Bun("Краторная булка N-200i", 1255)
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988)
        
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        assert burger.get_price() == 3578

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("Краторная булка N-200i", 1255)
        ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        ing2 = Ingredient(INGREDIENT_TYPE_FILLING, "Филе Люминесцентного тетраодонтимформа", 988)
        
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        
        receipt = burger.get_receipt()
        
        assert "(==== Краторная булка N-200i ====)" in receipt
        # Исправлено: правильный регистр (как в реальном чеке)
        assert "= sauce Соус фирменный Space Sauce =" in receipt
        assert "= filling Филе Люминесцентного тетраодонтимформа =" in receipt
        assert "Price: 3578" in receipt

    def test_empty_burger_receipt(self):
        burger = Burger()
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        burger.set_buns(bun)
        
        receipt = burger.get_receipt()
        
        assert "(==== Флюоресцентная булка R2-D3 ====)" in receipt
        assert "Price: 1976" in receipt

    @pytest.mark.parametrize("bun_name, bun_price, expected_price", [
        ("Краторная булка N-200i", 1255, 2510),
        ("Флюоресцентная булка R2-D3", 988, 1976)
    ])
    def test_different_buns_price(self, bun_name, bun_price, expected_price):
        burger = Burger()
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_name, ingredient_price", [
        ("Хрустящие минеральные кольца", 300),
        ("Кристаллы марсианских альфа-сахаридов", 762),
        ("Мини-салат Экзо-Плантаго", 4400),
        ("Сыр с астероидной плесенью", 4142),
        ("Мясо бессмертных моллюсков Protostomia", 1337),
        ("Говяжий метеорит (отбивная)", 3000),
        ("Биокотлета из марсианской Магнолии", 424)
    ])
    def test_add_different_ingredients(self, ingredient_name, ingredient_price):
        burger = Burger()
        bun = Bun("Краторная булка N-200i", 1255)
        burger.set_buns(bun)
        
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        
        expected_price = 1255 * 2 + ingredient_price
        assert burger.get_price() == expected_price
        assert burger.ingredients[0].get_name() == ingredient_name