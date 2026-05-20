from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""
    
    # ========== Тесты для set_buns ==========
    
    def test_set_buns(self, burger, bun):
        """Тест установки булочек"""
        burger.set_buns(bun)
        
        assert burger.bun == bun
        assert burger.bun.get_name() == "black bun"
        assert burger.bun.get_price() == 100

    # ========== Тесты для add_ingredient ==========
    
    def test_add_ingredient(self, burger, filling_ingredient):
        """Тест добавления одного ингредиента"""
        burger.add_ingredient(filling_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == filling_ingredient
        assert burger.ingredients[0].get_name() == "cutlet"
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING
        assert burger.ingredients[0].get_price() == 100

    def test_add_multiple_ingredients(self, burger, filling_ingredient, another_filling_ingredient, sauce_ingredient):
        """Тест добавления нескольких ингредиентов"""
        burger.add_ingredient(filling_ingredient)
        burger.add_ingredient(another_filling_ingredient)
        burger.add_ingredient(sauce_ingredient)
        
        assert len(burger.ingredients) == 3
        assert burger.ingredients[0].get_name() == "cutlet"
        assert burger.ingredients[1].get_name() == "dinosaur"
        assert burger.ingredients[2].get_name() == "hot sauce"

    # ========== Тесты для remove_ingredient ==========
    
    def test_remove_ingredient_middle(self, burger_with_ingredients):
        """Тест удаления ингредиента из середины"""
        burger_with_ingredients.remove_ingredient(1)
        
        assert len(burger_with_ingredients.ingredients) == 2
        assert burger_with_ingredients.ingredients[0].get_name() == "cutlet"
        assert burger_with_ingredients.ingredients[1].get_name() == "hot sauce"

    def test_remove_ingredient_first(self, burger, filling_ingredient, another_filling_ingredient):
        """Тест удаления первого ингредиента"""
        burger.add_ingredient(filling_ingredient)
        burger.add_ingredient(another_filling_ingredient)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == "dinosaur"

    def test_remove_ingredient_last(self, burger, filling_ingredient, another_filling_ingredient):
        """Тест удаления последнего ингредиента"""
        burger.add_ingredient(filling_ingredient)
        burger.add_ingredient(another_filling_ingredient)
        
        burger.remove_ingredient(1)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == "cutlet"

    # ========== Тесты для move_ingredient ==========
    
    def test_move_ingredient_from_0_to_1(self, burger_with_ingredients):
        """Тест перемещения ингредиента с индекса 0 на индекс 1"""
        burger_with_ingredients.move_ingredient(0, 1)
        
        assert burger_with_ingredients.ingredients[0].get_name() == "dinosaur"
        assert burger_with_ingredients.ingredients[1].get_name() == "cutlet"
        assert burger_with_ingredients.ingredients[2].get_name() == "hot sauce"

    def test_move_ingredient_from_1_to_0(self, burger_with_ingredients):
        """Тест перемещения ингредиента с индекса 1 на индекс 0"""
        burger_with_ingredients.move_ingredient(1, 0)
        
        assert burger_with_ingredients.ingredients[0].get_name() == "dinosaur"
        assert burger_with_ingredients.ingredients[1].get_name() == "cutlet"
        assert burger_with_ingredients.ingredients[2].get_name() == "hot sauce"

    def test_move_ingredient_from_2_to_0(self, burger_with_ingredients):
        """Тест перемещения ингредиента с индекса 2 на индекс 0"""
        burger_with_ingredients.move_ingredient(2, 0)
        
        assert burger_with_ingredients.ingredients[0].get_name() == "hot sauce"
        assert burger_with_ingredients.ingredients[1].get_name() == "cutlet"
        assert burger_with_ingredients.ingredients[2].get_name() == "dinosaur"

    def test_move_ingredient_from_1_to_2(self, burger_with_ingredients):
        """Тест перемещения ингредиента с индекса 1 на индекс 2"""
        burger_with_ingredients.move_ingredient(1, 2)
        
        assert burger_with_ingredients.ingredients[0].get_name() == "cutlet"
        assert burger_with_ingredients.ingredients[1].get_name() == "hot sauce"
        assert burger_with_ingredients.ingredients[2].get_name() == "dinosaur"

    def test_move_ingredient_same_index(self, burger_with_ingredients):
        """Тест перемещения ингредиента на тот же индекс"""
        burger_with_ingredients.move_ingredient(1, 1)
        
        # Порядок не должен измениться
        assert burger_with_ingredients.ingredients[0].get_name() == "cutlet"
        assert burger_with_ingredients.ingredients[1].get_name() == "dinosaur"
        assert burger_with_ingredients.ingredients[2].get_name() == "hot sauce"

    # ========== Тесты для get_price ==========
    
    def test_get_price_with_bun_only(self, burger_with_bun):
        """Тест расчета цены только с булочкой"""
        price = burger_with_bun.get_price()
        
        assert price == 200  # 100 * 2

    def test_get_price_with_one_ingredient(self, burger_with_bun, filling_ingredient):
        """Тест расчета цены с булочкой и одним ингредиентом"""
        burger_with_bun.add_ingredient(filling_ingredient)
        
        price = burger_with_bun.get_price()
        
        assert price == 300  # 100*2 + 100

    def test_get_price_with_two_ingredients(self, burger_with_bun, filling_ingredient, another_filling_ingredient):
        """Тест расчета цены с булочкой и двумя ингредиентами"""
        burger_with_bun.add_ingredient(filling_ingredient)
        burger_with_bun.add_ingredient(another_filling_ingredient)
        
        price = burger_with_bun.get_price()
        
        assert price == 500  # 100*2 + 100 + 200

    def test_get_price_with_three_ingredients(self, burger_with_bun, filling_ingredient, another_filling_ingredient, sauce_ingredient):
        """Тест расчета цены с булочкой и тремя ингредиентами"""
        burger_with_bun.add_ingredient(filling_ingredient)
        burger_with_bun.add_ingredient(another_filling_ingredient)
        burger_with_bun.add_ingredient(sauce_ingredient)
        
        price = burger_with_bun.get_price()
        
        assert price == 500  # 100*2 + 100 + 200 + 100 = 500

    def test_get_price_with_four_ingredients(self, burger_with_bun):
        """Тест расчета цены с булочкой и четырьмя ингредиентами"""
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        ingredient4 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        
        burger_with_bun.add_ingredient(ingredient1)
        burger_with_bun.add_ingredient(ingredient2)
        burger_with_bun.add_ingredient(ingredient3)
        burger_with_bun.add_ingredient(ingredient4)
        
        price = burger_with_bun.get_price()
        
        assert price == 900  # 100*2 + 100 + 300 + 100 + 200 = 900

    # ========== Тесты для get_receipt ==========
    
    def test_get_receipt_with_bun_only(self, burger_with_bun):
        """Тест получения чека только с булочкой"""
        receipt = burger_with_bun.get_receipt()
        
        expected_receipt = """(==== black bun ====)
(==== black bun ====)

Price: 200"""
        assert receipt == expected_receipt

    def test_get_receipt_with_ingredients(self, burger_with_ingredients):
        """Тест получения чека с булочкой и ингредиентами"""
        receipt = burger_with_ingredients.get_receipt()
        
        expected_receipt = """(==== black bun ====)
= filling cutlet =
= filling dinosaur =
= sauce hot sauce =
(==== black bun ====)

Price: 500"""
        assert receipt == expected_receipt

    def test_get_receipt_with_mixed_ingredients(self, burger_with_bun):
        """Тест чека с разными типами ингредиентов"""
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        
        burger_with_bun.add_ingredient(sauce)
        burger_with_bun.add_ingredient(filling)
        
        receipt = burger_with_bun.get_receipt()
        
        expected_receipt = """(==== black bun ====)
= sauce sour cream =
= filling sausage =
(==== black bun ====)

Price: 700"""
        assert receipt == expected_receipt

    def test_get_receipt_preserves_order(self, burger_with_bun, sauce_ingredient, filling_ingredient, another_filling_ingredient):
        """Тест: чек сохраняет порядок добавления ингредиентов"""
        burger_with_bun.add_ingredient(sauce_ingredient)      # hot sauce
        burger_with_bun.add_ingredient(filling_ingredient)    # cutlet
        burger_with_bun.add_ingredient(another_filling_ingredient)  # dinosaur
        
        receipt = burger_with_bun.get_receipt()
        
        # Проверяем, что ингредиенты в чеке идут в том же порядке
        lines = receipt.split('\n')
        assert "= sauce hot sauce =" in lines[1]
        assert "= filling cutlet =" in lines[2]
        assert "= filling dinosaur =" in lines[3]

    # ========== Интеграционные тесты ==========
    
    def test_complete_burger_workflow(self, burger, bun, filling_ingredient, another_filling_ingredient, sauce_ingredient):
        """Тест полного рабочего процесса с бургером (как в praktikum.py)"""
        # Собираем бургер
        burger.set_buns(bun)
        burger.add_ingredient(another_filling_ingredient)  # dinosaur
        burger.add_ingredient(sauce_ingredient)           # hot sauce
        burger.add_ingredient(filling_ingredient)         # cutlet
        
        # Перемещаем ингредиент с индекса 2 на индекс 1
        burger.move_ingredient(2, 1)
        
        # Проверяем порядок после перемещения
        assert burger.ingredients[0].get_name() == "dinosaur"
        assert burger.ingredients[1].get_name() == "cutlet"
        assert burger.ingredients[2].get_name() == "hot sauce"
        
        # Удаляем ингредиент с индексом 2
        burger.remove_ingredient(2)
        
        # Проверяем после удаления
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].get_name() == "dinosaur"
        assert burger.ingredients[1].get_name() == "cutlet"
        
        # Проверяем цену
        expected_price = 100 * 2 + 200 + 100  # 500
        assert burger.get_price() == expected_price
