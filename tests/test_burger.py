import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
class TestBurger:
    # Тест метода set_buns. 
    def test_set_buns(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)

        assert burger.bun == bun

    # Тест метода add_ingredient. 
    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    # Тест метода remove_ingredient.
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()

        # убедимся что список точно пустой
        assert len(burger.ingredients) == 0  

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0    

    # Тест метода remove_ingredient.
    # Несуществующий индекс ингредиента    
    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

        assert burger.ingredients == [ingredient]

    # Тест метода move_ingredient.
    def test_move_ingredient(self):
        burger = Burger()

        ing1 = Mock()
        ing2 = Mock()
        ing3 = Mock()

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ing2, ing3, ing1]

    # Тест метода get_price общий случай.
    # Изучив методы класса, принимаем, что в конечной стоимости бургера стоимость булки = х2
    # Этот вывод подтверждается в методе get_receipt

    def test_get_price(self):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = 100

        ing1 = Mock()
        ing1.get_price.return_value = 50

        ing2 = Mock()
        ing2.get_price.return_value = 150

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        expected_price = 100 * 2 + 50 + 150

        assert burger.get_price() == expected_price

    # тест метода get_price
    # Бургер без ингредентов
    def test_get_price_only_bun(self):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = 100

        burger.set_buns(bun)

        assert burger.get_price() == 200

    # тест метода get_price
    # Бургер без булки и без ингредиентов
    def test_get_price_without_bun(self):
        burger = Burger()

        with pytest.raises(AttributeError):
            burger.get_price()

    # тест метода get_price
    # различные варианты ингредиентов
    @pytest.mark.parametrize("bun_price, ingredients, expected", [
        (100, [50, 50, 100, 150], 550),
        (200, [100], 500),
        (50, [], 100),
    ])
    def test_get_price_parametrized(self,bun_price, ingredients, expected):
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredients:
            ing = Mock()
            ing.get_price.return_value = price
            burger.add_ingredient(ing)

        assert burger.get_price() == expected

    # тест метода get_receipt
    # Базовый тест, полное совпадение 
    def test_get_receipt_full_match(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "Черная булка"
        bun.get_price.return_value = 100

        ing1 = Mock()
        ing1.get_type.return_value = "SAUCE"
        ing1.get_name.return_value = "острый"
        ing1.get_price.return_value = 50

        ing2 = Mock()
        ing2.get_type.return_value = "FILLING"
        ing2.get_name.return_value = "котлета"
        ing2.get_price.return_value = 100

        ing3 = Mock()
        ing3.get_type.return_value = "FILLING"
        ing3.get_name.return_value = "сыр"
        ing3.get_price.return_value = 50

        ing4 = Mock()
        ing4.get_type.return_value = "FILLING"
        ing4.get_name.return_value = "перец халапенья"
        ing4.get_price.return_value = 35

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.add_ingredient(ing4)

        receipt = burger.get_receipt()

        expected = (
            "(==== Черная булка ====)\n"
            "= sauce острый =\n"
            "= filling котлета =\n"
            "= filling сыр =\n"
            "= filling перец халапенья =\n"
            "(==== Черная булка ====)\n\n"
            "Price: 435"
        )

        assert receipt == expected    

    # тест метода get_receipt
    # проверка количества строк
    def test_get_receipt_lines_count(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "bun"
        bun.get_price.return_value = 100
        
        ing1 = Mock()
        ing1.get_type.return_value = "SAUCE"
        ing1.get_name.return_value = "острый"
        ing1.get_price.return_value = 50

        burger.set_buns(bun)
        burger.add_ingredient(ing1)

        receipt = burger.get_receipt()
        lines = receipt.split("\n")

        assert len(lines) == 5  

    # тест метода get_receipt
    # проверка порядка ингредиентов

    def test_get_receipt_ingredients_order(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "bun"
        bun.get_price.return_value = 100

        ing1 = Mock()
        ing1.get_type.return_value = "SAUCE"
        ing1.get_name.return_value = "first line"
        ing1.get_price.return_value = 10

        ing2 = Mock()
        ing2.get_type.return_value = "FILLING"
        ing2.get_name.return_value = "second line"
        ing2.get_price.return_value = 20
        
        ing3 = Mock()
        ing3.get_type.return_value = "FILLING"
        ing3.get_name.return_value = "third line"
        ing3.get_price.return_value = 20

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)

        receipt = burger.get_receipt()
        lines = receipt.split("\n")

        assert "first line" in lines[1]
        assert "second line" in lines[2]    
        assert "third line" in lines[3]    

    # тест метода get_receipt
    # отсутствие лишнего текста в чеке
    def test_get_receipt_no_extra_lines(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "bun"
        bun.get_price.return_value = 100

        burger.set_buns(bun)

        receipt = burger.get_receipt()

        # Проверяем, что нет лишних символов в начале/конце
        assert receipt.startswith("(==== bun ====)")
        assert receipt.endswith("Price: 200")    

    # тест метода get_receipt
    # формата строки ингредиента
    def test_get_receipt_ingredient_format(self):
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "bun"
        bun.get_price.return_value = 100

        ing = Mock()
        ing.get_type.return_value = "SAUCE"
        ing.get_name.return_value = "ketchup"
        ing.get_price.return_value = 50

        burger.set_buns(bun)
        burger.add_ingredient(ing)

        receipt = burger.get_receipt()

        assert "= sauce ketchup =" in receipt
