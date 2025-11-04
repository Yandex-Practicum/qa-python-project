from ..burger import Burger
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_bun_return_correct_bun(self):
        """Проверяет, что метод set_buns корректно устанавливает все параметры булочки"""
        bun = Bun("Краторная булка N-200i", 1255)
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun
        assert burger.bun.get_name() == "Краторная булка N-200i"
        assert burger.bun.get_price() == 1255

    def test_add_ingredient_succesfull_add(self):
        """Проверяет, что метод add_ingredient добавил ингредиенты в бургер"""

        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spice-X", 90)
        
        burger.add_ingredient(ingredient)
        
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_succesfull_remove(self):
        """Проверяет, что метод remove_ingredient удалил ингредиенты из бургера"""

        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spice-X", 90)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient_succesfull_remove(self):
        """Проверяет, что метод move_ingredient успешно переместил ингредиенты"""

        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spice-X", 90)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80)
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient3
        assert burger.ingredients[2] == ingredient1

    def test_get_price_calculates_correct_total(self):
        """Проверяет, что метод get_price корректно рассчитывает общую стоимость"""

        burger = Burger()
        
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 50
        
        mock_ingredient2 = Mock()  
        mock_ingredient2.get_price.return_value = 75
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        result = burger.get_price()
        
        mock_bun.get_price.assert_called_once()
        mock_ingredient1.get_price.assert_called_once()
        mock_ingredient2.get_price.assert_called_once()

        assert result == 325  # 100*2 + 50 + 75

    def test_get_receipt_returns_correct_format(self):
        """Метод get_receipt возвращает чек в правильном формате с корректными данными"""

        burger = Burger()
        bun = Bun("Краторная булка N-200i", 1255)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус Spice-X", 90)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжий метеорит (отбивная)", 3000)
        
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        receipt = burger.get_receipt()
        
        expected_receipt = [
            "(==== Краторная булка N-200i ====)",
            "= sauce Соус Spice-X =",
            "= filling Говяжий метеорит (отбивная) =", 
            "(==== Краторная булка N-200i ====)",
            "",
            "Price: 5600"
        ]
        assert receipt == '\n'.join(expected_receipt)
