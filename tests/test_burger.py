import pytest
import allure
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurgerInit:

    @allure.title('Создание нового бургера')
    @allure.description('Проверяем, что новый бургер создается с пустыми значениями')
    def test_burger_init(self, burger):
        assert burger.bun is None and burger.ingredients == []

    @allure.title('Установка булочки')
    @allure.description('Проверяем корректную установку булочки')
    def test_set_buns_with_mock(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

class TestBurgerAddIngredient:

    @allure.title('Добавление одного ингредиента')
    @allure.description('Проверяем добавление одного ингредиента')
    def test_add_single_ingredient(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        assert len(burger.ingredients) == 1 and burger.ingredients[0] == mock_ingredient_sauce

    @allure.title('Добавление нескольких ингредиентов')
    @allure.description('Проверяем добавление нескольких ингредиентов')
    def test_add_multiple_ingredients(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 3 and burger.ingredients == mock_ingredients

class TestBurgerRemoveIngredient:

    @allure.title('Удаление ингредиента по индексу')
    @allure.description('Проверяем удаление ингредиента по индексу')
    def test_remove_ingredient_by_index(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)

        burger.remove_ingredient(1)
        assert (len(burger.ingredients) == 2 and 
            burger.ingredients[0] == mock_ingredients[0] and
            burger.ingredients[1] == mock_ingredients[2])

    @allure.title('Удаление первого ингредиента')
    @allure.description('Проверяем удаление первого ингредиента')
    def test_remove_first_ingredient(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        burger.remove_ingredient(0)
        assert (len(burger.ingredients) == 2 and 
            burger.ingredients[0] == mock_ingredients[1] and
            burger.ingredients[1] == mock_ingredients[2])

    @allure.title('Удаление последнего ингредиента')
    @allure.description('Проверяем удаление последнего ингредиента')
    def test_remove_last_ingredient(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        
        burger.remove_ingredient(2)
        assert (len(burger.ingredients) == 2 and 
            burger.ingredients[0] == mock_ingredients[0] and
            burger.ingredients[1] == mock_ingredients[1])

    @allure.title('Удаление ингредиента с неверным индексом')
    @allure.description('Проверяем поведение remove_ingredient() с неверным индексом')
    def test_remove_ingredient_invalid_index(self, burger, mock_ingredient_sauce):
        with allure.step("Добавить ингредиент"):
            burger.add_ingredient(mock_ingredient_sauce)
        
        with pytest.raises(IndexError):
            burger.remove_ingredient(5)  # Индекс больше длины списка

    @allure.title('Удаление ингредиента из пустого списка')
    @allure.description('Проверяем поведение remove_ingredient() из пустого списка')
    def test_remove_ingredient_from_empty_list(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    @allure.title('Параметризованные тесты для граничных случаев')
    @allure.description('Проверяем различные граничные случаи с параметризацией')
    @pytest.mark.parametrize("invalid_index", [-1, 10, 100])
    def test_remove_ingredient_parametrized_invalid_index(self, burger, mock_ingredients, invalid_index):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(invalid_index)

class TestBurgerMoveIngredient:

    @allure.title('Перемещение ингредиента')
    @allure.description('Проверяем перемещение ингредиента')
    def test_move_ingredient(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        burger.move_ingredient(0, 2)
        
        assert (len(burger.ingredients) == 3 and 
                burger.ingredients[0] == mock_ingredients[1] and
                burger.ingredients[1] == mock_ingredients[2] and
                burger.ingredients[2] == mock_ingredients[0])

    @allure.title('Перемещение ингредиента в начало')
    @allure.description('Проверяем перемещение ингредиента в начало')
    def test_move_ingredient_to_beginning(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        burger.move_ingredient(2, 0)
        assert (len(burger.ingredients) == 3 and 
                burger.ingredients[0] == mock_ingredients[2] and
                burger.ingredients[1] == mock_ingredients[0] and
                burger.ingredients[2] == mock_ingredients[1])

    @allure.title('Перемещение ингредиента в конец')
    @allure.description('Проверяем перемещение ингредиента в конец')
    def test_move_ingredient_to_end(self, burger, mock_ingredients):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        burger.move_ingredient(0, 3)
        assert (len(burger.ingredients) == 3 and 
                burger.ingredients[0] == mock_ingredients[1] and
                burger.ingredients[1] == mock_ingredients[2] and
                burger.ingredients[2] == mock_ingredients[0])

    @allure.title('Перемещение ингредиента с неверным индексом')
    @allure.description('Проверяем поведение move_ingredient() с неверным индексом')
    def test_move_ingredient_invalid_index(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)  # Неверный исходный индекс

    @allure.title('Перемещение ингредиента в неверную позицию')
    @allure.description('Проверяем поведение move_ingredient() с неверной целевой позицией')
    def test_move_ingredient_invalid_target_index(self, burger, mock_ingredient_sauce):
        burger.add_ingredient(mock_ingredient_sauce)
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 5)  # Неверная целевая позиция

    @allure.title('Перемещение ингредиента из пустого списка')
    @allure.description('Проверяем поведение move_ingredient() из пустого списка')
    def test_move_ingredient_from_empty_list(self, burger):
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 0)

    @pytest.mark.parametrize('source_index,target_index', [
        (-1, 0), (0, -1), (10, 0), (0, 10), (-1, -1), (10, 10)
    ])
    def test_move_ingredient_parametrized_invalid_indices(self, burger, mock_ingredients, source_index, target_index):
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.move_ingredient(source_index, target_index)

class TestBurgerGetPrice:

    @allure.title('Расчет цены бургера без ингредиентов')
    @allure.description('Проверяем расчет цены бургера только с булочкой')
    def test_get_price_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        price = burger.get_price()
        assert price == 200.0 and mock_bun.get_price.call_count == 1

    @allure.title('Расчет цены бургера с ингредиентами')
    @allure.description('Проверяем расчет цены бургера с булочкой и ингредиентами')
    def test_get_price_with_ingredients(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        price = burger.get_price()
        expected_price = 200.0 + 25.0 + 50.0 + 75.0  # 100*2 + 25 + 50 + 75
        assert price == expected_price

    def test_get_price_mock_calls(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        for ingredient in mock_ingredients:
            burger.add_ingredient(ingredient)
        burger.get_price()
        assert (mock_bun.get_price.call_count == 1 and 
                all(ingredient.get_price.call_count == 1 for ingredient in mock_ingredients))

    @allure.title('Расчет цены с разными типами ингредиентов')
    @allure.description('Проверяем расчет цены с соусами и начинками')
    @pytest.mark.parametrize('bun_price,ingredient_prices,expected_total', [
        (100.0, [50.0, 75.0], 325.0),  # 100*2 + 50 + 75
        (200.0, [25.0, 100.0], 525.0),  # 200*2 + 25 + 100
        (150.0, [30.0, 45.0, 60.0], 435.0),  # 150*2 + 30 + 45 + 60
    ])
    def test_get_price_parametrized(self, burger, bun_price, ingredient_prices, expected_total):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        actual_price = burger.get_price()
        assert actual_price == expected_total

class TestBurgerGetReceipt:

    @allure.title('Генерация чека без ингредиентов')
    @allure.description('Проверяем генерацию чека только с булочкой')
    def test_get_receipt_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected_receipt = "(==== black bun ====)\n(==== black bun ====)\n\nPrice: 200.0"
        assert receipt == expected_receipt and mock_bun.get_name.call_count == 2

    @allure.title('Генерация чека с ингредиентами')
    @allure.description('Проверяем генерацию чека с булочкой и ингредиентами')
    def test_get_receipt_with_ingredients(self, burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        receipt = burger.get_receipt()
        expected_lines = [
            "(==== black bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== black bun ====)",
            "",
            "Price: 325.0"
        ]
        expected_receipt = "\n".join(expected_lines)
        assert receipt == expected_receipt

    @allure.title('Генерация чека с разными типами ингредиентов')
    @allure.description('Проверяем генерацию чека с разными типами ингредиентов')
    @pytest.mark.parametrize('bun_name,ingredients_data,expected_price', [
        ("white bun", [("SAUCE", "hot sauce"), ("FILLING", "cutlet")], 300.0),
        ("red bun", [("SAUCE", "sour cream"), ("SAUCE", "chili sauce")], 300.0),
        ("black bun", [("FILLING", "dinosaur"), ("FILLING", "sausage")], 300.0),
    ])
    def test_get_receipt_parametrized(self, burger, bun_name, ingredients_data, expected_price):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        for ingredient_type, ingredient_name in ingredients_data:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_name.return_value = ingredient_name
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_price.return_value = 50.0
            burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        assert (lines[0] == f"(==== {bun_name} ====)" and
                lines[-3] == f"(==== {bun_name} ====)" and
                lines[-1] == f"Price: {expected_price}")

    @pytest.mark.parametrize("bun_name,ingredients_data,expected_price", [
        ("white bun", [("SAUCE", "hot sauce"), ("FILLING", "cutlet")], 325.0),
        ("red bun", [("SAUCE", "sour cream"), ("SAUCE", "chili sauce")], 400.0),
        ("black bun", [("FILLING", "dinosaur"), ("FILLING", "sausage")], 375.0),
    ])
    def test_get_receipt_parametrized_ingredients(self, burger, bun_name, ingredients_data, expected_price):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = 100.0
        burger.set_buns(mock_bun)
        for ingredient_type, ingredient_name in ingredients_data:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_name.return_value = ingredient_name
            mock_ingredient.get_type.return_value = ingredient_type
            mock_ingredient.get_price.return_value = 50.0
            burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        ingredient_lines = lines[1:-2]
        assert all(ingredient_lines[i] == f"= {ingredients_data[i][0].lower()} {ingredients_data[i][1]} =" 
                    for i in range(len(ingredients_data)))