import pytest


class TestBurger:
    
    def test_set_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, burger, ingredient_mock):
        initial_count = len(burger.ingredients)
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == initial_count + 1
        assert burger.ingredients[-1] == ingredient_mock

    def test_remove_ingredient(self, burger, ingredient_mock, cutlet_ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == cutlet_ingredient_mock

    def test_move_ingredient(self, burger, ingredient_mock, cutlet_ingredient_mock, cheese_ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        burger.add_ingredient(cheese_ingredient_mock)
        
        burger.move_ingredient(0, 2)
        
        assert burger.ingredients[2] == ingredient_mock
        assert burger.ingredients[0] == cutlet_ingredient_mock

    def test_get_price(self, basic_burger_setup, bun_mock, ingredient_mock, cutlet_ingredient_mock):
        burger = basic_burger_setup
        
        expected_price = (
            bun_mock.get_price() * 2 +  
            ingredient_mock.get_price() +
            cutlet_ingredient_mock.get_price()
        )
        
        assert burger.get_price() == expected_price

    def test_get_receipt_contains_all_elements(self, basic_burger_setup, bun_mock, ingredient_mock, cutlet_ingredient_mock):
        burger = basic_burger_setup
        
        receipt = burger.get_receipt()
        
        expected_elements = [
            f"(==== {bun_mock.get_name()} ====)",
            f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} =",
            f"= {cutlet_ingredient_mock.get_type().lower()} {cutlet_ingredient_mock.get_name()} =",
            f"Price: {burger.get_price()}"
        ]
        
        for element in expected_elements:
            assert element in receipt, f"Элемент '{element}' не найден в рецепте"

    def test_get_receipt_bun_appears_twice(self, burger, white_bun_mock):
        burger.set_buns(white_bun_mock)
        
        receipt = burger.get_receipt()
        bun_section = f"(==== {white_bun_mock.get_name()} ====)"
        
        assert receipt.count(bun_section) == 2, "Булка должна встречаться дважды в рецепте"

    def test_get_receipt_only_buns_structure(self, burger, white_bun_mock):
        burger.set_buns(white_bun_mock)
        
        receipt = burger.get_receipt()
        
        bun_section = f"(==== {white_bun_mock.get_name()} ====)"
        price_section = f"Price: {burger.get_price()}"
        
        assert bun_section in receipt
        assert price_section in receipt
        assert receipt.count(bun_section) == 2
        
        lines_with_single_equals = [line for line in receipt.split('\n') 
                                  if line.count('=') == 2 and '(====' not in line]
        assert len(lines_with_single_equals) == 0, "Не должно быть строк с ингредиентами"

    def test_get_receipt_no_bun_raises_exception(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_ingredient_order_preserved(self, burger, red_bun_mock, ingredient_mock, cutlet_ingredient_mock, cheese_ingredient_mock):
        burger.set_buns(red_bun_mock)
        
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        burger.add_ingredient(cheese_ingredient_mock)
        
        receipt = burger.get_receipt()
        
        receipt_lower = receipt.lower()
        ingredient_positions = [
            receipt_lower.find(ingredient_mock.get_name().lower()),
            receipt_lower.find(cutlet_ingredient_mock.get_name().lower()),
            receipt_lower.find(cheese_ingredient_mock.get_name().lower())
        ]
        
        assert all(pos != -1 for pos in ingredient_positions), "Не все ингредиенты найдены в рецепте"
        assert ingredient_positions[0] < ingredient_positions[1] < ingredient_positions[2], "Порядок ингредиентов нарушен"

    def test_get_price_empty_burger(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        
        expected_price = bun_mock.get_price() * 2
        assert burger.get_price() == expected_price

    def test_get_price_no_buns_raises_exception(self, burger, ingredient_mock):
        burger.add_ingredient(ingredient_mock)
        
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_comprehensive(self, burger, white_bun_mock, ingredient_mock, cutlet_ingredient_mock):
        burger.set_buns(white_bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(cutlet_ingredient_mock)
        
        receipt = burger.get_receipt()
        
        expected_elements = [
            f"(==== {white_bun_mock.get_name()} ====)",
            f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} =",
            f"= {cutlet_ingredient_mock.get_type().lower()} {cutlet_ingredient_mock.get_name()} =",
            f"Price: {burger.get_price()}"
        ]
        
        for element in expected_elements:
            assert element in receipt, f"Элемент '{element}' не найден в рецепте"
        
        bun_count = receipt.count(f"(==== {white_bun_mock.get_name()} ====)")
        assert bun_count == 2, f"Булка должна встречаться 2 раза, найдено {bun_count}"
        
        expected_price = white_bun_mock.get_price() * 2 + ingredient_mock.get_price() + cutlet_ingredient_mock.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_single_ingredient(self, burger, red_bun_mock, cheese_ingredient_mock):
        burger.set_buns(red_bun_mock)
        burger.add_ingredient(cheese_ingredient_mock)
        
        receipt = burger.get_receipt()
        
        expected_elements = [
            f"(==== {red_bun_mock.get_name()} ====)",
            f"= {cheese_ingredient_mock.get_type().lower()} {cheese_ingredient_mock.get_name()} =",
            f"Price: {burger.get_price()}"
        ]
        
        for element in expected_elements:
            assert element in receipt, f"Элемент '{element}' не найден в рецепте"
        
        assert receipt.count(f"(==== {red_bun_mock.get_name()} ====)") == 2

    def test_get_receipt_multiple_sauces(self, burger, bun_mock, ingredient_mock, sour_cream_ingredient_mock):
        burger.set_buns(bun_mock)  
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(sour_cream_ingredient_mock)
    
        receipt = burger.get_receipt()
    
        assert f"(==== {bun_mock.get_name()} ====)" in receipt
        assert f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} =" in receipt
        assert f"= {sour_cream_ingredient_mock.get_type().lower()} {sour_cream_ingredient_mock.get_name()} =" in receipt
        assert f"Price: {burger.get_price()}" in receipt
    
        receipt_lower = receipt.lower()
        assert ingredient_mock.get_name().lower() in receipt_lower
        assert sour_cream_ingredient_mock.get_name().lower() in receipt_lower

    def test_receipt_has_correct_price_format(self, basic_burger_setup):
        burger = basic_burger_setup
        
        receipt = burger.get_receipt()
        price_line = f"Price: {burger.get_price()}"
        
        assert price_line in receipt, "Цена должна быть в формате 'Price: X'"

    def test_receipt_has_ingredient_type_in_lowercase(self, burger, white_bun_mock, ingredient_mock):
        burger.set_buns(white_bun_mock)
        burger.add_ingredient(ingredient_mock)
        
        receipt = burger.get_receipt()
        ingredient_section = f"= {ingredient_mock.get_type().lower()} {ingredient_mock.get_name()} ="
        
        assert ingredient_section in receipt, "Тип ингредиента должен быть в нижнем регистре"